<h1>Junior Data Scientist Tasks</h1>

<h2>3. similar-texts-recognition </h2>

<h3>Contents: </h3>
1. Matching algorithm <br>
2. Rest API<br>
3. Result<br>

<h3>Matching algorithm</h3>
For this challenge I use Bag-of-Words technique to extract words from sentences and add the extracted words into an array. The code takes into account the presence of not significant common words (such as “the”, “a”, “an”, “in”) and ignores them. In this way I create the vocabulary of both text's words. Then I count how frequently the vocabulary words appear in each text and create two vectors containing the count of word occurrences in the texts. The last thing left to do is to calculate the cosine similarity between this vectors with Scipy library. The closer the result value to 0, the greater the match between vectors.
<h3>Rest API</h3>
In this project i use Flask framework and Postman agent. With /similar-recognition root and POST method I load json files that contain two texts and receive cosine similarity value.
<h3>Result</h3>
I tested two excerpts from the article about cats and got the result: 

![](https://sun9-41.userapi.com/impg/EorLkSqQZgGNi4IvBSzBM1jGtzOuAnfVSsxNXw/Caxg2Cmo1ZA.jpg?size=1792x537&quality=96&sign=58e9ed026a14e8ee97e02e732b8cce7b&type=album)


The result for texts about BERT model and cats:

![](https://sun9-52.userapi.com/impg/HuG3I_2Oi6vBSmmowQoKCE0fEuAee07nQI4RFw/Mp0RJOkQjoo.jpg?size=1790x542&quality=96&sign=431e423b8125f50191fe15d3ed538825&type=album)




<h2>1. emotion-detection </h2>

<h3>Contents: </h3>
1. Bert based model <br>
2. Rest API<br>
3. Result<br>

<h3>Bert based model</h3>
For this task i found appropriate trained model : 

[bert-base-uncased-multi-emotion](https://huggingface.co/poom-sci/bert-base-uncased-multi-emotion?text=I+like+you.+I+love+you)

The author left no descriptions, so I tried to figure it out on my own.
As I found out, this model builds on BERT’s language masking strategy and was trained on go-emotions dataset. Dataset labelled 58000 Reddit comments with 28 emotions: admiration, amusement, anger, annoyance, approval, caring, confusion, curiosity, desire, disappointment, disapproval, disgust, embarrassment, excitement, fear, gratitude, grief, joy, love, nervousness, optimism, pride, realization, relief, remorse, sadness, surprise + neutral.
I just loaded the model and processed the output with softmax function from Scipy library to get the probability distributions. Then I matched the outcomes with labels I found in [config.json file](https://huggingface.co/poom-sci/bert-base-uncased-multi-emotion/blob/main/config.json) 

<h3>Rest API</h3>
I also used Flask framework and Postman agent. With /emotion-detection root and POST method I loaded json files that contain sentence for input and received probabilities.

<h3>Result</h3>

Text: "Omg you cooked such delicious cupcakes!"<br>
Answer: Admiration

![Omg you cooked such delicious cupcakes!](https://sun1-15.userapi.com/impg/FF0s8xPJt8YTvn59rn4OvH1Bu_NHbdGZpK-Y1g/3okXSe6Vuwk.jpg?size=1773x668&quality=96&sign=d2a4dbb720e91a1e97179827f514e21b&type=album)


Text: "How dare you?" <br> Answer: Anger

![](https://sun9-44.userapi.com/impg/PjG0bMMhNxtE_CVxywwft1_QnVxWO-ECNYu4kw/uGzOw-gyxJE.jpg?size=1795x673&quality=96&sign=fa00fa99143da419d2a34cb92c28b227&type=album)







