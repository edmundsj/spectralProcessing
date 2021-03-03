"""
TODO: Add power spectrum plotting for pandas as well as numpy, separate out the
two.
"""
import numpy as np
import pandas as pd
from scipy.signal.windows import hann
from Plotting import plt, prettifyPlot
from pint import UnitRegistry
import re
ureg = UnitRegistry()

def getPowerSpectrum(data, window='box', siding='single'):
    """
    Computes the single-or double-sided power spectrum with different types
    of filetring (hann, boxcar)

    :param data: data to be transformed
    :param window: window type - hann or box
    :param siding: 'single' or 'double' sided spectrum.

    """
    data_length = len(data)

    if window == 'box' or window == 'boxcar':
        window_data = 1
    elif window == 'hann':
        hann_normalized = hann(data_length) / \
            np.sqrt(np.mean(np.square(hann(data_length))))
        window_data = hann_normalized
    else:
        raise ValueError(
            f'Window type {window} not supported. Supported types are \
            box and hann')
    if isinstance(data, np.ndarray):
        power_spectrum = getPowerSpectrumNumpy(
            data, window_data, siding=siding)
    elif isinstance(data, pd.DataFrame):
        power_spectrum = getPowerSpetrumPandas(
            data, window_data=window_data, siding=siding)
    else:
        raise ValueError(f"Function not implemented for type {type(data)},"+
                         "only np.ndarray, pd.DataFrame.")

    return power_spectrum

def getPowerSpetrumPandas(data, window_data=1, siding='single'):
    sampling_period = extractSamplingPeriod(data)
    sampling_frequency_Hz = (1 / sampling_period).to(ureg.Hz).magnitude

    power_quantity = extractUnit(data.columns.values[1])
    power_magnitude = power_quantity.magnitude
    power_unit = power_quantity.units
    power_unit_string = r'Power $({:~}^2)$'.format(power_unit)
    #breakpoint()

    half_data_length = int((len(data)/2+1))
    if siding == 'double':
        frequencies = np.linspace(-sampling_frequency_Hz/2,
                                  sampling_frequency_Hz/2,
                                  2*half_data_length - 1)
    elif siding == 'single':
        frequencies = np.linspace(0, sampling_frequency_Hz/2,
                                  half_data_length)
    else: raise ValueError(f'No such siding {siding}')
    fft_data = getPowerSpectrumNumpy(
        data.iloc[:,1].values,
        window_data=window_data, siding=siding)
    overall_data = pd.DataFrame(
        {'Frequency (Hz)': frequencies, power_unit_string: fft_data})
    return overall_data

def getPowerSpectrumNumpy(data, window_data, siding='single'):
    bare_fft = np.fft.fft(data * window_data / len(data))
    power_spectrum = np.square(np.abs(bare_fft))
    half_data_length = int((len(data)/2+1))
    if siding == 'single':
        # Change PSD from e^jx to sin(x)
        power_spectrum = \
            2 * power_spectrum[0:half_data_length]
        # DC component does not need to be corrected.
        power_spectrum[0] /= 2

    return power_spectrum

def powerSpectrumPlot(spectrum, sampling_frequency, siding='single'):
    fig, ax = plt.subplots()
    prettifyPlot(fig=fig, ax=ax)
    data_length = len(spectrum)
    frequency_spacing = sampling_frequency / 2 / data_length
    frequencies = np.arange(0, data_length * frequency_spacing,
                            frequency_spacing)
    ax.plot(frequencies, 10*np.log10(spectrum))
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Power (dBx)')
    return fig, ax

def extractSamplingPeriod(data):
    # For now, assume time is the first variable in the column
    columns = data.columns.values
    time_column = [('Time' or 'time') in c for c in columns]
    string = columns[time_column][0]
    delta_time = data[string][1] - data[string][0]

    sampling_period = delta_time * extractUnit(string)
    return sampling_period

def extractUnit(unit_string):
    # Search for anything in parentheses, interpret as a unit.
    unit_pattern = re.compile('\(\w+\)')
    match = unit_pattern.search(unit_string)
    if match == None:
        raise ValueError(f'Cannot match units of string {string}')

    bare_unit = match.group()[1:-1] # remove parentheses
    unit = 1 * ureg.parse_expression(bare_unit)
    return unit
