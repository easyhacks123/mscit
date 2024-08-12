import nltk
from nltk.parse import malt
mp = malt.MaltParser('D:/nlp/maltparser-1.7.2','D:/nlp/engmalt.linear-1.7.mco')
t = mp.parse_one('I saw a bird from my window.'.split()).tree()
print(t)
t.draw()
