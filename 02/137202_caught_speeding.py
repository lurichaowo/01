def caught_speeding(speed, is_birthday):
  i = 0 
  if (is_birthday == False):
    if (speed <= 60):
      return i
    if (speed > 60 and speed < 81):
      i = 1
      return i
    if (speed > 80):
      i = 2
      return i
  if (is_birthday):
    if (speed <= 65):
      return i
    if (speed > 65 and speed < 86):
      i = 1
      return i
    if (speed > 85):
      i = 2
      return i