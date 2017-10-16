# m = num of apples
# n = num of oranges
# -d = left of tree
# d = right of tree
# s, t = width of house
# a = apple tree loc
# b = orange tree loc

#!/bin/python3

import sys

def on_house(point):
    if point >= s and point <= t:
        return True
    else:
        return False

def main():
    is_on_house = [0,0]
    for d in apple:
        if (on_house(a + d)):
            is_on_house[0] += 1
    for d in orange:
        if(on_house(b + d)):
            is_on_house[1] += 1
    print(is_on_house[0])
    print(is_on_house[1])
        
s,t = input().strip().split(' ')
s,t = [int(s),int(t)] #dimenion of house
a,b = input().strip().split(' ')
a,b = [int(a),int(b)] #loc of trees
m,n = input().strip().split(' ')
m,n = [int(m),int(n)] # of fruits
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')] # apple dis from tree
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')] # orange dis from tree

main()