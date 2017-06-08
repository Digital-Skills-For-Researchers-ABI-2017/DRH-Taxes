##from source.output import tax_compare
##corp=1000;
##tax=900;

import unittest

from drhtaxes import application
from drhtaxes.output import tax_compare

class ApplicationTests(unittest.TestCase):
    
    def test_tax_compare_runs(self):
        corp = 1000
        tax = 900
        msg = tax_compare(corp, tax)
        
        self.assertTrue(len(msg) > 0)

    def test_tax_compare_high_corp(self):
        corp = 40000
        tax = 22000

        msg = tax_compare(corp, tax)

        self.assertEqual('Individual tax rate is the best method as the taxable income would be reduced by NZD 18000', msg)

    def test_tax_compare_high_corp(self):
        tax = 40000
        corp = 22000

        msg = tax_compare(corp, tax)

        self.assertEqual('Corporate tax rate is the best method as the taxable income would be reduced by NZD 18000', msg)

    def test_tax_compare_equal(self):
        corp = 40000
        tax = 40000

        msg = tax_compare(corp, tax)

        self.assertEqual('Choose either filing a income tax return as a corporate or as an individual', msg)


if __name__ == '__main__':
    unittest.main()

    
