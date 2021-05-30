# fetch_NLP

Run the main.py and login.html.
-- main.py consists of a script that reads the two texts from a form (login.html) as POST request and calls the measure_similarity.py


## measure_similarity 
Measure of Similarity -  Cosine similarity

## Preprocessing
* Removing punctuations
* Removing stopwords  (against a list siimilar to NLTK)
* Build a tokenizer (dictionary with indices for each words)
* Featurize_nonpos - Word count of each word (Ordering does not matter in this case) 
(Positional information is not taken since a gap of one word can affect subsequent positions)


