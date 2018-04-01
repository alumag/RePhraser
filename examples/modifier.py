from RePhraser import modifier

from nltk import tokenize, tag

modifier_db = modifier.Modifier()

"""
EXAMPLE #1
In this example we will find a modifier for the word "Obama"
"""
mod = modifier_db.find(word="Obama")
print("Example #1:\nObama:", mod)
del mod

"""
Example #2
Find a modifier to a word in a sentence
"""
sentence = "Obama ate an apple"

text = tokenize.word_tokenize(sentence)
new_sentence = sentence

for cur in tag.pos_tag(text):
    if cur[1] == "NN" or cur[1] == "NNP" or cur[1] == "RPR":
        mod = modifier_db.find(cur[0])
        if mod:
            rep = cur[0] + " (" + mod + ")"
            new_sentence = new_sentence.replace(cur[0], rep)

print("Example #2\n", sentence, "\n", new_sentence)
