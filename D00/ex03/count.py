#!/usr/bin/env python
import sys
PONCT = """!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""


def text_analyzer(txt=''):
    """This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text."""

    if not txt:
        print("What is the text to analyse?")
        txt = input()
    upper = sum([1 if c.isupper() else 0 for c in txt])
    lower = sum([1 if c.islower() else 0 for c in txt])
    spaces = sum([1 if c.isspace() else 0 for c in txt])
    ponct = sum([1 if c in PONCT else 0 for c in txt])
    print(
        """The text contains {} characters:
        - {} upper letters
        - {} lower letters
        - {} punctuation marks
        - {} spaces""".format(len(txt), upper, lower, ponct, spaces))


def text_analyzer_tests():
    text_analyzer("""Python 2.0, released 2000, introduced \
features like List comprehensions and a garbage collection \
system capable of collecting reference cycles.""")
    text_analyzer("""Python is an interpreted, high-level, \
general-purpose programming language. Created by Guido van \
Rossum and first released in 1991, Python's design philosophy \
emphasizes code readability with its notable use of significant \
whitespace.""")
    print(text_analyzer.__doc__)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == 'TEST':
            text_analyzer_tests()
        else:
            text_analyzer(sys.argv[1])
    else:
        text_analyzer()
