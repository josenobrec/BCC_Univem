
from random import randint

a = []
b = []
c = []
for i in range(10):
  a.append(randint(1,50))
  b.append(randint(1,50))
b = list(reversed(b))
for i in range(10):
  c.append(a[i] + b[i])
b = list(reversed(b))
print("\nPosiçao A: ",a)
print("\nPosiçao B: ",b)
print("\nPosiçao C: ",c)
