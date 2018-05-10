"""
This script looks at the words with emotion value data set and selects only the words with high negative or positive
emotion and writes them to another file in order to pick out a word feature set to use for the training data.
"""

STRONG_SENTIMENT = [
                    'anger',
                    #'anticipation',
                    'disgust',
                    #'fear',
                    'joy',
                    'negative',
                    'positive',
                    'sadness',
                    #'surprise',
                    #'trust'
                    ]

sentiment_words = set()
with open("res/NRC_Emotion.txt", "r") as f:
    for line in f.readlines():
        cur_word = line.split()
        if cur_word[2] == '1': # strong sentiment??
            if cur_word[1] in STRONG_SENTIMENT: # is a valid sentiment
                sentiment_words.add(cur_word[0])

    with open("res/featureset", "w+") as w_f:
        for word in list(sentiment_words):
            print word
            w_f.write(word + '\n')
