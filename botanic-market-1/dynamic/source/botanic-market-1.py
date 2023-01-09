# chatSNN bot
import functools
import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

intents = json.loads(open('./chatsnn-model/intents.json').read())
words = pickle.load(open('./chatsnn-model/words.pkl', 'rb'))
classes = pickle.load(open('./chatsnn-model/classes.pkl', 'rb'))
model = load_model('./chatsnn-model/model.h5')
lemmatizer = WordNetLemmatizer()

# Read flag into variable
file = open("flag.txt",'r')
FLAG = file.read()
file.close()

# Cleans user input
def cleanSentence(sentence):
    sentenceWords= nltk.word_tokenize(sentence)
    sentenceWords = [lemmatizer.lemmatize(token) for token in sentenceWords]
    return sentenceWords

# Get bag of words
def bagOfWords(sentence):
    sentenceWords = cleanSentence(sentence)
    bag = [0] * len(words)
    for word in sentenceWords:
        for i, token in enumerate(words):
            if token == word:
                bag[i] = 1
    return np.array(bag)

# Predict class
@functools.lru_cache(maxsize=4096)
def predictClass(sentence):
    bow = bagOfWords(sentence)
    res = model(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str (r[1])})
    return return_list

# Get response from intents
def getResponse(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

# Get response from chatbot model
def chatbotResponse(message):
    ints = predictClass(message)
    res = getResponse(ints, intents)
    if res == "FLAG":
        res = FLAG
    return res

# Flask app
from flask import Flask, request

app = Flask(__name__)

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')

    if userText is None:
        return "Missing 'msg' parameter", 400
    elif len(userText) > 255:
        return "Message too long", 400

    return chatbotResponse(userText)

if __name__ == "__main__":
    app.run(port=1337, host="0.0.0.0")
