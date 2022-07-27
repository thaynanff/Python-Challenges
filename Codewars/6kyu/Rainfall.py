'''
Problem description:

dataand data1 are two strings with rainfall records of a few cities for months from January 
to December. The records of towns are separated by \n. The name of each town is followed by : .

data and towns can be seen in "Your Test Cases:".

Task:
function: mean(town, strng) should return the average of rainfall for the city town and the 
strng data or data1 (In R and Julia this function is called avg).
function: variance(town, strng) should return the variance of rainfall for the city town and 
the strng data or data1.

Examples:

mean("London", data), 51.19(9999999999996) 
variance("London", data), 57.42(833333333374)
'''

import re

def mean(town, strng):
    try:
        i = re.split("[:, \n]", strng).index(town)
        s = []
        for e in range(i+2, i+25, 2):
            s.append(float(re.split("[:, \n]", strng)[e]))
        return sum(s)/12
    except:
        return -1


def variance(town, strng):
    try:
        if re.search(town, strng) == None:
            return -1
        i = re.split("[:, \n]", strng).index(town)
        s = []
        for e in range(i+2, i+25, 2):
            s.append(float(re.split("[:, \n]", strng)[e]))
        var = [(sum(s)/12) - x for x in s]
        doubled = []
        for e in var:
            doubled.append(e**2) 
        return sum(doubled)/12
    except:
        return -1
