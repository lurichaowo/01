def fizzbuzz():
    '''
    using max will print "fizzbuzz" before the actual range code for some reason :(
    '''
    #max = 101
    i = 1
    f = 'fizz'
    b = 'buzz'
    string = ''
    for i in range(1, 101): #for i in range(max):
        if (i%3 == 0 or i%5 == 0):
            if (i%3 == 0):
                string = string + f
            if (i%5 ==0):
                string = string + b
            print(string)
        else:
            string = i
            print(string)
        i = i + 1
        string = ''

fizzbuzz()