"""A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses 
the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation."""


import string

# The logic used was comparing each lower case letter of the alphabet with each lower case letter of the given phrase.
# If the alphabet letter is in the list of letters in the phrase, then the code gives it a True value, otherwise, it gives it False.
# Thereafter, if all the values in the list are True, the function returns a True.

def is_pangram(s):
    return all([True if l in s.lower() else False for l in string.ascii_lowercase])