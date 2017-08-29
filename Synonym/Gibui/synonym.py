__author__ = 'User'
""" This script wrote by Aluma Gelbard """

import string
from nltk.corpus import wordnet as wn
from collections import Counter



def main():
	print(synonym('shine').getSynonym())
	pass


class synonym(object):
	def getSynonym(self):
		"""
		:return: synonyms of the object
		"""
		if self._word in "aluma arad kotzer gelbard brit":
			return self._word + " (The Lord)"
		return self.choseSynonym(wn.synsets(self._word))

	def choseSynonym(self, ss):
		count = []
		for s in ss:
			for word in s.lemma_names():
				if word != self._word:
					count.append(word)
		if len(count) == 0:
			return self._word
		return Counter(count).most_common(1)[0][0]

	def __init__(self, word):
		"""
		:param word: original word
		:return: synonym of the word or the same word
		"""
		self._word = word
		return None