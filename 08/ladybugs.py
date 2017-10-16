#!/bin/python3

import sys
    
def is_happy(board, cell):
    if cell == 0:
        if board[cell] == board[cell + 1]:
            return True
        else:
            return False
    if (cell == len(board)):
        if board[cell] == board[cell-1]:
            return True
        else:
            return False
    if (cell != 0 and cell != len(board)):
        if (board[cell] == board[cell+1] or board[cell] == board[cell-1]):
            return True
        else:
            return False
    
def search_for_empty(b, unhappy):
    for space in b:
        if space == '_':
            space = unhappy
            unhappy = '_'
        
def can_move(b):
    for bug, cell in b:
        if not is_happy(b, cell):
            print("YES")
            search_for_empty(b, bug)   
            
Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip()) #board size 7
    b = input().strip() #color of lady bugs/cells 'BYR_BYR'
    can_move(b)