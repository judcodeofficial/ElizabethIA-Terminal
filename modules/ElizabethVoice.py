import pyttsx3
import requests
import time

class ElizabethVoice:
    eli_engine = pyttsx3.init()
    voice = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
    rate = 160

    def __init__(self):
        self.eli_engine.setProperty('voice', self.voice)
        self.eli_engine.setProperty('rate', self.rate)

    def eli_says(self, message):
        #time.sleep(0.32)
        self.eli_engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')
        self.eli_engine.setProperty('rate', self.rate)
        self.eli_engine.say(message)
        self.eli_engine.runAndWait()

    def get_voices(self):
        voices = self.eli_engine.getProperty('voices')

        for voice in voices:
            print(voice)