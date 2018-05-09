import nltk
from nltk.corpus import stopwords
import string

sentimentData = open("NRC_Emotion.txt")
trainData = open("all_reviews.txt")

pos = {}                                #all words that have a positive sentiment
neg = {}                                #all words that have a negative sentiment

for line in trainData.readlines():      #sets up negative and positive sentiment dicts
    temp = line.split()
    print temp
    if temp[1] == "positive":
        pos[temp[0]] = temp[2]
        print temp[0]
    elif temp[1] == "negative":
        neg[temp[0]] = temp[2]
        print[temp[0]]
    else:
        continue


def cleanData(dataSet):
    puncStr = datatSet.translate(None, string.punctuation)
    puncStr = puncStr.lower()
    cleanText = [word for word in puncStr if word not in stopwords.words('english')]
    return cleanText

def wordFeatureSet(words):
    currDict = dict([(word, True) for word in words])
