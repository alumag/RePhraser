__author__ = 'User'
""" This script wrote by Aluma Gelbard """

import nltk
import string
from nltk.corpus import wordnet as wn


def main():
    #print(synonym('spark.v.01').getSynonym())
    for ss in wn.synsets('before'):
        print(ss.name(), ss.lemma_names())

    pass


class synonym(object):
    def getSynonym(self):
        """
        :return: synonym of the object
        """
        return (wn.synset(self._word)).hypernyms()

    def __init__(self, word):
        """
        :param word: original word
        :return: synonym of the word or the same word
        """
        self._word = word
        return None

if __name__ == '__main__':
    main()