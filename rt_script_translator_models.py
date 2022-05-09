#This module is responsible for housing all of the functions that translate
#the text acquired from the speech-to-text portion of the project using 
#the ArgosTranslate API which is a package that requires the installation
#of several models

from argostranslate import package, translate
import os

#Set variable to current working directory
path = os.getcwd()

#Install packages for argostranslate with the path directory
package.install_from_path(path+'/en_es.argosmodel')
package.install_from_path(path+'/es_en.argosmodel')
package.install_from_path(path+'/en_fa.argosmodel')
package.install_from_path(path+'/fa_en.argosmodel')

#######################################################################################################

#Returns a dictionary of the language packages installed
installed_languages = translate.get_installed_languages()


#Language Dictionary is as follows: English[0], Farsi[1], Spanish[2]


#The following functions returns a translation given the corresponding language package installed

#English to Farsi
en_fa = installed_languages[0].get_translation(installed_languages[1])

#English to Spanish
en_es = installed_languages[0].get_translation(installed_languages[2])

#Spanish  to English
es_en = installed_languages[2].get_translation(installed_languages[0])

#Farsi to English
fa_en = installed_languages[1].get_translation(installed_languages[2])
################################################################################################################

#This section focuses on functions that return the corresponding translation
#given the source language and target language
################################################################################################################

#English Proxy function that triggers if either source or target languages
#are not English. Translate the desired speech results to another languge
#besides English.

def en_proxy(source_lang, target_lang, speech_2_txt):
    
    #Spanish to Farsi
    if(source_lang == 'es' and target_lang == 'fa'):
        eng = translate_es_en(speech_2_txt)

        translate_en_fa(eng)
        

    #Farsi to Spanish
    if(source_lang == 'fa' and target_lang == 'es'):
        eng = translate_fa_en(speech_2_txt)
        
        translate_en_es(eng)
        

    else:
        pass

#Translation Functions
#These functions are used to return translations
#in their respective languages that involve English

def translate_en_fa(speech_2_txt):

    return en_fa.translate(speech_2_txt)
    

def translate_es_en(speech_2_txt):

    return es_en.translate(speech_2_txt)
    


def translate_fa_en(speech_2_txt):

    return fa_en.translate(speech_2_txt)
    

def translate_en_es(speech_2_txt):

    return en_es.translate(speech_2_txt)
    
    