import context
import unittest
import numpy as np
from numpy.testing import assert_equal, assert_allclose
from spectral_processing import getPowerSpectrum

class TestSpectralPower(unittest.TestCase):
    def setUp(self):
        pass # Set up to be run before every test case

    @classmethod
    def setUpClass(cls):
        pass # Set up to be run once at the beginning 

    def testPowerSpectrumBoxcar(self):
        """
        Tests calculation of the power spectrum with a boxcar window
        """
        # Tests the case where we have an even number of samples
        raw_data = np.array([1, 2, 3, 4, 5, 0])
        actual_spectrum = \
                getPowerSpectrum(raw_data, filtering='box', siding='single')
        desired_spectrum = np.array([6.25, 2*1, 2*1/3.0, 2*1/4.0])
        assert_allclose(actual_spectrum, desired_spectrum)

        # Odd number of samples
        raw_data = np.array([1, 2, 3, 4, 5, 0,1])
        actual_spectrum = getPowerSpectrum(raw_data, filtering='box',
                                           siding='single')
        desired_spectrum = np.array([5.224489795918367,
                                     2*0.9303959383749711,2*0.21858791491176946,
                                     2*0.2387712487540753])
        assert_allclose(actual_spectrum, desired_spectrum)

    def testPowerSpectrumSinewaveHann(self):
        """
        Tests the power spectrum of a sinewave with a Hann window
        """
        x = np.arange(-5, 5+0.5, 0.5)
        raw_data = np.sin(x)
        actual_spectrum = getPowerSpectrum(raw_data, filtering='hann',
                                           siding='single')
        desired_spectrum = np.array([4.367188082510738e-37,
                                     2*0.09791637933291152,
                                     2*0.13736140613819783,
                                     2*0.015585927491469722,
                                     2*0.0000995891811181273,
                                     2*7.064948406227207e-6,
                                     2*8.781078402325934e-7,
                                     2*1.1447549848704329e-7,
                                     2*7.504694473409487e-9,
                                     2*7.232988034990556e-10,
                                     2*5.1913320650517704e-9])
        assert_allclose(actual_spectrum, desired_spectrum, atol=1e-15)
        total_power = np.sum(desired_spectrum)
        assert_equal(total_power, 0.501942746189535)

    def testPowerSpectrumSinewaveBoxcar(self):
        """
        Tests teh power spectrum of a sinewave with no hann window.

        """
        x = np.arange(-5, 5+0.5, 0.5)
        raw_data = np.sin(x)
        actual_spectrum = getPowerSpectrum(raw_data, filtering='box',
                                           siding='single')
        desired_spectrum = np.array([1.118000149122749e-34,
                                     2*0.022942929484678257,
                                     2*0.20704159581664763,
                                     2*0.018317774296044642,
                                     2*0.007597511788147477,
                                     2*0.004508971439847654,
                                     2*0.0031729976902471545,
                                     2*0.0024827702154015855,
                                     2*0.0020984476697393016,
                                     2*0.0018876552893358684,
                                     2*0.0017933402731461997])
        assert_allclose(actual_spectrum, desired_spectrum, atol=1e-15)
        total_power = np.sum(desired_spectrum)
        assert_equal(total_power, 0.5436879879264717)

    def testPowerSpectrumSinewaveBoxcar(self):
        """
        Tests teh power spectrum of a sinewave with no hann window.

        """
        x = np.arange(-5, 5+0.5, 0.5)
        raw_data = np.sin(x)
        actual_spectrum = getPowerSpectrum(raw_data, filtering='box',
                                           siding='double')
        desired_spectrum = np.array([1.118000149122749e-34,
                                     0.022942929484678257,
                                     0.20704159581664763,
                                     0.018317774296044642,
                                     0.007597511788147477,
                                     0.004508971439847654,
                                     0.0031729976902471545,
                                     0.0024827702154015855,
                                     0.0020984476697393016,
                                     0.0018876552893358684,
                                     0.0017933402731461997,
                                     0.0017933402731461997,
                                     0.0018876552893358684,
                                     0.0020984476697393016,
                                     0.0024827702154015855,
                                     0.0031729976902471545,
                                     0.004508971439847654,
                                     0.007597511788147477,
                                     0.018317774296044642,
                                     0.20704159581664763,
                                     0.022942929484678257,
                                    ])
        assert_allclose(actual_spectrum, desired_spectrum, atol=1e-15)
        total_power = np.sum(desired_spectrum)
        assert_equal(total_power, 0.5436879879264715)

    def tearDown(self):
        pass # Tear down to be run after every test case

    @classmethod
    def tearDownClass(self):
        pass # Tear down to be run after entire script
