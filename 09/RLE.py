def encode(s):
  s = despace(s)
  listed = []
  count = 0
  for num, i in enumerate(s):
    if s[num] == i:
      count += 1
      if (num == len(s) - 1 or s[num + 1] != i):
        listed.append(count)
        listed.append(i)
        count = 0
  return listed
      
def despace(s): # get rid of spaces
  s = s.split()
  new = ""
  for i in s:
    new = new + i
  return new
  
print(encode("aaaaa"))
print(encode("aabcccdeeeeaaaa"))
print(encode("asjdsajsnkkjajddjqwejqqppqpqpqposoc,zxmc ,tn,eeiixzx"))
print(encode(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"))
print(encode(".................,.,.,.,.,.,.,.,.,.    .,.,.,..32.4.141@@@@w$%^&*"))
    