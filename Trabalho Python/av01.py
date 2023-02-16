#Pedro Pazini, Vinicius Franzçozo e José Nobre
frase = input('Digite a mensagem codificada na linguagem do p: ')
frase_sem_espaco = frase.split(' ')
aux=''
for i in range(len(frase_sem_espaco)):
    for j,k in enumerate(frase_sem_espaco[i]):
        if j%2 == 1:
            aux+=k
    aux+=' '
print(f'Mensagem codificada: {frase}')
print(f'Mensagem decodificada: {aux}')