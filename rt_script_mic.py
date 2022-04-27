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

def record():
    capture = pyaudio.PyAudio()
    stream = capture.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=8192)
    print('Recording...')
 
    # Initialize array that be used for storing frames
    frames = [] 
    
    # Store data in chunks for 8 seconds
    for i in range(0, int(16000 / 4096 * 5)):
        data = stream.read(4096)
        frames.append(data)
    
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    
    # Terminate - PortAudio interface
    capture.terminate()

    return frames
    """
    print('Done !!! ')
    filename = "sample.wav"
    # Save the recorded data in a .wav format
    sf = wave.open(filename, 'wb')
    sf.setnchannels(1)
    sf.setsampwidth(capture.get_sample_size(pyaudio.paInt16))
    sf.setframerate(16000)
    sf.writeframes(b''.join(frames))
    sf.close()
    """

    

def offline_mode_translation(source):

    #lang_path = rt_script_defs.lang_dist

    model = Model(source)

    r = KaldiRecognizer(model, 16000)


    capture = pyaudio.PyAudio()
    #stream = capture.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=8192)

    data = record()

    #stream.start_stream()

    #while True:
    #while stream.is_active():
    #    time.sleep(5)


    #stream.stop_stream()

    #data = stream.read(4096)
    """if len(data) == 0:
        pass

    elif r.AcceptWaveform(data):
        print(r.Result())
    """  
    r.AcceptWaveform(data)    
    return r.Result()


