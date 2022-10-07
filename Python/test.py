import time
def sum(x):
  if(x == 1): return 1
  else: return x + sum(x-1)
start = time.time()
print(sum(588))
end = time.time()
print(end-start)