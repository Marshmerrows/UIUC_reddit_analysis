from nltk.corpus import stopwords
from nltk import word_tokenize
from gensim import models, corpora
import re
import os


folder = "testData"
data = []

for path,dirs,file in os.walk(folder):
    for document in file:
        fullname = os.path.abspath(os.path.join(path,document))
        with open(fullname, 'r') as currFile:
            tempData = currFile.read().replace("\n" , ' ')
            data.append(tempData)

numTOPICS = 2
stopWORDS = stopwords.words('english')

def cleanData(text):
    tokenText = word_tokenize(text.lower())
    cleanText = [word for word in tokenText if word not in stopWORDS and re.match('[a-z][a-z]{2,}', word)]
    return cleanText

tokenData = []

for preProsText in data:
    tokenData.append(cleanData(preProsText))

dataDictionary = corpora.Dictionary(tokenData)

BoWCorpus = [dataDictionary.doc2bow(document) for document in tokenData]

print(corpus[2])
