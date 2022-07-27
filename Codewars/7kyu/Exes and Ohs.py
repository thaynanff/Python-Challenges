'''
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

'''

def xo(s):
    return True if s.lower().count('x') == s.lower().count('o') or s.lower().count('x') == s.lower().count('o') == 0 else False