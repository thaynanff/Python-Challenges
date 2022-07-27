'''
Problem description:

Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,

each taken only once - coming from s1 or s2.

Exemples:

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
'''

def longest(s1, s2):
    temp = []
    for l in s1:
        if l not in temp:
            temp.append(l)
    for l in s2:
        if l not in temp:
            temp.append(l) 
    return ''.join(sorted(temp))
