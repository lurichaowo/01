import csv

def de_alpha(w): # return word w/o punctuation
    '''
        input: word
        output: loops through to return an all alpha of word
    '''
    result=""
    for l in w:
        if l.isalpha() or l == " ":
            result = result + l
    return result.split()

def iindex(s):
    '''
        input: csv text file
        mid: --> removes non-alpha char
            --> run through each last statement to search for a word or phrase
        output: dict of words with execnums it's part of
    '''
    f = open(s)
    csv_reader = csv.reader(f)
    l = []
    for line in csv_reader:
        l.append(line)
    f.close()
    d = {}
    for x in l:
        statement = de_alpha(x[8])
        for w in statement:
            d.setdefault(w, [])
            if x[0] not in d[w]: 
                d[w].append(x[0])
    return d

def main(l):
    '''
        inpute: a word
        output: list of execution #s with that word.
    '''
    for x in execnums:
        if x == l:
            return execnums[x]
    


execnums = iindex("offenders-clean.csv")
search = main("sorry")
print(search)
