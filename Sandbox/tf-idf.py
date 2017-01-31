__author__ = 'User'
""" This script wrote by Arad Kotzer and Aluma Gelbard
                    December 2016                     """

import nltk
import string
from nltk.corpus import stopwords
from collections import Counter
from math import log10
import time


def main():
    filenames = ["text1.txt", "text2.txt", "text3.txt"] # the file-names: uses them as corpus
    corpus = makeCorpus(filenames)  # read the files and place them in a list

    for f in filenames:
        print("----\nStarting: " + f)
        now = time.time()
        printLog(f, corpus)
        print("It took: " + str(time.time() - now) + " sec.")
        print("FINISH\n")

def printLog(filename, corpus):
    text = cleanText(filename)
    filename = filename.replace('.txt', '') + 'Log.txt'
    file = open(filename, 'w')

    print("opened " + filename)

    file.write(filename.replace(".txt", '') + '\n')
    for word in Counter(getWords(text)):
        string = word + " TF-IDF Score: " + str(TF_IDF(word, text, corpus))
        file.write(string)
        file.write('\n')
    file.close()


def makeCorpus(fileNames):
    # Input: list of text-files name
    # Output: list of texts
    corpus = []
    for f in fileNames:
        corpus.append(cleanText(f))
    return corpus


def TF_IDF(word, text, corpus):
    # Output: TF_IDF grade for a word in a text
    return (TF(word, text) * IDF(word, corpus))


def IDF(word, corpus):
    # return IDF grade
    word = word.lower()
    wordAppears = 0
    for text in corpus:
        if word in text:
            wordAppears +=1
    #wordAppears +=1 # avoid dividing by zero
    length = len(corpus) # number of texts
    return log10((length/wordAppears))


def TF(word, text):
    # this function return the TF grade of word in a document
    word = word.lower()
    tokens = getWords(text)
    counter = (Counter(tokens)).get(word)
    if (counter == None):
        counter = 0
    length = len(tokens)
    return (counter/length)


def cleanText(filename):
    # read the file and return clean text
    with open(filename, 'r') as f:
        text = (f.read()).lower()
    for ch in string.punctuation:
        text = text.replace(ch, '')
    f.close()
    return text


def getWords(text):
    # this function clear the text and tokenize it
    tokens = nltk.tokenize.word_tokenize(text)
    filtered = tokens#[w for w in tokens if not w in stopwords.words('english')]
    return filtered

if __name__ == '__main__':
    main()