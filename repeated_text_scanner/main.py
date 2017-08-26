import nltk
import string
from nltk.util import ngrams


f = open('bhetest.txt', 'r')
a = f.read()
f.close()

exclude = set(string.punctuation)
a = ''.join(ch for ch in a if ch not in exclude)
a = a.lower()
a = ' '.join(a.split())

grams = { 5 : None,
          6 : None,
          7 : None,
          8 : None,
          9 : None,
          10: None }

for key in grams.iterkeys():
    g = a
    grams[key] = [w for w in ngrams(g.split(), key)]
    print str(key)+"-grams:"
    fdist = nltk.FreqDist(grams[key])
    fdist_s = sorted(fdist.items(), key=lambda x: x[1], reverse=True)
    for k, v in fdist_s:
        if v > 2:
            print str(v) + ': ' + ' '.join([b for b in k])
