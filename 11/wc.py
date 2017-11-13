def remove_non_alpha(w): # return word w/o punctuation
    '''
        input: word
        output: loops through to return an all alpha of word
    '''
    result=""
    for l in w:
        if l.isalpha():
            result = result + l
    return result

def count(wordlist): # counts number of words
    '''
        input: list of word
        mid: if word doesnt exist in dict, creates new key with value of 0 (then add 1)
        output: returns dict of words and count of word
    '''
    d={}
    for w in wordlist:
        d.setdefault(w,0)
        d[w] = d[w] + 1
    return d

def main(f):
    '''
        input: string represent a file
        outout: a dic with keys for words and count of word
    '''
    txt = open(f).read()
    l=[]
    for word in txt.split():
        word = word.lower()
        word = remove_non_alpha(word)
        l.append(word)
    d = count(l)
    return d


d = main("hamlet.txt")
v = list(d.values())
print(d)
v.sort()
print(v)

d2 = main("sonnets.txt")
v2 = list(d2.values())
print(d2)
v2.sort()
print(v2)
for l in d2:
    if (d2[l] > 150):
        print(l, " : ", d2[l])
l = [x for x in range(10)]
print(l)
s = [x**2 for x in range(10)]
print(s)

d = {'a' : 5, 'b': 10, 'c': 20}
v3 = [v for k, v in d]
print(v3)