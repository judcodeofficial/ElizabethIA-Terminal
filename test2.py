import os
import pocketsphinx
#from pocketsphinx import LiveSpeech, get_model_path

model_path = pocketsphinx.get_model_path()

print(model_path)

var_hmm = 'model\\es-mx'
var_lm = 'model\\es-mx\\es-mx.lm.bin'
var_dic = 'model\\es-mx\\cmudict-es-mx.dict'

speech = pocketsphinx.LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    remove_noise=True,
    hmm=var_hmm,
    lm=var_lm,
    dic=var_dic
)

print(speech.audio_device)

for phrase in speech:
    print(phrase)
    print(speech.confidence() * 100)