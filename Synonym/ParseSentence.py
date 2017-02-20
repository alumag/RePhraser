__author__ = 'User'

import re
import nltk
import synonym
import sys
__import__("synonym")


def change_sentence(sentence):
    text = nltk.tokenize.word_tokenize(sentence)
    new_sentence = ""
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
        new = open(newFile, 'w')
        new_sentences = []
        for sentence in sentences:
            print sentences
            new_sentences.append(change_sentence(sentence))
        new.writelines(new_sentences)
    new.close()
    f.close()

def main(argv):
    if len(argv) == 1:
        s = raw_input()
        print change_sentence(s)
    elif len(argv) == 2 and argv[1] == "-help":
        print "python ParseSentence.py -s ''<sentence>''"
        print "python ParseSentence.py -f ''<filename>''"
        print "python ParseSentence.py"
        sys.exit(0)

    elif len(argv) == 3 and argv[1] == "-s":
        print change_sentence(argv[2])

    elif len(argv) == 3 and argv[1] == "-f":
        try:
            change_text(argv[2], "log.txt")
        except:
            print "Error"
        finally:
            print

    else:
        print "Syntax error"
        print "USE -help command :)"
        sys.exit(1)

if __name__ == '__main__':
    main(sys.argv)

