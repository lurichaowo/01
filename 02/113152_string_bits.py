def string_bits(str):
  i = 1
  string = ''
  while i <= len(str):
    string = string + str[i-1]
    i = i + 2
  return string 

# return str[::2]
