from random import *
cont = 0
numsorteado = randint(0,100)

while(True):
  numdigitado = int(input("Digite um numero: ")) 
  if(numsorteado == numdigitado):
    print("Parabens, Você acertou o numero sorteado é o ",numsorteado)
    break

  elif(numdigitado != numsorteado):
    if(numsorteado > numdigitado):
      print("O numero sorteado é maior")
      cont+=1
      print("Você esta na tentativa n°",cont)
    else:
      print("o numero sorteado é menor")
      cont+=1
      print("Você esta na tentativa n°",cont)
