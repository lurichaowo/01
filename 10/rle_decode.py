def decode(r):
    s = ''
    for index,al in enumerate(r):
        if al.isalpha() and index != 0:
            if not r[index-1].isalpha():
                s = s + al * int(r[index-1])
            elif r[index-1].isalpha():
                s = s + al
        elif al.isalpha() and index ==0:
            s = s + al
    return s

a = ["b", "5", "c","e"]
print(decode(a))
            