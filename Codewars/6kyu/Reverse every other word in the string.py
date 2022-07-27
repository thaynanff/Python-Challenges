'''
Problem desciption:

Reverse every other word in a given string, then return the string. Throw away any leading 
or trailing whitespace, while ensuring there is exactly one space between each word. 
Punctuation marks should be treated as if they are a part of the word in this kata.
'''

def reverse_alternate(string):
    return ' '.join(e[::-1] if p % 2 else e for p, e in enumerate(string.split()))