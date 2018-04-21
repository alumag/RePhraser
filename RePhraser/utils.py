import string


def no_punctuation(text):
    """Return the string with no punctuation."""
    return text.translate(None, string.punctuation)
