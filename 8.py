count = 0
view=0

def calc_view_count(value, view):
  for i, n in enumerate(view):
    if(value<=n):
      cal=i+1
      return cal
  return len(view)
   

with open("8.txt", 'r') as f:
  lines=[[t for t in line.rstrip()] for line in f]
  height = len(lines)
  width = len(lines[0])
  for i, line in enumerate(lines):
    for j, value in enumerate(line):
      if i==0 or j == 0 or i==len(lines)-1 or j==len(line)-1:
        continue
      view_left = lines[i][0:j]
      view_right = lines[i][j+1:width]
      view_top = [row[j] for row in lines][0:i]
      view_bottom=[row[j] for row in lines][i+1:height]
      max_view_left = max(view_left)
      max_view_right = max(view_right)
      max_view_top = max(view_top)
      max_view_bottom=max(view_bottom)
      #print(f'view_left {view_left}')
      #print(f'view_right {view_right}')
      #print(f'view_top {view_top}')
      #print(f'view_bottom {view_bottom}')
        
      
      min_max = min(max_view_left[0], max_view_right[0], max_view_top[0], max_view_bottom[0])
      if value > min_max[0]:
        #print("FOUNDMAX")
        #print(f'value {value}')
        #print(f'max_view_left {max_view_left}')
        #print(f'max_view_right {max_view_right}')
        #print(f'max_view_top {max_view_top}')
        #print(f'max_view_bottom {max_view_bottom}')
      
        count += 1
          
      rev_view_left=view_left[::-1]
      rev_view_top=view_top[::-1]

      n_right_view = calc_view_count(value, view_right) 
      n_bottom_view = calc_view_count(value, view_bottom)
      n_left_view = calc_view_count(value, rev_view_left)
      n_top_view = calc_view_count(value, rev_view_top)

      n_view=n_right_view* n_bottom_view * n_left_view * n_top_view
      print(n_view, view)
      if n_view > view:
        view=n_view
  
  count=count + (height-1) * 4

print(count)
print(view)
