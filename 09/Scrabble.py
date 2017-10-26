dict = {"aeioulnrst":"1", 
        "dg":"2", 
        "bcmp":"3", 
        "fhvwy":"4",
        "k":"5",
        "kx":"8",
        "qz":"10"}

def score(w):
  score = 0
  w = w.lower()
  for i in w:
    for key,val in dict.items():
      if i in key:
        score += int(val)
  return score

print(score("hello"))
print(score("computer"))
print(score("ZeBra"))
print(score("hypocriTe"))
print(score("Supercalifragilisticexpialidocious"))