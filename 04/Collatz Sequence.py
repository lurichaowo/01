def user_input():
    n = int(input('enter an integer: ')) #userinput number
    print(n) #print init num
    looper(n) # enter looper
        
def looper(num):
    if (num != 1): #stop looper if num =1
        num = collatz(num) # enter collarz
        looper(num)
    else:
        return num
    
def collatz(number):
    n = number
    if (number%2 == 0): # even num
        n = number//2
        print(number // 2)
        return n
    elif (number%2 == 1): #odd num
        n = (number *3) +1
        print((number *3) +1)
        return n
    
user_input()