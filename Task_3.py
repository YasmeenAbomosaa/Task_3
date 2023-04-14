
from nltk.stem import PorterStemmer
ps = PorterStemmer()
word =  ["programming"]
for x in word:
     print(x, ":", ps.stem(x))


print("---------------------------------------------")
print("---------------------------------------------")


from nltk.stem import  SnowballStemmer
ss = SnowballStemmer('english')
word =  ["programming"]
for x in word:
     print(x, ":", ps.stem(x))