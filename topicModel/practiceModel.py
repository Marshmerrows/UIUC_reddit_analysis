from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from gensim import models, corpora
import re, string, os

TOKENIZER = RegexpTokenizer(r'\w+')

folder = "testData"
data = []
someNonSense = 43
for path,dirs,file in os.walk(folder):
    for document in file:
        fullname = os.path.abspath(os.path.join(path,document))
        with open(fullname, 'r') as currFile:
            tempData = ' '.join(currFile)
            data.append(tempData)


numTOPICS = 8
stopWORDS = stopwords.words('english')

def cleanData(currText):
    tokenTextPunct = currText.translate(None, string.punctuation)
    tokenTextPunct = unicode(tokenTextPunct, errors='replace')
    tokenTextRaw = tokenTextPunct.lower()
    tokenText = TOKENIZER.tokenize(tokenTextRaw)
    cleanText =[word for word in tokenText if word not in stopWORDS]
    return cleanText

tokenData = []

for preProsText in data:
    # cleanData(preProsText)
    tokenData.append(cleanData(preProsText))

dataDictionary = corpora.Dictionary(tokenData)

BoWCorpus = [dataDictionary.doc2bow(document) for document in tokenData]

lda_model = models.LdaModel(BoWCorpus, numTOPICS, dataDictionary)

bow = [dataDictionary.doc2bow(tokenData[0])]
document = lda_model.get_document_topics(bow)

print "LDA Model"

for i in range(numTOPICS):
    print("Topic #{}".format(i) + lda_model.print_topic(i, numTOPICS))
