from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import pickle
import nltk.classify.util
import string
import os

CLASSIFIER = "res/bayes_classifier.pickle"
START_DIR = "courses"
TOKENIZER = RegexpTokenizer(r'\w+')
stopWORDS = stopwords.words('english')
classifier = open(CLASSIFIER, "rb")
classifier = pickle.load(classifier)
featureset = [word.strip() for word in open('res/featureset', 'r').readlines()]

def cleanData(currText):
    """
    takes an input string currText, cleans it of punctuation and stopwords,
    and returns it as a tokenized list
    :param currText: string of wordbois for us to clean
    :return: list of tokenized words
    """
    tokenTextPunct = currText.translate(None, string.punctuation)
    tokenTextPunct = unicode(tokenTextPunct, errors='replace')
    tokenTextRaw = tokenTextPunct.lower()
    tokenText = TOKENIZER.tokenize(tokenTextRaw)
    cleanText =[word for word in tokenText if word not in stopWORDS]
    return cleanText

def classify(token_list):
    word_dict = {}
    for word in token_list: # get full word count
        word = word.encode('ascii', 'ignore')
        if word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    feature_dict = {}
    for word in featureset: # move that over to feature set
        if word in word_dict.keys():
            feature_dict[word] = word_dict[word]
        else:
            feature_dict[word] = 0
    return classifier.classify(feature_dict)

def recurse_traverse(rating_dict, dir, course):
    for item in os.listdir(dir):
        path = dir + '/' + item
        if os.path.isdir(path): #search into this directory
            print "searching: " + path
            recurse_traverse(rating_dict, path, item)
        else: #just a joe schmoe file name
            print "classifying: " + path
            with open(path, "r") as f:
                data = []
                for line in f.readlines():
                    if line != "----":
                        data.append(line)
                data = ' '.join(data)
                tokens = cleanData(data)
                value = classify(tokens)

                if value == 0: #negative sentiment
                    value = -1; #subtract one from total sentiment value

                if course in rating_dict.keys():
                    rating_dict[course] += value
                else:
                    rating_dict[course] = value
ratings = {}
recurse_traverse(ratings, START_DIR, 'NONE')

with open("res/final.csv", "w+") as f:
    for key in ratings.keys():
        f.write(key + "," + str(ratings[key]) + '\n')
