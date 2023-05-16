import speech_recognition as sr
import pyaudio
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
    print(voice)

print(engine.getProperty('rate'))

engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')
engine.setProperty('rate', '95')
engine.say("...")
engine.say("...")

def holi():
    print("Hi snowboy")

try:
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)

        engine.say("")
        engine.runAndWait()

        print("A la orden sr...")
        voice = listener.listen(source)

        rec = listener.recognize_sphinx(voice, language="es-MX")

        print(rec)
except Exception as ex:
    print("Error...")
    print(ex)