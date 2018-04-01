from RePhraser.synonym import synonym

from nltk import tokenize, tag

synonym_db = synonym()

"""
EXAMPLE #1
In this example we will try to find a synonym to the word "shiny"
"""
synonym = synonym_db.getSynonym(word="shiny")
print("Example #1: ", "shiny =", synonym)
del synonym


"""
EXAMPLE #2
In this example we will run over a sentence and find a synonym for only relevant words
"""
sentence = "I can climb the tree very fast"
text = tokenize.word_tokenize(sentence)

for cur in tag.pos_tag(text):
    if cur[1] == "RB" or cur[1] == "VBP" or cur[1] == "VB" or cur[1] == "CC" or cur[1] == "PRT":
        synonym = synonym_db.getSynonym(word=cur[0])
        if not synonym == cur[0].upper():  # sometimes NLTK will find the same word, just in uppercase
            if '_' in synonym: synonym = synonym.replace("_", " ")
            sentence = sentence.replace(cur[0], synonym)

print("Example #2\n", "I can climb the tree very fast\n", sentence)
