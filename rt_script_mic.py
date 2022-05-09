#This module is responsible for handling the microphone functionality
#depending on the mode of operation chosen by the user. Functions
#include recording an audio clip for approximately 5 seconds to use
#in offline mode with the online mode intended to use the
#Speech Recognition API.

import sys
import time
from vosk import Model, KaldiRecognizer
import pyaudio
import rt_script_defs
import speech_recognition as sr
import json
import wave


from array import array
from sys import byteorder
from struct import pack

###################################################################################################################

#This function is used to record an audio clip using the PyAudio package.
#The format of the data being recieved is first established and then
#a stream is opened for the microphone to capture audio for approximately
#5 seconds. Afterwhich the stream is closed and then converted into a WAV file
#named 'Sample.wav' to be fed into the offline translation function.
def record():
    CHUNK = 8192
    RATE = 16000
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    
    capture = pyaudio.PyAudio()
    stream = capture.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)

    frames= []
    filename = 'sample.wav'

    duration = 9 #seconds

    for i in range(0,int(RATE/CHUNK*duration)):
        data = stream.read(4096)
        frames.append(data)

    clip = frames

    stream.stop_stream()
    stream.close()
    capture.terminate()

    waveFile = wave.open(filename, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(capture.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
############################################################################################################## 

#This function is used when the user chooses to operate in offline
#mode. It first calls the record() function to obtain a 5 second audio clip
#named Sample.wav. It then proceeds to load in the intended model from the source
#language variable provided by the user. Afterwhich the model is booted up and then
#passed into the recognizers' AcceptWaveform() function which reads and recognizes
#the audio passed into it and returns a string of the speech recieved.
def offline_mode_translation(source):


    record()

    wf = wave.open('sample.wav',"rb")

    transcript = []

    model = Model(source)

    r = KaldiRecognizer(model, 16000)


    while True:
            data = wf.readframes(4096)
            if len(data) == 0:
                break
            if r.AcceptWaveform(data):
                result_dict = json.loads(r.Result())

                transcript.append(result_dict.get("text",""))


    final = json.loads(r.FinalResult())
    transcript.append(final.get("text",""))

    transcript_txt = ' '.join(transcript)
    print(transcript_txt)
    return str(transcript_txt)

################################################################################################################

#This function is responsible for utilizing the Google API should the user choose
#to operate the device in online mode. After passing both the source and target language
#a few modules from the Google Cloud API is imported to create an instance which will 
#recognize the speech. This is done by using the microphone through the Speech Recognition
#module to create an instance that listens to the microphone until speech is not detected.
#Afterwhich the Google translate API takes in the results of the instance and returns the
#intended translation.
def online_translation_mode(source_lang, target_lang):
    
    import six
    from google.cloud import translate_v2 as translate
    translate_client = translate.Client()
    


    API_KEY = 'AIzaSyCh1U1--pgW4IY0njnOtKut-MjQZ3ej510'
    l_codes = rt_script_defs.lang_codes
    
    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    
    try:
        speech = str(r.recognize_google(audio,language=l_codes[source_lang]))
        print("\n\n")
        print("Recognized Text: "+speech)
        result = translate_client.translate(speech, target_language=target_lang)
        print(u"Translation: {}".format(result["translatedText"]))

    except sr.UnknownValueError:
        print("Couldn't understand audio")

    except sr.RequestError as e:
        print("Couldn't request results from service")

    

    return



    


#def check_if_wifi():
 #   return True
