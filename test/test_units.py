import context
import unittest
import numpy as np
import pandas as pd
from numpy.testing import assert_equal, assert_allclose
from spectral_processing import extractSamplingPeriod
from pint import UnitRegistry

class TestUnits(unittest.TestCase):
    def setUp(self):
        pass # Set up to be run before every test case

    @classmethod
    def setUpClass(cls):
        cls.ureg = UnitRegistry()

    def testExtractUnits(self):
        data = pd.DataFrame({'Time (ms)': [0, 0.1, 0.2, 0.3, 0.4],
                             'Values': [0, 1, 2, 3, 4]})
        actual_unit = extractSamplingPeriod(data)
        desired_unit = self.ureg.ms * 0.1
        assert actual_unit == desired_unit

    def tearDown(self):
        pass # Tear down to be run after every test case

    @classmethod
    def tearDownClass(self):
        pass # Tear down to be run after entire script
