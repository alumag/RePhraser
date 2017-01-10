__author__ = 'User'

import re
import nltk
import synonym
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
        sentences = re.split(r'\.\?!', text)
        open(newFile, 'w')
        for sentence in sentences:
            newFile.write(change_sentence(sentence))

s = "Lummie is love very much apples"
print s
print change_sentence(s)