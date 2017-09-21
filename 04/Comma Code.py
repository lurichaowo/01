def de_comma(list):
    string = ''
    for word in list:
        if (list.index(word) == len(list)-1): #last word ', and' condition
            string = string + ', and ' + word
        elif (list.index(word) == 0): #so beginning doesn't have ', '
            string = string + word
        else: #adding add
            string = string + ', ' + word
    return string
            
list = ['hi', 'my', 'name', 'is', 'bob']

print(de_comma(list))