map_theirs = {"A": 1, "B": 2, "C": 3}
map_mine = {"X": 1, "Y": 2, "Z": 3}
WIN = 6
DRAW = 3
LOSE = 0
beats = {1:3, 2:1, 3:2}
beaten = {1:2, 2:3, 3:1}
map_result = {"X": 0, "Y": 3, "Z": 6}

f = open("2.txt")
result = 0
result2 = 0
for l in f:
  content = l.rstrip().split(" ")
  result += map_mine[content[1]]
  if (beats[map_mine[content[1]]] == map_theirs[content[0]]):
    result += WIN
  elif (map_mine[content[1]] == map_theirs[content[0]]):
    result += DRAW

  result2 += map_result[content[1]]
  print(str(content[0]) +" "+ str(content[1]))
  print(map_result[content[1]])
  
  if (map_result[content[1]] == DRAW):
    print(map_theirs[content[0]])
    result2 += map_theirs[content[0]]
  elif (map_result[content[1]] == WIN):
    print(beaten[map_theirs[content[0]]])
    result2 += beaten[map_theirs[content[0]]]
  elif (map_result[content[1]] == LOSE):
    print(beats[map_theirs[content[0]]])
    result2 += beats[map_theirs[content[0]]]

print("FIRST RESULT " + str(result))

print("SECOND RESULT " + str(result2))
