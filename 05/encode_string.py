def encode_letter(c, r):
    c = c.lower()
    num = ord(c)
    if (num + int(r) > 122): # checks if ord num passes ord of Z
        diff = 122 - int(num) #finds remaining amount till ord(z)
        r = int(r) - diff 
        num = 96 + r #restart from 97
    else:
        num = num + int(r) #else just do normally
    return chr(num)

def encode_upper_letter(c, r):
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
#string = input("enter a string: ")
number = input("enter a number: ")
print(encode_string('Hello Name is Bob', number))
