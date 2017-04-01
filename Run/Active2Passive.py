__author__ = 'User'


import en as en
import nltk
import string

def cleanText(sen):
    for ch in string.punctuation:
        sentence = sentence.replace(ch, '')
    return sentence

"""
Gets a sentence (that contains a tmura) and writes it into the tmura.txt file, so we will have a corpus
"""
def writeToOurCorpus(sentence):
    text_file = open("tmura.txt", "a")
    text_file.write(sentence + "\n")
    text_file.close()


def active_change_sentence(sentence):
    text = nltk.tokenize.word_tokenize(sentence)
    for cur in nltk.pos_tag(text):
        print cur[0] + "- " + cur[1]


def get_word_past_participle(word):
    return en.verb.past_participle(word)


def make_string(list):
    return " ".join(str(x) for x in list)


def switch_JJ(sent, i1, i2):
    parsed = nltk.pos_tag(nltk.tokenize.word_tokenize(make_string(sent)))
    if((parsed[i1 - 1][1] == "JJ" and parsed[i2 - 1][1] == "JJ") or (parsed[i1 - 1][1] == "DT" and parsed[i2 - 1][1] == "DT")):
        temp = sent[i1 - 1]
        sent[i1 - 1] = sent[i2 - 1]
        sent[i2 - 1] = temp
    elif(parsed[i1 - 1][1] == "JJ"):
        sent.insert(i2 - 1, sent[i1 - 1])
        sent.pop(i1 - 1)
        i1 -= 1
    elif(parsed[i1 - 1][1] == "DT"):
        sent.insert(i2, sent[i1 - 1])
        sent.pop(i1 - 1)
        i1 -= 1
    elif(parsed[i2 - 1][1] == "JJ" or parsed[i2 - 1][1] == "DT"):
        sent.insert(i1, sent[i2 - 1])
        sent.pop(i2)
        i1 += 1
    return sent, i1, i2


def turn_to_passive(sent):
    i1 = 0
    foundI1 = False
    i2 = 0
    foundI2 = False
    theVerb = 0
    text = nltk.tokenize.word_tokenize(sent)
    parsed = nltk.pos_tag(text)
    for word in parsed:
        if (word[1] == "VBD" or word[1] == "VB" or word[1] == "VBP"):
            theVerb = word[0]
        if (foundI1 == False and (word[1] == "NN" or word[1] == "PRP")):
            foundI1 = True
        elif (foundI2 == False and (word[1] == "NN" or word[1] == "PRP")):
            foundI2 = True
        i1 += (foundI1 == False)
        i2 += (foundI2 == False)

    newSent, i1, i2 = switch_JJ(sent.split(), i1, i2)
    #print nltk.tokenize.word_tokenize(nltk.pos_tag())
    newSent[newSent.index(theVerb)] = get_word_past_participle(theVerb)
    a = newSent[i1]
    newSent[i1] = newSent[i2]
    newSent[i2] = a
    newSent.insert(i1 + 1, "was")
    newSent.insert(newSent.index(get_word_past_participle(theVerb)) + 1, "by")
    return make_string(newSent)


def main():
    a = {
    'a': 'value',
    'another': 'value', }
    print a["a"]
    sent = "an I ate apple"
    print "Your sentence is:        " + sent
    print "The passive sentence is:       " + turn_to_passive(sent)
    text = nltk.tokenize.word_tokenize(sent)
    parsed = nltk.pos_tag(text)
    print parsed
    print en.sentence.tag(sent)

    """
    with open("newSent.txt", 'w') as newF:
        with open("sentences.txt", 'r') as f:
            sentence = f.read()
        f.close()
        sentences = sentence.split('\n')
        for sent in sentences:
            print(change_sentence(sent))
            newF.write(change_sentence(sent) + "\n")

    newF.close()"""


if __name__ == '__main__':
    main()