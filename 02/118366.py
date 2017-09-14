def string_splosion(str):
  length = len(str)
  string = ''
  i = 1
  if (length == 0):
    return string
  while (i-1 <= length):
    string = string + str[:i-1]
    i = i +1
  return string