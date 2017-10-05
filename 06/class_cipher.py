import math
real_stats = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]

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
    
def build_frequency_vector(s):
    # count the letters in the string
    spaces = s.count(' ')
    num_letters = len(s) - spaces
    v=[]
    for letter in "abcdefghijklmnopqrstuvwxyz":
        v.append(s.count(letter) / num_letters)

    return v

def print_vector_table(v):
    s="abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        print(s[i]," : ",v[i])

def decode(s):
    l = []
    i = 1
    while i < 26:
        encoded = encode_string(s, i)
        l.append(encoded)
        i = i + 1
    f = []
    for sent in l:
        f.append(build_frequency_vector(sent))
    d = []
    for freq in f:
        d.append(distance(real_stats, freq))

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
    

s = "this is a longer sentence with more letters so hopefully it will be closer to the real distribution"

r = encode_string(s,3)

print(s)
print(r)

f = build_frequency_vector(s)

print(distance(real_stats,f))
print("\n--------------------------------------\n")
f = build_frequency_vector(r)
print(distance(real_stats,f))
print("\n--------------------------------------\n")
print(decode(s))
