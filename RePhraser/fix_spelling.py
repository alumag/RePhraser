import en as en
import string

__author__ = 'User'


"""
"""
def clean_sent(word):
    word = word.lower()
    for ch in string.punctuation:
        word = word.replace(ch, '')
    return word


def find_right_fix(word):
    contained_punctuation = 0
    place = -1
    i = 0
    for leter in word:  # It doesn't fix words like: diddn't- it lives theme the same
        if string.punctuation.__contains__(leter):
            contained_punctuation += 1
            place = i
        i += 1
    if (contained_punctuation > 1 or place != len(word) - 1):
        return word
    clean_word = clean_sent(word)
    options = en.spelling.suggest(clean_word)
    word = clean_word
    if not options.__contains__(clean_word):  # So it will change only words that need to be changed (it had a problem with compuetr.)
        word = options[0]
    return word


def fix_spelling(sent):
    newSent = ""
    i = 0
    for word in sent.split():
        punctuation = word.lower().replace(clean_sent(word), "")
        newSent += find_right_fix(word)
        if len(punctuation) == 1:
            newSent += punctuation
        i += 1
        if (i < len(sent.split())):  # So we won't have a spare " "
            newSent += " "
    return newSent


def main():
    print fix_spelling("hello world, I didn't use my computre.")

if __name__ == '__main__':
    main()
