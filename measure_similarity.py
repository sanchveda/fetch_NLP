import numpy as np

stop_words =['i','me','my','myself','we','our','ours','ourselves','you','your','yours',\
             'yourself','yourselves','he','him','his','himself','she','her','hers','herself',\
             'it','its','itself','they','them','their','theirs','themselves','what','which',\
             'who','whom','this','that','these','those','am','is','are','was','were','be','been','being',\
             'have','has','had','having','do','does','did','doing','a','an','the','and','but',\
             'if','or','because','as','until','while','of','at','by','for','with','about',\
             'against','between','into','through','during','before','after','above',\
             'below','to','from','up','down','in','out','on','off','over','under','again',\
             'further','then','once','here','there','when','where','why','how','all','any'\
             'both','each','few','more','most','other','some','such','no','nor','not','only',\
             'own','same','so','than','too','very','s','t','can','will','just','don','should','now'
]

tokens  = {}


# Remove punctuations. Pre-processing step
def remove_punctuation(s):
    for x in s:
        if x in '''!()-[]{};:'"\,<>./?@#$%^&*_~''':
            s = s.replace(x, '')

    return s


# Stop words are listed above. Preprocessing step
def remove_stop_words(s):
    new_str = []
    for x in s.split(' '):
        if x not in stop_words:
            new_str.append(x)

    return ' '.join(new_str)

# A simple tokenizer
def build_tokenize (s):

  for sentence in s :

    for idx, word in enumerate(sentence.split(' ')):
      if word not in tokens:
        tokens[word] = idx+1


# Non Positional features of the vocabulary
def featurize_nonpos(s):
    feat = np.zeros(len(tokens))
    words = s.split(' ')
    for idx, x in enumerate(tokens.keys()):
        if x in words:
            feat[idx] = feat[idx]+1

    return feat


# Positional features of the vocabulary
def featurize(s):
    feat = np.zeros(len(tokens))
    words = s.split(' ')
    for idx, x in enumerate(tokens.keys()):
        if x in words:
            feat[idx] = words.index(x)

    return feat

# Cosine similarity function
def cosine_similarity(vec1, vec2):

  dot = np.dot (vec1, vec2)

  norm1 = np.sqrt (np.sum(vec1**2))
  norm2 = np.sqrt (np.sum(vec2**2))

  sim = dot / (norm1 * norm2)

  return sim

# Inputt = Two strings. Output = Similarity score
def similarity (s1, s2):

  s1 = s1.lower()
  s2 = s2.lower()

  s1=remove_punctuation(s1)
  s1=remove_stop_words (s1)

  s2=remove_punctuation(s2)
  s2=remove_stop_words (s2)

  build_tokenize([s1,s2])

  s1 = featurize_nonpos(s1)
  s2 = featurize_nonpos (s2)

  return cosine_similarity (s1, s2)




#Lines to execute.  Uncomment for executing the samples
s1 = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."

s2 = "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."

s3 = "We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."
print (similarity(s1, s2))
print (similarity(s1, s3))
