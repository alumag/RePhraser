__author__ = 'User'

from lxml import html
import requests
import re
from nltk import pos_tag, word_tokenize
import nltk
import string
from nltk.corpus import stopwords
from collections import Counter
from math import log10
import time

"""
Dear un-hebrew speakers:
'Tmura' is 'Grammatical modifier': an element that describes the object in sentence.
We love the name 'Tmura', So we use it.

for example:
without Tmura: Lummie and Arad study in Magshimim
with Tmura: Lummie and Arad study in Magshimim, The national cyber project
"""

def cleanText(sen):
    for ch in string.punctuation:
        sentence = sentence.replace(ch, '')
    return sentence


"""
Gets a sentence (that contains a tmura) and writes it into the tmura.txt file, so we will have a corpus
"""
def writeToOurCorpus(sentence):
    text_file = open("tmura.txt", "a")
    text_file.write(sentence + "\n")
    text_file.close()


"""
    Gets a word, finds its page in wordnet and downloades it. Returns a correct HTML document,
    which means the parent node is <html>, and there is a body and possibly a head
"""
def downloadPage(word):
    search = "http://wordnetweb.princeton.edu/perl/webwn?s="
    search += word
    search += "&sub=Search+WordNet&o2=&o0=1&o8=1&o1=1&o7=&o5=&o9=&o6=&o3=&o4=&h=0" # Builds the url
    page = requests.get(search) # Get page
    return html.fromstring(page.content) # Fromstring creates the correct HTML document

"""
    Gets a word, gets its html page in wordnet (using downloadPage(word)), and returns the tmura of the word.
"""
def getTmura(word):
    tree = downloadPage(word) # Gets the page data
    words = tree.xpath("//div[@class='form']/ul/li/text()") #Gets only the text
    theWord = []
    for i in words:
        if (i != ', '): # We want to take only the first tmura and to clear all of the ', '
            theWord = i
            break
    if (theWord != []): # If found a tmura
        theWord = theWord.split(';')[0].replace(" (", "") # Cleans the tmura from '(' and ')' in the first explenation
        theWord = theWord.split(';')[0].replace(")", "")
        return theWord
    else: # If didn't find a tmura
        return "not found"


"""
    Gets a word, pharses it and finds it tmure. Gets only nouns!!!
    Returns the original word and the tmura- word: tmura
"""
def findTmura(word):
    the_tmura = word + ": " + getTmura(word.replace(" ", "+"))
    #writeToOurCorpus(the_tmura) # Olny if we want to put it in our corpus
    return the_tmura


"""
    It must be a class, so we can call it.
"""

class Modifier(object):
    def change_sentence(self):
        text = nltk.tokenize.word_tokenize(self._sentence)
        changed = False
        for cur in nltk.pos_tag(text):
            if (cur[1] == "NN" or cur[1] == "NNP" or cur[1] == "RPR"):
                if getTmura(cur[0]) != "not found" and changed == False:
                    rep = cur[0] + ", " + getTmura(cur[0]) + ", "
                    self._sentence = self._sentence.replace(cur[0], rep)
                    changed = True
        return self._sentence

    def __init__(self, sentence):
        """
        :param word: sentence
        :return: sentence with tmura
        """
        self._sentence = sentence
        return None


def main():
    with open("newSent.txt", 'w') as newF:
        with open("sentences.txt", 'r') as f:
            sentence = f.read()
        f.close()
        sentences = sentence.split('\n')
        for sent in sentences:
            print(Modifier(sent).change_sentence)
            newF.write(Modifier(sent).change_sentence + "\n")

    newF.close()