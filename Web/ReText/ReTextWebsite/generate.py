#!/usr/bin/python
import os
import subprocess


class generate(object):
	def __init__(self, sentence):
		self._sentence = sentence
	
	def create_page(self):
		print(os.path.dirname(os.path.realpath(__file__)))
		file = open("C:\Users\Viole\Documents\Magshimim\Project\Web\ReText\ReTextWebsite\\templates\ReTextWebsite\\rephrase.html", 'r')
		newfile = open("C:\Users\Viole\Documents\Magshimim\Project\Web\ReText\ReTextWebsite\\templates\ReTextWebsite\\newRephrase.html", "w")

		try:
			p = subprocess.Popen('python try.py', stdout=subprocess.PIPE)
			#p = subprocess.Popen(['python','../../../Run/ParseSentence.py -s "'+self._sentence+'"'], stdout=subprocess.PIPE)
			self._sentence = p.communicate()
			#self._sentence = os.system('python ../../../Run/ParseSentence.py -s "'+self._sentence+'"')
			#self._sentence = subprocess.check_output('python ../../../Run/ParseSentence.py -s "'+self._sentence+'"', shell=True)
		except subprocess.CalledProcessError as e:
			self._sentence = e.output
		finally:
			print("Yeah yeah no exception")
		print("Sentence: " + str(self._sentence))
		
		if(self._sentence == None):
			self._sentence = "Sorry, error :("

		newfile.write(file.read().replace("<ul id=\"msg\"> </ul>", str(self._sentence)))
		newfile.close()
		file.close()