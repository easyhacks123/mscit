import spacy
nlp = spacy.blank("en")
str = "I love to study Natrual Language processing in python"
doc = nlp(str)
words = [ word.text for word in doc]
print(words)
