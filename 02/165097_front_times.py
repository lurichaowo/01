def front_times(str, n):
  front = str[0:3]
  i = n
  string = ''
#string = i * front
  if len(str) ==  0:
    return string
  else :
    while i > 0 :
      string = string + front
      i = i -1
  return string
