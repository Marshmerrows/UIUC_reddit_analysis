from nltk.corpus import stopwords
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import nltk.classify.util
import string

STOPWORDS = stopwords.words('english')
# sentimentData = open("NRC_Emotion.txt")
trainData = open("all_reviews.txt")

posReviews = []                                #all words that have a positive sentiment
negReviews = []                                #all words that have a negative sentiment

# for line in trainData.readlines():      #sets up negative and positive sentiment dicts
#     temp = line.split()
#     print temp
#     if temp[1] == "positive":
#         pos[temp[0]] = temp[2]
#         print temp[0]
#     elif temp[1] == "negative":
#         neg[temp[0]] = temp[2]
#         print[temp[0]]
#     else:
#         continue


def cleanData(dataSet):
    # //puncStr = dataSet.translate(None, string.punctuation)
    # puncStr = puncStr.lower()
    cleanText = [word for word in dataSet if word not in STOPWORDS]
    currDict = dict([(word, True) for word in cleanText])
    return currDict

for file in movie_reviews.fileids('neg'):
    wordSet = movie_reviews.words(file)
    negReviews.append((cleanData(wordSet), "negative"))

for file in movie_reviews.fileids('pos'):
    posWordSet = movie_reviews.words(file)
    posReviews.append((cleanData(posWordSet), "positive"))


numFolds = 10
foldSize = len(posReviews)/numFolds
for i in range(numFolds):
    testingData = posReviews[i*foldSize:][:foldSize] + negReviews[i*foldSize:][:foldSize]
    trainingData = (posReviews[:i*foldSize] + posReviews[(i+1)*foldSize:]) + (negReviews[:i*foldSize] + negReviews[(i+1)*foldSize:])
    classifier = NaiveBayesClassifier.train(trainingData)
    print nltk.classify.util.accuracy(classifier, testingData)
