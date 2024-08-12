import nltk
from nltk.tokenize import RegexpTokenizer
tk = RegexpTokenizer('\s+', gaps=True)
str = "I love to study Natrual Language processing in python"
tokkens = tk.tokenize(str)
print(tokkens)
