def full_encodes(s):
    i = 0
    new_string = ''
    while i < 26: #26 characters in alphabet duh
        for letter in s: #runs through each char of string
            if (letter == ' '):
                new_string = new_string + ' '
            else:
                new_string = new_string + encode_letter(letter, i) #encodes each char with the cooresponding i value
        print(new_string) #prints rotated with respect to i
        new_string = '' #reset new_string
        i = i + 1 #i++

def encode_letter(c, r):
    c = c.lower()
    num = ord(c)
    if (num + int(r) > 122): # checks if ord num passes ord of Z
        diff = 122 - int(num) #finds remaining amount till ord(z)
        r = int(r) - diff 
        num = 96 + r #restart from 96
    else:
        num = num + int(r) #else just do normally
    return chr(num)


string = input("enter a string: ")
full_encodes(string)
