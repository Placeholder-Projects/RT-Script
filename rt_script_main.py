#!/usr/bin/env python3

"""
RT Script
############################################################

This is the main file for the RT Script project. This file is meant to encapsulate all of the other header files that 
will help with the ability to translate in real-time. The goal of the main file is to connect all of the header files
which include the speech recognizer, translator, speech-to-text, and data transfer to the peripherals for the camera
and touchscreen on the Jetson Nano. In its current state the user will input the source languge, target language and
method of operation for the device (online/offline) and await the results of the desired speech. Languages are provi-
ded in ISO 639-1 format. https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes


Note: Current processing time takes around 3-6 seconds depending if Argos and Vosk has been booted up.
"""

import sys
import os
import rt_script_defs
import rt_script_mic
import rt_script_translator_models
import argostranslate


if __name__== "__main__":

#Error checking for arguments provided numbering below or above 4.
    if(len(sys.argv) < 4):
        print("Not enough commands to run. Try [python3 rt_script_main.py [source_language] [target_language] [offline/online]")
        exit

    if(len(sys.argv) > 4):
        print("Too many arguments. Try python3 rt_script_main.py [source_language] [target_language] [offline/online]")

    
#Give user provided arguments their appropriate name and variable for the functions to use.   
    source_lang = sys.argv[1]

    target_lang = sys.argv[2]

    device_mode = sys.argv[3]

    lang_dictionary = rt_script_defs.lang_dict

    cwd = os.getcwd()

    mic = rt_script_mic

    tran = rt_script_translator_models

#Waits for the user to input the command "listen" in order to begin recording or recognizing speech.
    command = input('Type [listen] to begin recording audio\n')

    if(command != 'listen'):
        while command != 'listen':
            command = input('Type [listen] to begin recording audio\n')

  
#If method of operation chosen is offline then depending on the languages chosen
#the corresponding functions will be used from rt_script_mic and rt_script_translator_models
#are used.
    if(device_mode == 'offline'):
        print("We're offline!")
        result = mic.offline_mode_translation(cwd+lang_dictionary[source_lang])

        #For Proxy function when neither languages are English
        if(source_lang != 'en' and target_lang != 'en'):
            print(tran.en_proxy(source_lang,target_lang,result))

        if(source_lang == 'es' and target_lang == 'en'):
            print(tran.translate_es_en(result))

        if(source_lang == 'en' and target_lang == 'es'):
            print(tran.translate_en_es(result))

        if(source_lang == 'fa' and target_lang == 'en'):
            print(tran.translate_fa_en(result))

        if(source_lang == 'en' and target_lang == 'fa'):
            print(tran.translate_en_fa(result))

#Used if method of operation is chosen to be online.
    if(device_mode == 'online'):
        print("We're online!")
        mic.online_translation_mode(source_lang,target_lang)

    else:
        pass
    