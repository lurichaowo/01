def encode_letter(c, r):
    c = c.lower()
    num = ord(c)
    if (int(r) > 26):
        r = int(r) % 26
    if (int(r) < 0):
        r = 26 +int(r)
    if (num + int(r) > 122): # checks if ord num passes ord of Z
        diff = 122 - int(num) #finds remaining amount till ord(z)
        r = int(r) - diff 
        num = 96 + r #restart from 97
    else:
        num = num + int(r) #else just do normally
    return chr(num)

string = input("enter a letter: ")
number = input("enter a number: ")
print(encode_letter(string, number))

