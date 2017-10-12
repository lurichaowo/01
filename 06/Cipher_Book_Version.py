import math

def create_freq_vector(s):
    spaces = s.count(' ')
    num_letters = len(s) - spaces
    v =[]
    for letter in  'abcdefghijklmnopqrstuvwxyz':
        v.append(s.count(letter) / num_letters)
    return v

drac = open('data.dat')
drac.readlines()
