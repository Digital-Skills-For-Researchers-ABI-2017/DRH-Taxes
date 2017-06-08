import unittest
import inspect

from drhtaxes import application

class ApplicationTests(unittest.TestCase):
    
    def test_application(self):
        self.assertTrue(inspect.ismodule(application))

    
if __name__ == '__main__':
    unittest.main()

