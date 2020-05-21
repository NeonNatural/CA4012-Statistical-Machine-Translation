import collections
import codecs
ngram = int(input("Please enter an gram "))
def read_file(corpus):
    with codecs.open(corpus, 'r') as corpus:
        corpus = corpus.readlines()
    return corpus

def word_freq(corpus):

    corpus = read_file(corpus)
    numbertk = len(corpus)
    count_dict = collections.Counter(corpus)
    lst= []
    for key, value in count_dict.items():
        n = 'The word',key,'frequency is:',float(value)/numbertk
        lst.append(n)
    return lst


def unigram(input, corpus):

    corpus  = read_file(corpus)
    co = []
    for sentence in corpus:
        co.append(sentence.split())

    flat = [item for sublist in co for item in sublist]
    input = input.split()
    for i in range(len(corpus)):
        count_dict = collections.Counter(flat)
    count = 1
    for key, value in count_dict.items():
        if key in input:
            count *= float(value)/len(corpus)


    return count


def getBigramsCorpus(input_file):
    corpus= read_file(input_file)
    bigramCL=[]
    for sentence in corpus:
        for i in range(len(sentence.split())-ngram+1): #-2 because bigrams

            bigramCL.append(sentence.split()[i:i+ngram]) #+2 because bigrams
    return bigramCL


def getBigramsSent(sent):
    bigramSL=[]
    for i in range(len(sent.split())-ngram+1):
        bigramSL.append(sent.split()[i:i+ngram])
    return bigramSL


def bigramP(sent, input_file):

    bigramsSentence=getBigramsSent(sent)

    bigramsCorpus=getBigramsCorpus(input_file)

    totalBigramProb=1
    for bigramS in bigramsSentence:
        bigramCount=bigramsCorpus.count(bigramS)

        totalCount=0
        for bigramC in bigramsCorpus:
            if ngram == 1:
                totalCount+=1
            else:
                if bigramS[0:ngram-1] == bigramC[0:ngram-1]:
                   totalCount+=1
        totalBigramProb*=float(bigramCount)/float(totalCount)
    return totalBigramProb



def getVocab(input_file):
    wordDict={}
    c = read_file(input_file)
    for sentence in c:
        for i in range(len(sentence.split())):
            if sentence.split()[i] in wordDict:
                wordDict[sentence.split()[i]]+=1
            else:
                wordDict[sentence.split()[i]]=1
    return wordDict

def bigramPSmoothing(sent, input_file):
    bigramsSentence=getBigramsSent(sent)

    bigramsCorpus=getBigramsCorpus(input_file)
    vocabDict=getVocab(input_file)
    vocabCount=len(vocabDict)
    totalBigramProb=1
    for bigramS in bigramsSentence:
        bigramCount=bigramsCorpus.count(bigramS)
        totalCount=0
        for bigramC in bigramsCorpus:
            if ngram == 1:
                totalCount+=1
            else:
                if bigramS[0:ngram-1] == bigramC[0:ngram-1]:
                   totalCount+=1
        totalBigramProb*=float(bigramCount+1)/float(totalCount+vocabCount)

    return totalBigramProb


def main():
    c = word_freq('corpus.txt')
    l = unigram('cat sat ont he mat', 'corpus.txt')
    o = bigramP('cat sat', 'corpus2.txt')
    k = bigramPSmoothing('<s> a cat sat on the mat </s>', 'corpus2.txt')
    print(k)
if __name__ == "__main__":
    main()
