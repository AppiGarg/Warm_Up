import random
def Create_lst():
  lst = []
  for i in range (10):
    Rand = random.randint(-1000, 1000)
    lst.append(Rand)
  return lst

lst = Create_lst()
def swap(lst, i1, i2):
  lst[i2 - 1]

def Sort(lst):
  for i in range(len(lst)):
    min = i
    for b in range(i, 9):
      if lst[b] < lst[min]:
        min = b
    swap(lst, min, i)
    
      


