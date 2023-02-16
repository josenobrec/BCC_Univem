import random

linhas = 5
colunas = 4

M = [0] * linhas

for i in range(0,linhas):
  M [i] = [0]*colunas
  for j in range(0,colunas):
    M[i][j] = random.randint(1,25)

print("Matriz\n")
for i in range(0,linhas):
  for j in range(0,colunas):
    print('[{:^2}]'.format(M[i][j]),end ='')
  print()
print('\n')


somalinha = 0
medialinha = 0
for i in range(0,linhas):
  for j in range(0,colunas):
    somalinha = somalinha + M[i][j]  
    medialinha = somalinha / linhas
  print('Média Linha {} : {}'.format(i,medialinha))

somacoluna = 0
mediacoluna = 0 