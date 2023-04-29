'''
This is a test module
'''
import unittest
from ..translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    '''
    This is a test class for translator.py 
    '''
    def test_e2f(self):
        '''
        This is a function to test english_to_french function
        '''
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertIsNone(english_to_french(None))

    def test_f2e(self):
        '''
        This is a function to test french_to_english function
        '''
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertIsNone(french_to_english(None))

if __name__ == "__main__":
    unittest.main()
