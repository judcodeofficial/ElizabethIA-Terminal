from modules.ElizabethVoice import ElizabethVoice
from modules.ElizabethSpeechRecognition import ElizabethSpeechRecognition
import modules.ElizabethTrain as et
import pocketsphinx
import speech_recognition as sr
import modules.Constants as const
from modules.ElizabethCore import ElizabethCore
import numpy as np

esr = ElizabethSpeechRecognition()
esr.EliSpeak.eli_says("Neural matrix loaded...")
# Init speech recognition
esr.EliSpeak.eli_says("Starting speech recognition...")

ecore = ElizabethCore()

listener = sr.Recognizer()
listener.pause_threshold = 1

def process_speech(speech):
    print("[+] Processing speech...")
    # Pass througt neural network
    processed_speech = et.get_eli_response(speech)

    eli_tag = processed_speech[0]
    eli_response = processed_speech[1]
    probabilities = processed_speech[2][0]
    prob_list = [float(num) * 100 for num in probabilities]
    max_prob = np.max(prob_list)

    is_command_tag = eli_tag in const.command_tags

    # First. validate if probabilities > min_predict
    if max_prob > const.min_predict and not is_command_tag:
        print("[+] Speaking...")
        esr.EliSpeak.eli_says(eli_response)
    elif is_command_tag:
        # Second. Validate if its command
        print("[+] Processing command...")
        ecore.execute_command(eli_tag, speech)
    else:
        # TODO: Save in BD to add in neural network JSON
        print("[+] NEW ONE TO BE SAVED: " + speech)

while True:
    if esr.check_connection:
        try:
            with sr.Microphone() as source:
                listener.adjust_for_ambient_noise(source)
                voice = listener.listen(source)
                rec = listener.recognize_google(voice, language="es-ES")

                print("[+] You said: " + rec)

                # Process speech
                process_speech(rec)
        except Exception as ex:
            # TODO: colocar aqui codigo para reconocer offline
            print("Error...")
            print(ex)
    else:
        speech = pocketsphinx.LiveSpeech(
            verbose=False,
            sampling_rate=16000,
            buffer_size=2048,
            no_search=False,
            full_utt=False,
            remove_noise=True,
            hmm=const.var_hmm,
            lm=const.var_lm,
            dic=const.var_dic
        )

        for phrase in speech:
            process_speech(phrase)