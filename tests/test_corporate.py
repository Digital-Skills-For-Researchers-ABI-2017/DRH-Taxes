import unittest
import inspect

from drhtaxes import corporate
from drhtaxes.corporate import COR


class ApplicationTests(unittest.TestCase):
    """
    Testing class_COR
    """
    
    def test_class_COR(self):
        """
        Testing function_corp
        """
        tax = COR()
        self.assertEqual(15800, tax.corp(79000, 0))
        self.assertEqual(16980, tax.corp(85000,100))
        self.assertEqual(400, tax.corp(2000,0))
        self.assertEqual(19000, tax.corp(100000,5000))
        self.assertEqual(8000, tax.corp(40000,0))

if __name__ == '__main__':
    unittest.main()

