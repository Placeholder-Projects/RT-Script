#!/usr/bin/env python3

"""
RT Script
############################################################

This is the main file for the RT Script project. This file is meant to encapsulate all of the other header files that 
will help with the ability to translate in real-time. The goal of the main file is to connect all of the header files
which include the speech recognizer, translator, speech-to-text, and data transfer to the peripherals for the camera
and touchscreen on the Jetson Nano.
"""

import speech_recognition as sr
import time
from translate import Translator


from os import path

recognize = sr.Recognizer()
with sr.Microphone() as mic:

#Detect Audio
    print("Testing Audio Detection: ")
    sound = recognize.listen(mic)

try:
    print("Captured Transcript: " + recognize.recognize_sphinx(sound) + " Detection Test Passed")

except sr.UnknownValueError:
    print("Error Detecting Voice!")

except sr.RequestError as err:
        print("API Error; {0}".format(err))


#Background Listening

#Caption Audio

#Translation