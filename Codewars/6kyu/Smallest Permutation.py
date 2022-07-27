'''
Given a number, find the permutation with the smallest absolute value (no leading zeros).

-20 => -20
-32 => -23
0 => 0
10 => 10
29394 => 23499

'''

def min_permutation(n):
    if n <0:
        y = [y for y in str(-n)]
    else: 
        y = [y for y in str(n)]
    
    y = sorted(y)
    
    if '0' in y:
        count0 = y.count('0')
        for x in range(0,count0):
            y.remove('0')
        y.insert(1,'0'*count0)
    
    if n <0:
        return int(''.join(y))*(-1)
    else:
        return int(''.join(y))
