#This module is meant to contain some necessary and potentially necessary
#definitions of the properly named languge models for both VOSK and ArgosTranslate
#API through the use of dictionaries.

#Dictionary for the language recognition models aptly named according to 
#ISO 639-1 language codes to match user input.
lang_dict = {"en": '/en', 
             "es": '/es', 
             "fa": '/fa', 
             "tl": '/tl'}


#Language Abbreviations dictionary for future display of current languages being
#used for both source and target.
lang_abbrev = {'en' : 'English',
               'es' : 'Spanish',
               'fa' : 'Farsi',
               'tl' : 'Tagalog'}

#Dictionary containing language codes for online translation API
lang_codes = {'en' : "en-US",
              'es' : "es-US",
              'fa' : "fa-IR",
              'tl' : "fil-PH"}
