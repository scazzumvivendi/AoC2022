currentDir = ""
dir_size = dict()

def changeDir(newDir, currentDir):
  if newDir == '/':
    return '/'
  elif newDir == "..":
    return currentDir.rsplit("/", 1)[0]
  else:
    if currentDir == "/":
      return "/" + newDir
    else :
      return currentDir + "/" + newDir

def listDir(tokens):
  tokens = [t for t in tokens if t != '' and t != "ls"]
  for token in tokens:
    size_dir, name = token.split(" ")
    if(size_dir != "dir"):
      dirs = currentDir.split("/")
      for i, d in enumerate(dirs):
        newDir = "/".join(dirs[:i+1])        
        if newDir in dir_size.keys():
          dir_size[newDir] = int(dir_size[newDir]) + int(size_dir)
        else:
          dir_size[newDir] = int(size_dir)
  
          
with open("7.txt", 'r') as f:
  commands = f.read().split("$ ")
  for c in commands:
    lines = c.split('\n')
    if(len(lines) == False):
      continue
    tokens = lines[0].split(" ")
    tokens = [t for t in tokens if t != '']
    if(len(tokens) == False):
      continue
    if(tokens[0] == "cd"):
      currentDir = changeDir(tokens[1], currentDir)
    elif (tokens[0] == "ls"):
      listDir(lines)

#BEAUTY HACK
dir_size['/'] = int(dir_size[''])
dir_size.pop('')

vals = {k: v for k, v in dir_size.items() if v <= 100000}

print(sum(vals.values()))
needed_space = 30000000 - (70000000 - dir_size["/"])
print(needed_space)
print(dir_size)


#One liner?
deletable = {k: v for k, v in dir_size.items() if v > needed_space}
biggest_deletable = {k: v for k, v in dir_size.items() if v == min(deletable.values())}
#
print(biggest_deletable)
