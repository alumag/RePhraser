from RePhraser import fix_spelling

"""
EXAMPLE #1
this feature work only on python 2.7
"""

sentence = "hello world, I didn't use my computre."
fixed = fix_spelling.fix_spelling(sent=sentence)
print(sentence+"\n"+fixed)
