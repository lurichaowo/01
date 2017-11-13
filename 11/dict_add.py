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

def listify(wordlist): # counts number of words
    '''
        input: list of word
        mid: if word doesnt exist in dict, creates new key with value of 0 (then add 1)
        output: returns dict of words and count of word
    '''
    d={}
    for index,w in enumerate(wordlist):
        d.setdefault(w,[])
        if index == len(wordlist)-1:
            word = d[w]
            d[w] = (word[:])
        else:
            d[w].append(wordlist[index+1])
    '''
    for i in range(',len(wordlist)):
        w1 = wordlist[i-1]
        w2 = wordlist[i]
        d.setdefault(w1, [])
        d[w1].append(w2)
    '''
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
    d = listify(l)
    return d



d = main("hamlet.txt")
print(d)