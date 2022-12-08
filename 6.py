result = 0

def check(char_arr):
  return len(set(char_arr)) == len(char_arr)

with open("6.txt", 'r') as f:
  lines = [line.rstrip() for line in f]
  found_first = False
  for i, val in enumerate(lines[0]):
    chars_four = lines[0][i:i+4]
    chars_fourteen = lines[0][i:i+14]
    if check(chars_four) and found_first == False:
      result = i+4
      found_first = True
      print(result)
    if check(chars_fourteen):
      result = i+14
      print(result)
      break
