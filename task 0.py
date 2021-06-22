import random
w = [random.randint(-100, 100) for x in range(30)]
biggest = max(w)
r.index(biggest_number)
print(w)
print(biggest)
print(w.index(biggest_number)+1)
for i in range(29):
  if w[i]<0 and w[i+1]<0:
    print(w[i],w[i+1])
