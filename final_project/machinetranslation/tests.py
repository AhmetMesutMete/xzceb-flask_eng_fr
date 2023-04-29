'''
Test module
'''
import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    '''
    Test class for translator.py 
    '''
    def test_e2f(self):
        '''
        This is a function to test english_to_french function
        '''
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french('   '),'')

    def test_f2e(self):
        '''
        This is a function to test french_to_english function
        '''
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english('   '),'')

if __name__ == "__main__":
    unittest.main()
