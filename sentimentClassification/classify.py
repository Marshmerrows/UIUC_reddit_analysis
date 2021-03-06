from nltk.corpus import movie_reviews
from random import randint
import nltk.classify.util
from nltk.metrics.scores import (precision, recall)
import collections
import pickle

featureset = [word.strip() for word in open('res/featureset', 'r').readlines()]
print featureset
trainData = open("res/all_reviews.txt")


reviews = []
for files, label in [(movie_reviews.fileids('neg'), 0), (movie_reviews.fileids('pos'), 1)]: # negative has 0 label, pos has 1
    print "working on " + str(label)
    for file in files:
        wordSet = movie_reviews.words(file)
        word_dict = {}
        for word in wordSet: # get full word count
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
        reviews.append((feature_dict, label)) # 0 identifies negative review

train = []
test = []
#only for testing, real model will make use of all the data
for review in reviews: # split into train and test data randomly, 20% of data goes to test
    randnum = randint(0, 100)
    if randnum > 80:
        test.append(review)
    else:
        train.append(review)

print "classifying.........."
try:
    old_class = open("res/bayes_classifier_test.pickle", "rb")
    classifier = pickle.load(old_class)
    classifier.train(train)
    old_class.close()
except IOError:
    classifier = nltk.NaiveBayesClassifier.train(train)

observed_test = collections.defaultdict(set)
reference_test = collections.defaultdict(set)
for i, (features, label) in enumerate(test):
    reference_test[label].add(i)
    val = classifier.classify(features)
    observed_test[val].add(i)

print 'accuracy: {}'.format(nltk.classify.accuracy(classifier, test))
print 'recall pos: {}'.format(recall(observed_test[1], reference_test[1]))
print 'precision pos: {}'.format(precision(observed_test[1], reference_test[1]))
print 'recall neg: {}'.format(precision(observed_test[0], reference_test[0]))
print 'precision neg: {}'.format(precision(observed_test[0], reference_test[0]))


print "saving..............."
new_class = open("res/bayes_classifier_test.pickle", "wb+")
pickle.dump(classifier, new_class)
new_class.close()
