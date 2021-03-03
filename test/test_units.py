import context
import unittest
import numpy as np
import pandas as pd
from numpy.testing import assert_equal, assert_allclose
from spectral_processing import extractSamplingPeriod, extractUnit
from pint import UnitRegistry

class TestUnits(unittest.TestCase):
    def setUp(self):
        pass # Set up to be run before every test case

    @classmethod
    def setUpClass(cls):
        cls.ureg = UnitRegistry()

    def testExtractSamplingPeriod(self):
        data = pd.DataFrame({'Time (ms)': [0, 0.1, 0.2, 0.3, 0.4],
                             'Values': [0, 1, 2, 3, 4]})
        actual_period = extractSamplingPeriod(data)
        desired_period = self.ureg.ms * 0.1
        assert actual_period == desired_period

    def testExtractTimeUnits(self):
        unit_string = 'Time (s)'
        desired_unit = 1 * self.ureg.s
        actual_unit = extractUnit(unit_string)
        assert desired_unit == actual_unit

        unit_string = 'time (ms)'
        desired_unit = 1 * self.ureg.ms
        actual_unit = extractUnit(unit_string)
        assert desired_unit == actual_unit

        unit_string = 'Time (us)'
        desired_unit = 1 * self.ureg.us
        actual_unit = extractUnit(unit_string)
        assert desired_unit == actual_unit

        unit_string = 'Time (ns)'
        desired_unit = 1 * self.ureg.ns
        actual_unit = extractUnit(unit_string)
        assert desired_unit == actual_unit

        unit_string = 'Time (ps)'
        desired_unit = 1 * self.ureg.ps
        actual_unit = extractUnit(unit_string)
        assert desired_unit == actual_unit

    def testExtractElectricalUnits(self):
        unit_string = 'Photocurrent (pA)'
        desired_unit = 1 * self.ureg.pA
        actual_unit = extractUnit(unit_string)
        assert desired_unit == actual_unit

        unit_string = 'Photocurrent (nA)'
        desired_unit = 1 * self.ureg.nA
        actual_unit = extractUnit(unit_string)
        assert desired_unit == actual_unit

        unit_string = 'Current (uA)'
        desired_unit = 1 * self.ureg.uA
        actual_unit = extractUnit(unit_string)
        assert desired_unit == actual_unit

        unit_string = 'Jordans (mA)'
        desired_unit = 1 * self.ureg.mA
        actual_unit = extractUnit(unit_string)
        assert desired_unit == actual_unit

        unit_string = 'More Current (A)'
        desired_unit = 1 * self.ureg.A
        actual_unit = extractUnit(unit_string)
        assert desired_unit == actual_unit

        unit_string = 'Photovoltage (V)'
        desired_unit = 1 * self.ureg.V
        actual_unit = extractUnit(unit_string)
        assert desired_unit == actual_unit

        unit_string = 'Photovoltage (mV)'
        desired_unit = 1 * self.ureg.mV
        actual_unit = extractUnit(unit_string)
        assert desired_unit == actual_unit

        unit_string = 'Photovoltage (uV)'
        desired_unit = 1 * self.ureg.uV
        actual_unit = extractUnit(unit_string)
        assert desired_unit == actual_unit

        unit_string = 'Photovoltage (nV)'
        desired_unit = 1 * self.ureg.nV
        actual_unit = extractUnit(unit_string)
        assert desired_unit == actual_unit

    def tearDown(self):
        pass # Tear down to be run after every test case

    @classmethod
    def tearDownClass(self):
        pass # Tear down to be run after entire script
