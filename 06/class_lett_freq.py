def rotate_char(c, r):
    v = ord(c)
    v = v - 97 #shift downback 'a' to 0
    v = (v + r)%26
    v = v +97
    result = chr(v)
    print(result)
    
def encode_string(s, r):
    result = ''
    for letter in s:
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            letter = rotate_char(letter, r)
        result = result + letter
    return result

def distance(l1, l2):
    if len(l1)>len(l2):
        length = len(l2)
        for i in range(length):
            sum = sum + (l1(i) - l2(i))*(l1(i) - l2(i))
        print(sum)
        
def build_freq_vecotr(s):
    spaces = s.count(' ')
    num_letters = len(s) - spaces
    v =[]
    for letter in  'abcdefghijklmnopqrstuvwxyz':
        v.append(s.count(letter) / num_letters)
    return v
    
def print_vector_table(v):
    s = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(26):
        print (s[i], ": " , v[i])

r = encode_string("this is a string", 13)
print(r)
r = encode_string("this is a string", 13)
print(r)
print(distance((l1,l2)))