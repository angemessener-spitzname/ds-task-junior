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












