'''
Problem description:

Given an array (arr) as an argument complete the function countSmileys that should return 
the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]

Example:

countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
'''

def count_smileys(arr):
    c = 0
    if len(arr) == 0:
        return 0
    for e in arr:
        if len(e) == 2:
            if (e[-1] in ')D') and e[0] in ':;':
                c += 1
        elif len(e) == 3:
            if (e[-1] in ')D') and (e[0] in ':;') and (e[1] in '-~'):
                c += 1
        else:
            continue
    return c
