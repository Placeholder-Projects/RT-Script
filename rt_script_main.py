#!/usr/bin/env python3

"""
RT Script
############################################################

This is the main file for the RT Script project. This file is meant to encapsulate all of the other header files that 
will help with the ability to translate in real-time. The goal of the main file is to connect all of the header files
which include the speech recognizer, translator, speech-to-text, and data transfer to the peripherals for the camera
and touchscreen on the Jetson Nano.
"""

import sys
import os
import rt_script_defs
import rt_script_mic
import rt_script_translator_models
import argostranslate


if __name__== "__main__":

    if(len(sys.argv) < 4):
        print("Not enough commands to run. Try [python3 rt_script_main.py [source_language] [target_language] [offline/online]")
        exit

    if(len(sys.argv) > 4):
        print("Too many arguments. Try python3 rt_script_main.py [source_language] [target_language] [offline/online]")

    
    
    source_lang = sys.argv[1]

    target_lang = sys.argv[2]

    device_mode = sys.argv[3]

    lang_dictionary = rt_script_defs.lang_dict

    cwd = os.getcwd()

    mic = rt_script_mic

    translate = rt_script_translator_models

    command = input('Type [listen] to begin recording audio\n')

    if(command != 'listen'):
        while command != 'listen':
            command = input('Type [listen] to begin recording audio\n')

    #audio = rt_script_mic.listen_record()

    if(device_mode == 'offline'):
        result = mic.offline_mode_translation(cwd+lang_dictionary[source_lang])

        #For Proxy function when neither languages are English
        if(source_lang != 'en' and target_lang != 'en'):
            print(translate.en_proxy(source_lang,target_lang,result))

        if(source_lang == 'es' and target_lang == 'en'):
            print(translate.es_en(result))

        if(source_lang == 'en' and target_lang == 'es'):
            print(translate.en_es(result))

        if(source_lang == 'fa' and target_lang == 'en'):
            print(translate.fa_en(result))

        if(source_lang == 'en' and target_lang == 'fa'):
            print(translate.en_fa(result))

    #For Online Mode (To Be Included Later)
    else:
        pass