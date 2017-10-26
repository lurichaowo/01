#!/bin/python3

import sys           

    
Q = int(input().strip())
list = []
for a0 in range(Q):
    n = int(input().strip()) #board size 7
    b = input().strip() #color of lady bugs/cells 'BYR_BYR'
    #check to see if playable
    #see if any ladybugs are unhappy
    #all happy = NO
    #unhappy + movable = YES
