import numpy as np
import pandas as pd
from scipy.signal.windows import hann
from Plotting import plt, prettifyPlot

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
            data, window_data, siding=siding)
    else:
        raise ValueError(f"Function not implemented for type {type(data)},"+
                         "only np.ndarray, pd.DataFrame.")

    return power_spectrum

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

