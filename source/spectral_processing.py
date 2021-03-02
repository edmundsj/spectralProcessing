import numpy as np
import pandas as pd
from scipy.signal.windows import hann

def getPowerSpectrum(data, filtering='box', siding='single'):
    """
    Computes the single-or double-sided power spectrum with different types
    of filetring (hann, boxcar)

    :param data: data to be transformed
    :param filtering: Filtering type - hann or box
    :param siding: 'single' or 'double' sided spectrum.

    """
    if not isinstance(data, np.ndarray):
        raise ValueError(f"Function not implemented for type {type(data)},"+ "only np.ndarray.")
    data_length = len(data)
    half_data_length = int((data_length/2+1))

    if filtering == 'box':
        window = 1
    elif filtering == 'hann':
        hann_normalized = hann(data_length) / \
            np.sqrt(np.mean(np.square(hann(data_length))))
        window = hann_normalized
    bare_fft = np.fft.fft(data * window / data_length)
    spectral_power_double_sided = np.square(np.abs(bare_fft))

    # Change PSD from e^jx to sin(x)
    spectral_power_single_sided = \
        2 * spectral_power_double_sided[0:half_data_length]
    # DC component does not need to be corrected.
    spectral_power_single_sided[0] /= 2

    if siding == 'single':
        return spectral_power_single_sided
    else:
        return spectral_power_double_sided
