def piglatin(str):
    str = str.lower()
    string = ''
    vowelc = is_vowel(str[0])
    if (vowelc):
        string = str+ 'ay'
        return string
    elif (vowelc == False):
        string = str[1:] + str[0] + 'ay'
        return string
        
        
def is_vowel(a):
    if (a == 'a' or a == 'e' or a=='i' or a=='o' or a=='u'):
        return True
    else:
        return False
    
print(piglatin('HIPPO'))
print(piglatin('aunt'))