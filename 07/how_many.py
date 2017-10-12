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

def main():
    str = input("Enter something (try not to enter 2 of the same number of letters as the mode. It wasn't part of the assignemnt!): ")
    print(mode(str))

main()