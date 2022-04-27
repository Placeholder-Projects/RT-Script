from argostranslate import package, translate
import os

path = os.getcwd()

package.install_from_path(path+'/en_es.argosmodel')
package.install_from_path(path+'/es_en.argosmodel')
package.install_from_path(path+'/en_fa.argosmodel')
package.install_from_path(path+'/fa_en.argosmodel')


installed_languages = translate.get_installed_languages()
#print(installed_languages)

#Language Dictionary is as follows: English[0], Farsi[1], Spanish[2]

#English to Farsi
en_fa = installed_languages[0].get_translation(installed_languages[1])

#English to Spanish
en_es = installed_languages[0].get_translation(installed_languages[2])

#Spanish  to English
es_en = installed_languages[2].get_translation(installed_languages[0])

#Farsi to English
fa_en = installed_languages[1].get_translation(installed_languages[2])


#English Proxy
def en_proxy(source_lang, target_lang, speech_2_txt):
    
    #Spanish to Farsi
    if(source_lang == 'es' and target_lang == 'fa'):
        eng = translate_es_en(speech_2_txt)

        return translate_en_fa(eng)

    #Farsi to Spanish
    if(source_lang == 'fa' and target_lang == 'es'):
        eng = translate_fa_en(speech_2_txt)
        
        return translate_en_es(eng)

    else:
        pass

#Translation Functions

def translate_en_fa(speech_2_txt):

    return en_fa.translate(speech_2_txt)

def translate_es_en(speech_2_txt):

    return es_en.translate(speech_2_txt)

def translate_fa_en(speech_2_txt):

    return fa_en.translate(speech_2_txt)

def translate_en_es(speech_2_txt):

    return en_es.translate(speech_2_txt)
    