def lone_sum(a, b, c):
  i = 0
  if (a == b and a == c):
    return i
  if (a != b and b ==c):
    i = a 
    return i
  if (b != a and a == c):
    i = b
    return i
  if (c != a and a ==b):
    i = c
    return i
  if (a != b and b != c):
    i = a + b + c
    return i
