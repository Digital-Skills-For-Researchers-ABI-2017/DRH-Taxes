import unittest
import inspect
import sys

from drhtaxes.admission import tax_input_checker
from drhtaxes import admission

class InputCheckerTests(unittest.TestCase):

    def test_float(self):
        self.assertTrue(tax_input_checker('9.000'))

    def test_bad_float(self):
        self.assertFalse(tax_input_checker('9..00'))

class AdmissionTests(unittest.TestCase):

    def test_admission_three_inputs(self):
        sys.argv = ['koala', '12435','44225','4643356']
        with self.assertRaises(SystemExit) as cm:
            admission.admission()
            self.assertEqual('Error Code: PANDA',cm.exception)

    def test_admission_one_input(self):
        sys.argv = ['koala', '12435']
        with self.assertRaises(SystemExit) as cm:
            admission.admission()
            self.assertEqual('Error Code: PANDA',cm.exception)
            
    def test_admission_incorrect_income_double_floating_point(self):
        sys.argv = ['koala', '1243..05','44225']
        with self.assertRaises(SystemExit) as cm:
            admission.admission()
            self.assertEqual('Error Code: HUGH',cm.exception)
            
    def test_admission_incorrect_income_leading_letter_character(self):
        sys.argv = ['koala', 'f124.05','44225']
        with self.assertRaises(SystemExit) as cm:
            admission.admission()
            self.assertEqual('Error Code: HUGH',cm.exception)
            
    def test_admission_incorrect_losses_trailing_letter_character(self):
        sys.argv = ['koala', '12435','7825.s8']
        with self.assertRaises(SystemExit) as cm:
            admission.admission()
            self.assertEqual('Error Code: JELLYBEAN',cm.exception)
        
        
    
if __name__ == '__main__':
    unittest.main()

