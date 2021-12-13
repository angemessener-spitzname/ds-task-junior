from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

import flask
from flask import Flask, jsonify, request 

idx_label = {
    0:"admiration",
    1:"amusement",
    2:"anger",
    3:"annoyance",
    4:"approval",
    5:"caring",
    6:"confusion",
    7:"curiosity",
    8:"desire",
    9:"disappointment",
    10:"disapproval",
    11:"disgust",
    12:"embarrassment",
    13:"excitement",
    14:"fear",
    15:"gratitude",
    16:"grief",
    17:"joy",
    18:"love",
    19:"nervousness",
    20:"optimism",
    21:"pride",
    22:"realization",
    23:"relief",
    24:"remorse",
    25:"sadness",
    26:"surprise",
    27:"neutral"
}

def emo_recognition(text: str) -> dict:
    tokenizer = AutoTokenizer.from_pretrained("poom-sci/bert-base-uncased-multi-emotion")
    model = AutoModelForSequenceClassification.from_pretrained("poom-sci/bert-base-uncased-multi-emotion")

    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)

    probs = softmax(output['logits'][0].detach().numpy())

    label_prob = {}

    for idx in idx_label.keys():
        label_prob[idx_label[idx]] = probs[idx]
        
    return label_prob    

app = Flask(__name__)

@app.route('/emotion-detection', methods=['POST'])
def infer_text():
   
    request_data = request.get_json()
    text = request_data['text']
    
    probs = emo_recognition(text)
    
    return '''
           Input text: {}
           Probabilities: {}
           '''.format(text, probs)


@app.route('/', methods=['GET'])
def index():
    return 'Multilabel Emotion Detection'
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')