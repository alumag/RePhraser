import os
import string
from random import randrange
import requests
import sqlite3
from lxml import html
import nltk

from .utils import no_punctuation


"""
Dear un-hebrew speakers:
'Tmura' is 'Grammatical modifier': an element that describes the object in sentence.
We love the name 'Tmura', So we use it.

for example:
without Tmura: Lummie and Arad study in Magshimim
with Tmura: Lummie and Arad study in Magshimim, The national cyber project
"""


def cleanText(sen):
    return no_punctuation(sen)


def writeToOurCorpus(sentence):
    """
    Gets a sentence (that contains a tmura) and writes it into the tmura.txt file, so we will have a corpus
    """
    with open("tmura.txt", "a") as text_file:
        text_file.write(sentence + os.linesep)


def downloadPage(word):
    """
        Gets a word, finds its page in wordnet and downloades it. Returns a correct HTML document,
        which means the parent node is <html>, and there is a body and possibly a head
    """
    search = "http://wordnetweb.princeton.edu/perl/webwn?s="
    search += word
    search += "&sub=Search+WordNet&o2=&o0=1&o8=1&o1=1&o7=&o5=&o9=&o6=&o3=&o4=&h=0" # Builds the url
    page = requests.get(search) # Get page
    return html.fromstring(page.content) # Fromstring creates the correct HTML document


def getTmura(word):
    """
        Gets a word, gets its html page in wordnet (using downloadPage(word)), and returns the tmura of the word.
    """
    # TODO: Use BeautifulSoup instead of this horrible xpath
    tree = downloadPage(word)  # Gets the page data
    words = tree.xpath("//div[@class='form']/ul/li/text()")  # Gets only the text
    theWord = []
    for i in words:
        if i != ', ':  # We want to take only the first tmura and to clear all of the ', '
            theWord = i
            break
    if theWord != []:  # If found a tmura
        theWord = theWord.split(';')[0].replace(" (", "") # Cleans the tmura from '(' and ')' in the first explenation
        theWord = theWord.split(';')[0].replace(")", "")
        return theWord
    else:  # If didn't find a tmura
        return "not found"


def findTmura(word):
    """
        Gets a word, pharses it and finds it tmure. Gets only nouns!!!
        Returns the original word and the tmura- word: tmura
    """
    the_tmura = word + ": " + getTmura(word.replace(" ", "+"))
    return the_tmura


class Modifier(object):
    def change_sentence(self, sentence):
        text = nltk.tokenize.word_tokenize(sentence)
        changed = False
        for cur in nltk.pos_tag(text):
            if cur[1] == "NN" or cur[1] == "NNP" or cur[1] == "RPR":
                tmura = self.find(cur[0])
                if tmura and not changed:
                    if randrange(2) == 0:
                        rep = cur[0] + ", " + tmura + ", "
                    else:
                        rep = cur[0] + "(" + tmura + ") "
                        
                    sentence = sentence.replace(cur[0], rep)
                    changed = True
        return sentence

    def find(self, word):
        founded = self.getFromDB(word)
        if not founded:
            founded = getTmura(word)
            if founded != "not found":
                founded = founded.replace('OR', 'or')
                self.add2DB(word, founded)
                return founded
        else:
            return founded

    def getFromDB(self, word):
        cur = self._conn.cursor()
        cur.execute("SELECT Define FROM tmura WHERE WORD=\""+word.lower()+"\"")
        self._conn.commit()
        rows = cur.fetchall()
        if len(rows) == 0:  # Does'nt exist
            return None
        return rows[0][0]
    
    def add2DB(self, word, define):
        try:
            self._conn.execute("INSERT INTO tmura (WORD, Define) \
            VALUES (?, ?)", (word.lower(), define.lower()))
            self._conn.commit()
            return True
        except:
            return False
        self._conn.commit()
    
    def addTable(self):
        self._conn.execute('''CREATE TABLE tmura
               (ID INTEGER  PRIMARY KEY  AUTOINCREMENT     NOT NULL,
               WORD TEXT NOT NULL,
               Define TEXT    NOT NULL);''')
        self._conn.commit()

    def __init__(self):
        """
        :param word: sentence
        :return: sentence with tmura
        """
        path = os.path.dirname(os.path.realpath(__file__))
        self._conn = sqlite3.connect(path+'\\tmura.db')

    def __del__(self):
        self._conn.close()
