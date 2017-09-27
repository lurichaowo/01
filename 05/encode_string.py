def encode_letter(c, r): # rotates lower case letters
    c = c.lower()
    num = ord(c)
    if (num + int(r) > 122): # checks if ord num passes ord of Z
        diff = 122 - int(num) #finds remaining amount till ord(z)
        r = int(r) - diff 
        num = 96 + r #restart from 97
    else:
        num = num + int(r) #else just do normally
    return chr(num)

def encode_upper_letter(c, r): #rotates upper case letters
    num = ord(c)
    if (num + int(r) > 90): # checks if ord num passes ord of Z
        diff = 90 - int(num) #finds remaining amount till ord(z)
        r = int(r) - diff 
        num = 64 + r #restart from 97
    else:
        num = num + int(r) #else just do normally
    return chr(num)

def encode_string(s, r):
    new_list = s.split() # split the string
    new_string = ''
    for word in new_list: # call each word in listed string
        string = ''
        for letter in word: # call each letter in word
            if letter.isupper(): # check if letter is caps
                new_letter = encode_upper_letter(letter, r) # if is cap then call encode_upper_letter
                string = string + new_letter
            else: # if isn't cap call encode_letter
                new_letter = encode_letter(letter, r)
                string = string + new_letter
        new_string = new_string + string + ' '
        string = ''
    return new_string # print string 

''' --> you are a dum dum you could've just used a if (letter == ' ')
    --> yeah i noticed after I finished the full encode.
    =========================different and probably more easily followed code===========================
    def encode_string(s, r):
    new_string = ''
    for letter in s:
        if letter.isupper(): # check if letter is caps
            new_letter = encode_upper_letter(letter, r) # if is cap then call encode_upper_letter
            new_string = new_string + new_letter
        elif letter == ' ': #checks for space
            new_string = new_string + ' '
        elif letter.isupper() == False: # if isn't cap call encode_letter
            new_letter = encode_letter(letter, r)
            new_string = new_string + new_letter

    return new_string # print string  '''

#string = input("enter a string: ")
number = input("enter a number: ")
print(encode_string('Hello Name is Bob', number))

