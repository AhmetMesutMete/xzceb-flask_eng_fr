'''
Translator Module
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')

def english_to_french(english_text):
    '''
    This function takes english text as an input and returns 
    its translation to french as text
    '''
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    # frenchText = json.dumps(translation, indent=2, ensure_ascii=False)
    return french_text

def french_to_english(french_text):
    '''
    This function takes french text as an input and returns 
    its translation to english as text
    '''
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    # englishText = json.dumps(translation, indent=2, ensure_ascii=False)
    return english_text
