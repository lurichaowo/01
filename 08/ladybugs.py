#!/bin/python3

import sys
    
def is_happy(b, cellnum):
    if (cellnum != 0 and cellnum != len(b)-1):
        if (b[cellnum+1] is b[cellnum] or b[cellnum-1] is b[cellnum]):
            return True
    elif (cellnum == 0 and b[cellnum+1] is b[cellnum]):
        return True
    elif (cellnum == len(b) and b[cellnum-1] is b[cellnum]):
        return True
    else:
        return False
    
def poss(b, cellnum):
    for i, num in enumerate(b):
        if (i != cellnum and b[cellnum] == b[i]):
            return True
   
def playable(b):
    playable = True
    if (b.count("_") == len(b)):
        return True
    for i, num in enumerate(b):
        if num != "_":
            if (b.count(num) == 1):
                return False
            elif not(is_happy(b, i)) and ("_" in b) and (poss(b, i)):
                playable = True
            elif not(is_happy(b,i)) and not(poss(b,i)):
                playable = False
            elif is_happy(b, i) and i == len(b):
                playable = True 
    return playable
   
Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip()) # number of cells
    b = input().strip() # color of bugs
    if playable(b):
        print("YES")
    elif not(playable(b)):
        print("NO")