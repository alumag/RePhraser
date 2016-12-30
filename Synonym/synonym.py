__author__ = 'User'
""" This script wrote by Aluma Gelbard """

import nltk
import string
from nltk.corpus import wordnet as wn
import operator
from collections import Counter



def main():
    print(synonym('phone').getSynonym())
    pass


class synonym(object):
    def getSynonym(self):
        """
        :return: synonyms of the object
        """
        return self.choseSynonym(wn.synsets(self._word))

    def choseSynonym(self, ss):
        count = []
        for s in ss:
            for word in s.lemma_names():
                if word != self._word:
                    count.append(word)
        return Counter(count).most_common(1)[0][0]

    def __init__(self, word):
        """
        :param word: original word
        :return: synonym of the word or the same word
        """
        self._word = word
        return None

if __name__ == '__main__':
    main()