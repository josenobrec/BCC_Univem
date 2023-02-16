from random import randint 
 
vetor0 = [] 
vetor1 = [] 
x = y = -1 
for i in range(0,49,1): 
    vetor0.append(randint(0, 999)) 

while (x < 0 or x > 49 or y < 0 or x > 49): 
    try: 
        x = int(input(' Digite o 1° indice de 0 á 49: ')) 
        y = int(input(' Digite o 2° indice de 0 á 49: ')) 
        if (x < 0 or x > 49 or y < 0 or x > 49): 
            print('\nAlgum dos valores digitados está fora do esperado ( 0 até 49)!\n') 
    except ValueError: 
        print("Este valor é Inexistente") 
if y > x: 
  print(f'\n o indice {x} contém o valor de {vetor0[x]}\n o índice {y} contém o valor de {vetor0[y]}\n\n{x} e {y}\n\n{vetor0[x:y+1]}')
  print()
else: 
  print("\n Invalido")
  print()
