import pocketsphinx
from modules.ElizabethVoice import ElizabethVoice
import requests
import pocketsphinx
import speech_recognition as sr

class ElizabethSpeechRecognition():
    EliSpeak = ElizabethVoice()
    def __init__(self):
        self.EliSpeak.eli_says("Sistemas de voz cargados...")
        self.EliSpeak.eli_says("Cargando reconocimiento de voz...")

        # Offline vars
        self.model_path = pocketsphinx.get_model_path()
        self.var_hmm = 'model\\es-mx'
        self.var_lm = 'model\\es-mx\\es-mx.lm.bin'
        self.var_dic = 'model\\es-mx\\cmudict-es-mx.dict'

        if self.check_connection:
            self.EliSpeak.eli_says("Red estable y con conexión...")
        else:
            self.EliSpeak.eli_says("No se encontró conexión, levantando sistemas locales...")

    
    def init_eli_speech_recognition(self):
        self.EliSpeak.eli_says("Iniciando reconocimiento de voz...")
        while True:
            if self.check_connection:
                self.sr_online
            else:
                self.sr_offline
    
    def check_connection(self):
        try:
            req = requests.get('https://www.google.com/', timeout=1)
            req.raise_for_status()
            return True
        except Exception as ex:
            return False