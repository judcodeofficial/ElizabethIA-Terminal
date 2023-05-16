from pydoc import doc
from tkinter import W
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import numpy
import tflearn
import tensorflow
import json
import random
import pickle
import os

# nltk.download('punkt')

# Create work folders
root_folder = 'ElizabethSpeech'
tmp_folder = root_folder + '/tmp'
if not os.path.exists(root_folder):
    os.makedirs(root_folder)

if not os.path.exists(tmp_folder):
    os.makedirs(tmp_folder)

with open('resources/elizabeth_speech_training.json', encoding='utf-8') as trainning_file:
    data = json.load(trainning_file)

try:
    with open(root_folder + '/vars.pickle', 'rb') as pickle_file:
        words, tags, trainning, output = pickle.load(pickle_file)
except Exception as ex:
    words = []
    tags = []
    aux1 = []
    aux2 = []

    for content in data['speech']:
        for pattern in content['patterns']:
            auxWord = nltk.word_tokenize(pattern)
            words.extend(auxWord)
            aux1.append(auxWord)
            aux2.append(content['tag'])

            if content['tag'] not in tags:
                tags.append(content['tag'])

    words = [stemmer.stem(w.lower()) for w in words if w != '?']
    words = sorted(list(set(words)))
    tags = sorted(tags)

    trainning = []
    output = []
    emptyOutput = [0 for _ in range(len(tags))]

    for x, document in enumerate(aux1):
        cubet = []
        auxWord = [stemmer.stem(w.lower()) for w in document]

        for w in words:
            if w in auxWord:
                cubet.append(1)
            else:
                cubet.append(0)

        outputRow = emptyOutput[:]
        outputRow[tags.index(aux2[x])] = 1
        trainning.append(cubet)
        output.append(outputRow)

    # Neural network
    trainning = numpy.array(trainning)
    output = numpy.array(output)

    with open(root_folder + '/vars.pickle', 'wb') as pickle_file:
        pickle.dump((words, tags, trainning, output), pickle_file)


    

network = tflearn.input_data(shape=[None,len(trainning[0])])
# Create hidden layers for process
network = tflearn.fully_connected(network, 100, activation='Relu')
network = tflearn.fully_connected(network, 100)
network = tflearn.fully_connected(network, 100, activation='Relu')
network = tflearn.fully_connected(network, 100)

network = tflearn.fully_connected(network, len(output[0]), activation="softmax")

network = tflearn.regression(network)

model = tflearn.DNN(network, tensorboard_dir=tmp_folder, best_checkpoint_path=root_folder)

if os.path.isfile('elispeech.tflearn.index'):
    model.load('elispeech.tflearn')
else:
    # DEBUG
    #model.fit(trainning, output, n_epoch=4000, batch_size=50, show_metric=True)
    model.fit(trainning, output, n_epoch=5000, batch_size=80, show_metric=False)
    model.save('elispeech.tflearn')

# def mainBot():
#     while True:
#         talk = input("Hablame: ")
#         cubet = [0 for _ in range(len(words))]
#         processInput = nltk.word_tokenize(talk)
#         processInput = [stemmer.stem(word.lower()) for word in processInput]
#         for each_word in processInput:
#             for i, word in enumerate(words):
#                 if word == each_word:
#                     cubet[i] = 1
        
#         results = model.predict([numpy.array(cubet)])
#         ind_results = numpy.argmax(results)
#         tag = tags[ind_results]

#         for tagAux in data['speech']:
#             if tagAux['tag'] == tag:
#                 response = tagAux['responses']
        
#         print("[+] TAG: " + tag)
#         print(results)

#         print("[+] ", random.choice(response))

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.lower(), b.lower())
    return s

def get_eli_response(speech):
    # Clean entry
    speech = normalize(speech)
    cubet = [0 for _ in range(len(words))]
    processInput = nltk.word_tokenize(speech)
    processInput = [stemmer.stem(word.lower()) for word in processInput]
    for each_word in processInput:
        for i, word in enumerate(words):
            if word == each_word:
                cubet[i] = 1
    
    results = model.predict([numpy.array(cubet)])
    ind_results = numpy.argmax(results)
    tag = tags[ind_results]

    for tagAux in data['speech']:
        if tagAux['tag'] == tag:
            response = tagAux['responses']
    
    random_response = random.choice(response)
    # response list
    eli_response = []
    # 1. TAG
    eli_response.append(tag)
    # 2. Random response
    eli_response.append(random_response)
    # 3. Array with probabilities
    eli_response.append(results)

    return eli_response