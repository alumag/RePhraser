__author__ = 'User'

import re
import nltk
import synonym
import sys
__import__("synonym")

def change_sentence(sentence):
    text = nltk.tokenize.word_tokenize(sentence)
    new_sentence = ""
    #print text
    #print nltk.tag.pos_tag(text)
    for cur in nltk.tag.pos_tag(text):
        if (cur[1] == "RB" or cur[1] == "VBP" or cur[1] == "VB" or cur[1] == "CC" or cur[1] == "PRT"):
            synonym1 = synonym.synonym(cur[0]).getSynonym()
            sentence.replace(cur[0], synonym1)
            new_sentence += synonym1 + " "
        else:
            new_sentence += cur[0] + " "
    return new_sentence



def change_text(originalFile, newFile):
    with open(originalFile, 'r') as f:
        text = f.read()
        print text
        sentences = re.split(r'\.\?!', text)
        new = open(newFile, 'w')
        new_sentences = []
        for sentence in sentences:
            new_sentences.append(change_sentence(sentence))
        new.writelines(new_sentences)
    new.close()
    f.close()

def change_text(text="Hey i just met you"):
    print text
    sentences = re.split(r'\.\?!', text)
    new = ""
    for sentence in sentences:
        new += change_sentence(sentence)
    print new
    return new

change_text(sys.argv[1])

# s = "Bring me all your money, fast."
# print s
# print change_sentence(s)
#
# change_text("../Texts/crisis.txt", "../Texts/new_crisis.txt")

