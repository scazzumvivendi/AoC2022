result = 0
result2 = 0
with open("4.txt", 'r') as f:
  lines = [line.rstrip() for line in f]
  for l in lines:
    l_assign, r_assign = l.split(",")
    print(l_assign, r_assign)
    l_start, l_end=l_assign.split("-")
    r_start, r_end=r_assign.split("-")
    l_range = range(int(l_start), int(l_end)+1)
    r_range = range(int(r_start), int(r_end)+1)
    first_int = list(set(l_range).intersection(r_range))

    if len(l_range) == len(first_int) or len(r_range)==len(first_int):
      print(first_int)
      result += 1

    if len(first_int) > 0:
      result2 += 1


print(result)
print(result2)
