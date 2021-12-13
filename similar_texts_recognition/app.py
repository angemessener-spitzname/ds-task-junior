import re
import numpy as np
from numpy import array
from scipy import spatial
from scipy.spatial import distance
from collections import Counter

import nltk
from nltk.corpus import stopwords

import flask
from flask import Flask, jsonify, request 

def words_extraction(text: str) -> list:
    words = re.sub("[^\w]", " ",  text).split()    
    stop_words = set(stopwords.words('english'))
    filtered_words = [w.lower() for w in words if w.lower() not in stop_words]    
    return filtered_words

def similar_texts_recognition(txt_1: str, txt_2: str) -> np.float64:
    text_1 = words_extraction(txt_1)
    text_2 = words_extraction(txt_2)
    
    vocabulary = set(text_1 + text_2)
    
    cntr_text_1 = Counter(text_1)
    cntr_text_2 = Counter(text_2)
    
    text_freq = np.zeros([2, len(vocabulary)])

    i = -1
    for word in sorted(vocabulary):
        i += 1
        text_freq[0][i] = cntr_text_1[word]
        text_freq[1][i] = cntr_text_2[word]
        
    return distance.cosine(text_freq[0,:], text_freq[1,:])

app = Flask(__name__)

@app.route('/similar-recognition', methods=['POST'])
def infer_text():
   
    request_data = request.get_json()
    text_1 = request_data['text_1']
    text_2 = request_data['text_2']  
    
    similarity = similar_texts_recognition(text_1, text_2)
    
    return '''
           Cosine similarity is: {}
           '''.format(similarity)


@app.route('/', methods=['GET'])
def index():
    return 'Similar Texts Recognition'
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')