f = open("1.txt");
tot = [0];
for l in f:
  if l == "\n":
    tot.append(0)
  else:
    tot[len(tot)-1] += int(l);

tot.sort(reverse=True)

print(tot[0])

print(tot[0]+tot[1]+tot[2])
