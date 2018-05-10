from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from gensim import models, corpora
import re, string, os

TOKENIZER = RegexpTokenizer(r'\w+')
folder = "../res_all/res2"
numTOPICS = 8
stopWORDS = stopwords.words('english')


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
    cleanText =[[word] for word in tokenText if word not in stopWORDS]
    return cleanText

def get_topic(data):
    """
    runs a topic modeler on 'data' and returns numTOPIC number of topics for the string (the top topics)
    :param data: data to find topic of
    :return: list of top topics
    """
    tokenData = cleanData(data)
    if len(tokenData) == 0:
        return "NAH BB"
    dataDictionary = corpora.Dictionary(tokenData)
    BoWCorpus = [dataDictionary.doc2bow(document) for document in tokenData]

    lda_model = models.LdaModel(BoWCorpus, numTOPICS, dataDictionary)

    bow = [dataDictionary.doc2bow(tokenData[0])]
    document = lda_model.get_document_topics(bow)

    return lda_model.print_topic(0, numTOPICS)

COURSE_RE = '[a-z]{2,10} ?[1-5][0-9][0-9]'
pattern = re.compile(COURSE_RE)

for path,dirs,file in os.walk(folder):
    print path
    for document in file:
        fullname = os.path.abspath(os.path.join(path,document))
        with open(fullname, 'r') as currFile:
            data = []
            for line in currFile.readlines():
                if line != "----":
                    data.append(line)

            data = ' '.join(data)
            topics = get_topic(data)
            courses = pattern.findall(topics)

            for course in courses:
                print fullname
                print course
