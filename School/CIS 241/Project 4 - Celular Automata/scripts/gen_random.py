import random
p = 0.5
w = 800
h = 800

for r in range(h):
  for c in range(w):
    if(random.uniform(0,1) < p):
      print('#', end='')
    else:
      print('.', end='')
  print('')
