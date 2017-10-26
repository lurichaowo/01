#!/bin/python3

import sys           
#cases: 
# 1 LB (uh)
# no spaces 
#   if already happy (h)
#   otherwise (uh)
# 1 or more spaces (we can arbitraryily rearrange the list)
#   if there is 2 or more of each char (h)
#   otherwise (uh)
    
Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip()) #board size 7
    b = input().strip() #color of lady bugs/cells 'BYR_BYR'
    #check to see if playable
    #see if any ladybugs are unhappy
    #all happy = NO
    #unhappy + movable = YES
    if not(checker(b)):
        print("NO")
    else:
        print("YES")
        
    
def checker(b):
    count = counter(b)
    if not("_" in b):
        for num, i in enumerate(b):
            if not(is_happy(b, num)):
                return False
        for num in count:
            if (num < 2)L
                return False
    elif ("_" in b):
        for num in count:
            if (num < 2):
                return False
    
        
def counter(b):
    list = []
    spaces = s.count('_')
    num_letters = len(s) - spaces
    v=[]
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        v.append(s.count(letter) / num_letters)
    return v
    
def is_happy(b, cellnum):
    if cellnum != len(b):
        if (b[cellnum] == b[cellnum+1]):
            return True
        else:
            return False
    elif cellnum == len(b):
        if (b[cellnum] == b[cellnum -1]):
            return True
        else:
            return False
