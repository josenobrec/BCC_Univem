n = 1
while (True):
  cont = 0
  for i in range(1,16):
    if(n % i == 0):
      cont+=1
  if (cont == 15):
    print (n)
    break
  n+=1