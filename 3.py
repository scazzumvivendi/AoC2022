result = 0
result2 = 0
# Intersezione di array
with open("3.txt", 'r') as f:
  lines = [line.rstrip() for line in f]
  for l in lines:
    # FIRST RESULT
    sacks = l.rstrip();
    lsack, rsack = sacks[:int(len(sacks)/2)], sacks[int(len(sacks)/2):]
    intersection = list(set(lsack).intersection(rsack))
    char_value = ord(intersection[0])-96;
    if(char_value < 1):
      char_value = ord(intersection[0])-65+27;
    result += char_value;
  # SECOND RESULT
  # Raggruppare elementi in tre
  three_groups = [lines[i:i + 3] for i in range(0, len(lines), 3)]
  for three_group in three_groups:
    # Intersezione di array
    intersection = list(set(three_group[0]).intersection(three_group[1]).intersection(three_group[2]))
    char_value = ord(intersection[0])-96;
    if(char_value < 1):
      char_value = ord(intersection[0])-65+27;
    result2 += char_value;
print(f'FIRST RESULT {result}')
print(f'SECOND RESULT {result2}')
