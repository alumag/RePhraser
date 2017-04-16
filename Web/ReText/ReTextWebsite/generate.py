#!/usr/bin/python
import os
import subprocess

"""
This class run the ParseSentence.py script according to the input of the client.
This algorthm is awful but actually we dont care. GET OVER IT!!
"""
class generate(object):
	def __init__(self, sentence):
		self._sentence = sentence
	
	def create_page(self):	
		run_str = "python ../../Run/ParseSentence.py -s \"{0}\" > out.txt"
		run_str = run_str.replace("{0}", self._sentence)
		file = open("C:\Users\Viole\Documents\Magshimim\Project\Web\ReText\ReTextWebsite\\templates\ReTextWebsite\\index.html", 'r')
		newfile = open("C:\Users\Viole\Documents\Magshimim\Project\Web\ReText\ReTextWebsite\\templates\ReTextWebsite\\newindex.html", "w")
		
		os.system(run_str)
		output = open("out.txt", 'r')
		self._sentence = output.read()
		
		if(self._sentence == None):
			self._sentence = "Sorry, there is some error :(</br>Please connect Aluma/Arad and tell them it happen. Maybe theyll care.."

		newfile.write(file.read().replace("<textarea name=\"text\" id=\"text\" placeholder=\"Enter your text\" rows=\"6\"></textarea>","<textarea name=\"text\" id=\"text\" placeholder=\"Enter your text\" rows=\"6\">" + str(self._sentence) + "</textarea>"))
		newfile.close()
		file.close()
		output.close()