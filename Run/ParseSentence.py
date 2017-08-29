__author__ = 'User'

from re import split as reSplit
from nltk import tokenize
from nltk import tag
import sys
from os import linesep
from nltk import FreqDist
from collections import Counter
from nltk.corpus import stopwords

from tmura import * # Import our Modifier module
from Active2Passive import * # Import our Active convertor module
from synonym import * # Import our Synonym module

import socket
import threading

def TF(text):
	"""
	this function return the TF grade of word in a document
	:param text: text to find a TF to.
	:return: most common word in the text
	"""
	tokens = tokenize.word_tokenize(text)
	filtered = [w for w in tokens if not w in stopwords.words('english')]
	fdist = FreqDist(tokens)
	try:
		return fdist.most_common(1)
	except:
		return None

def change_sentence(sentence):
	try: # Active 2 Passive using try because Arad is retard
		sentence = Active2Passive(sentence).change_sentence()
	except:
		pass
	try:	
		sentence = Modifier(sentence).change_sentence() # Add data
	except:
		pass
	
	text = tokenize.word_tokenize(sentence)
	new_sentence = ""
	
	syn = synonym()
	for cur in tag.pos_tag(text):
		if (cur[1] == "RB" or cur[1] == "VBP" or cur[1] == "VB" or cur[1] == "CC" or cur[1] == "PRT"):
			synonym1 = syn.getSynonym(cur[0])
			if not synonym1 == cur[0].upper():
				if '_' in synonym1:
					synonym1 = synonym1.replace('_', ' ')
				sentence.replace(cur[0], synonym1)
				new_sentence += synonym1 + " "
			else:
				new_sentence += cur[0] + " "
			
		else:
			if cur[0] in string.punctuation:
				new_sentence += cur[0]
			else:
				new_sentence += cur[0] + " "
				
	syn.disconnectDB()
	return new_sentence


def change_text(originalFile, newFile):
	with open(originalFile, 'r') as f:
		text = f.read()
		sentences = reSplit(r'\.\?!', text)
		new = open(newFile, 'w')
		new_sentences = []
		for sentence in sentences:
			print sentences, linesep
			changeSent = change_sentence(changeSent)
			new_sentences.append(changeSent)
			print (">> ", changeSent, linesep)
		new.writelines(new_sentences)
	new.close()
	f.close()

class ThreadedServer(object):
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.bind((self.host, self.port))

	def listen(self):
		print("listening")
		self.sock.listen(5)
		while True:
			client, address = self.sock.accept()
			client.settimeout(60)
			print("got a client: " + str(address)) 
			threading.Thread(target = self.listenToClient,args = (client,address)).start()

	def listenToClient(self, client, address):
		size = 4000
		while True:
			try:
				data = client.recv(size)
				if data:
					# Set the response to echo back the recieved data 
					print data
					response = change_sentence(data)
					client.send(response)
				else:
					raise error('Client disconnected')
			except:
				client.close()
				return False

def main(argv):
	if len(argv) == 1:
		s = raw_input()
		print change_sentence(s)
	elif len(argv) == 2 and argv[1] == "-help":
		print "python ParseSentence.py -s ''<sentence>''"
		print "python ParseSentence.py -f ''<filename>''"
		print "python ParseSentence.py"
		sys.exit(0)
		
	elif len(argv) == 2 and argv[1] == "-r":
		ThreadedServer('0.0.0.0',9292).listen()
		
	elif len(argv) == 3 and argv[1] == "-s":
		print change_sentence(argv[2])

	elif len(argv) == 3 and argv[1] == "-f":
		try:
			change_text(argv[2], "log.txt")
		except Exception as inst:
			print "Error"
			print type(inst)
			print inst.args
			print inst
		finally:
			print

	else:
		print "Syntax error"
		print "USE -help command"
		sys.exit(1)

if __name__ == '__main__':
	main(sys.argv)

