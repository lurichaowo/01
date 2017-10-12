import math

v = []

def main():
    f = input("enter the file name: ")
    num = input("enter a number to rotate it by: ")
    flz = open(f)
    read = flz.read()
    v = create_freq_vector(read)
    print(v)
    r_str = encode_string(read, int(num))
    print(r_str)
    d_str = decode(read)
    print(d_str)
    
def rotate_char(c,r):
    """
    Rotates character c by amount r. Wraps if past z
    """
    v = ord(c)
    v = v - 97 # shift down so that 'a' is 0
    v = (v + r)%26
    v = v + 97 # shift back up so that 'a' is 97
    result = chr(v)
    return result

def encode_string(s,r):
    """
    rotate a string (lower case letters only)
    """
    result = ""
    for letter in s:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            letter = rotate_char(letter,r)
        result = result + letter
    return result

def create_freq_vector(s): 
    str = s.lower()
    spaces = str.count(' ')
    num_letters = len(str) - spaces
    v =[]
    for letter in  'abcdefghijklmnopqrstuvwxyz':
        v.append(str.count(letter) / num_letters)
    return v

def distance(l1,l2):
    """
    Euclidean distance between l1 and l2. If the lists are of 
    different lengths, go to the lenght of the shorter one
    """
    length = len(l1)
    if length>len(l2):
        length = len(l2)
    sum=0
    for i in range(length):
        sum = sum + (l1[i]-l2[i])*(l1[i]-l2[i])
    d = math.sqrt(sum)
    return d

def decode(s):
    l = []
    i = 0
    while i < 26:
        encoded = encode_string(s, i)
        l.append(encoded)
        i = i + 1
    f = []
    for sent in l:
        f.append(create_freq_vector(sent))
    d = []
    for freq in f:
        d.append(distance(v, freq))
    print(d)
    lower = d[0]
    count = 1
    lowest = 0
    while count < len(d):
        if d[count] < lower:
            lower = d[count]
            lowest = count
            count = count + 1
        else:
            count = count + 1
            pass
    result = l[lowest]
    return result

main()