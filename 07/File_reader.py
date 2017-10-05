#you can read a file into a big string using read
f = open("data.dat")
#f is a file object and we can read from it
s = f.read()
print(s)

#we can do the same thing by chaining the read into the open
s2 = open("data.dat").read()
print(s2)
#once you read it you have to reopen it
#once its a string we can do things with it
s3 = open("data.dat").read()
l = s3.split() # split on white space
l2 = s3.split("\n") #split on new line
print(l)
print(l2)

#if we want to split on lines, we can use readlines()
l3 = open("data.dat").readlines()
print(l3)

#or we can read one line at a time with readlines()
f = open("data.dat")
for line in f:
    print(line)

#or just go back to read each char at a time
s = open("data.dat").read()
for c in s:
    print(c)