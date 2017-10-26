def rle(s):
    encoded = []
    while len(s) >1:
        runlen = 1
        runchar = s[0]
        while runlen < len(s) and s[runlen] == runchar:
            runlen = runlen + 1
        if runlen> 1:
            encoded.append(runlen)
        encoded.append(runchar)
        s=s[runlen:]
    return encoded

print(rle("aaaaaaaaaaabbbbbbbbbbbcddddddeeeee"))