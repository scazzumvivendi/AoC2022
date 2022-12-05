import math

result2 = ""

def cratemover(reverse = True):
  result = ""
  piles = {}
  with open("5.txt", 'r') as f:
    lines = [line for line in f]
    for i, l in enumerate(lines):
      if len(l) == 0:
        print(f'SEPARATOR {l}')
      elif l[0] == "[":
        for i, char in enumerate(l):
          if i % 4 == 1:
            #print(f'char {char} idx {i} pile {math.floor(i / 4)+1}')
            if char != " ":
              # Sets [] if not exists, inserts char
              piles.setdefault(math.floor(i / 4)+1, []).insert(0, char)
      elif l[0] == "m":
        #print(piles)
        #print(f'MOVE {l}')
        l_split = l.rstrip().split(" ");
        crate_much, crate_from, crate_to = int(l_split[1]), int(l_split[3]), int(l_split[5])
        #print(f'CRATES {crate_much, crate_from, crate_to}')
        # Gets last /crate_much/ items
        to_move = piles[crate_from][-crate_much:]
        if reverse:
          to_move.reverse()
        #print(f'OBJS TO MOVE {to_move}')
        # Gets split of piles until crate_much
        piles[crate_from] = piles[crate_from][:len(piles[crate_from]) - crate_much]
        piles[crate_to].extend(to_move)
  for i in range(1,10):
    result += piles[i][len(piles[i])-1]

  return result

print(cratemover())
print(cratemover(False))


