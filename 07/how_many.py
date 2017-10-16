import random

def freq(n, i):
    count = 0
    for letter in i:
        if letter == n:
            count = count + 1
    return count

def min(i):
    lower = i[0]
    lowest = 0
    while lowest < len(i):
        if lowest <= len(i):
            if (i[lowest] < lower):
                lower = i[lowest]
                lowest = lowest + 1
            else:
                lowest = lowest + 1
    return lower
         
def max(i):
    higher = i[0]
    highest = 0
    highnum = 0
    while highest < len(i):
        if highest <= len(i):
            if (i[highest] > higher):
                higher = i[highest]
                highnum = highest
                highest = highest + 1
            else:
                highest = highest + 1
    return highnum

def mode(i):
    v = []
    for letter in  'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        v.append(freq(letter, i))
    m = max(v)
    return i[m]
    
'''i = [2,4,5,79,10,1]
print(min(i))
print(max(i))'''

def model(l):
    mode_so_far = freq(l[0], l)
    mode_index = 0
    for index, value in enumerate(l):
        next_freq = freq(value,l)
        if (next_freq > mode_so_far):
            mode_so_far = next_freq
            mode_index = index
    return l[mode_index]

def mode2(l):
    buckets = []
    for i in range(100):
        buckets.append(0)
    for item in l:
        buckets[item] = buckets[item] + 1
    max_index = 0
    for index, item in enumerate(buckets):
        if (buckets(index) > buckets(max_index)):
            max_index = index
    return max_index

def build_random_list(items):
    l = []
    i = 0
    for i in range(items):
        l.append(random.randrange(10))
    return l

def main():
    str = input("Enter something (try not to enter 2 of the same number of letters as the mode. It wasn't part of the assignemnt!): ")
    print(mode(str))
    i = [1,4,1,6,1,2,7,1,3,1,1,7]
    print(model(i))
    l = build_random_list(15)
    print(l)
    print(mode(l))
    print(mode2(l))

main()
