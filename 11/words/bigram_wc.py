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

def binary_listify(wordlist):
    d={}
    for index,w in enumerate(wordlist):
        if index < len(wordlist) -2:
            new_word = w + " " + wordlist[index+1]
            d.setdefault(new_word,[])
            if index == len(wordlist)-2:
                word = d[new_word]
                d[new_word] = (word[:])
            else:
                d[new_word].append(wordlist[index+2])
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
    d2 = binary_listify(l)
    return d2



d = main("hamlet.txt")
print(d)
