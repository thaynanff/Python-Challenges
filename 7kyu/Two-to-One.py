def longest(s1, s2):
    temp = []
    for l in s1:
        if l not in temp:
            temp.append(l)
    for l in s2:
        if l not in temp:
            temp.append(l) 
    return ''.join(sorted(temp))