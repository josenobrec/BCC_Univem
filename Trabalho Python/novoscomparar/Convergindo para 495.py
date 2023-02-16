from random import *

def remove_repetidos(numero_random):
  lista_numero  = list(map(int, str(numero_random))) 
  lista_retorno = []
  for i in lista_numero:
      if i not in lista_retorno:
          lista_retorno.append(i)
  lista_retorno.sort()
  return lista_retorno

def gera_numero():
  numero_random = randint(100,1000)
  numero_validacao = remove_repetidos(numero_random)
  if len(numero_validacao) < 3:
    gera_numero()

  return numero_random

def ordena_numero(numero_random, reverter=False):
  lista_numero  = list(map(int, str(numero_random))) 
  lista_numero.sort(reverse=reverter)
  numero        = int("".join(map(str, lista_numero)))
  return numero

def calcula_valor(numero_maior, numero_menor):
  return numero_maior - numero_menor

numero       = gera_numero()
print(numero)

numero_maior = ordena_numero(numero, True)
numero_menor = ordena_numero(numero, False)

iteracao=0
cont = True
while(cont):

  novo_numero = calcula_valor(numero_maior, numero_menor)

  iteracao += 1

  numero_maior = ordena_numero(novo_numero, True)
  numero_menor = ordena_numero(novo_numero, False)
  
  print(novo_numero)
  
  cont = novo_numero != 495

print(iteracao)