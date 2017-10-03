frequency = [12.02, 9.10, 8.12, 7.68, 7.31, 6.95, 6.28, 6.02,
             5.92, 4.32, 3.98, 2.88, 2.71, 2.61, 2.30, 2.11, 2.09, 2.03,
             1.82, 1.49, 1.11, 0.69, 0.17, 0.11, 0.10, 0.07]

alphabet = 'abcdefghijklmnopqrstuvwxyz'

orig_frequency = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                 0.0, 0.0, 0.0, 0.0]

new_frequency2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                 0.0, 0.0, 0.0, 0.0]

letter_count = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                 0.0, 0.0, 0.0, 0.0]

string_list = []

def main():
    string = input("enter a string: ")
    full_encodes(string)
    find_frequency(string_list[0], orig_frequency)
    
    
    
def find_frequency(string1, freq_list):
    for alpha in alphabet:
        for letter in string1: #compare letters in string and alphabet to get number of each letter
            if alpha == letter:
                letter_count[alphabet.index(letter)] = letter_count[alphabet.index(letter)] + 1.0
                #increment that value
    return_frequency(letter_count, freq_list) #return frequency of each letter
    '''for i, num in enumerate(letter_count): #reset letter count
        letter_count[i] = 0.0
    for alpha in alphabet:
        for letter in string2:
            if alpha == letter:
                letter_count[alphabet.index(letter)] = letter_count[alphabet.index(letter)] + 1.0
    return_frequency(letter_count, new_frequency2)'''
    

def return_frequency(l_count, freq_list):
    sum = 0.0
    for i in l_count: #find sum
        sum = sum + i
    for i, num in enumerate(l_count): #set frequency of each list
        freq_list[int(i)] = num/sum   

def find_distance(frequency, new_frequency):
    inside_sum = 0.0
    i = 0
    while i < len(list1): #assuming list1 length = list2 length
        inside_sum = inside_sum + ((list1[i] - list2[i]) ** 2) #the sum of inside of square root
        i = i + 1
    distance = inside_sum ** (0.5)
    return distance

'''full encode'''

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
        string_list.append(new_string)
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




find_frequency('hello', 'hi')

#when given 2 lists of equal length
#find distance using distance formula using each point btwn lists
#


