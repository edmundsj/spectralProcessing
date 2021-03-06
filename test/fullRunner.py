"""
Run all the core unit tests, not the lengthy and major integration tests
"""
print("RUNNING ALL UNIT TESTS ---------")
import unittest
import sys
import context
sys.path.append('test') # Allows this runner to be run from the main directory

import test_spectral_power
import test_units

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromModule(test_spectral_power))
suite.addTests(loader.loadTestsFromModule(test_units))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

numberFailures = len(result.errors)
numberErrors= len(result.failures)
numberIssues = numberFailures + numberErrors

sys.exit(numberIssues)
