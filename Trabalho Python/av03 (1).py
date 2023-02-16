#Pedro Pazini, Vinicius Franzçozo e José Nobre
def prahse_to_number(valor):
    alfabeto = list('abcdefghijklmnopqrstuvwxyz.!# ')
    matriz = []
    if len(valor) % 2 == 1:
        valor.append(' ')
    aux = len(valor)//2
    for i in range(2):
        matriz.append([])
        for j in range(aux):
            if valor[j] in alfabeto:
                matriz[i].append(alfabeto.index(valor[j])+1)
        del valor[0:len(valor)//2]
    return matriz

def number_to_prahse(valor):
    a = ''
    alfabeto = list('abcdefghijklmnopqrstuvwxyz.!# ')
    for i in range(2):
        for j in range(len(valor[i])):
                valor[i][j] = alfabeto[int(valor[i][j])-1]
        a+=''.join(valor[i])
    return a.replace('#', ' ').rstrip()

def cript(valor):
    A = [[3,1],[2,1]]
    c =[]
    for i in range(2):
        c.append([])
        for j in range(len(valor[i])):
            c[i].append(0)
            for k in range(len(valor)):
                c[i][j] += A[i][k] * valor[k][j]
            print(c[i][j], end = ' ')

def decript(valor):
    B = [[1,-1],[-2,3]]
    c =[]
    matriz = []
    aux = len(valor)//2
    for i in range(2):
        matriz.append([])
        for j in range(aux):
            matriz[i].append(valor[j])
        del valor[0:len(valor)//2]
    
    for i in range(len(matriz)):
        c.append([])
        for j in range (len(matriz[i])):
            c[i].append(0)
            for k in range(len(matriz)):
                c[i][j] += B[i][k] * int(matriz[k][j])
                            
    for i in range(2):
        for j in range(len(c[i])):
            c[i][j] = str(c[i][j])
    return c

def main():
    while True:
        main = int(input('''\nEscolha sua opção
[1] Frase para número
[2] Número para frase
[3] Sair
>> '''))
        if main == 1:
            digite = list(input('\nEscreva a frase \n>> ').lower().replace(' ', '#'))
            print()
            cript(prahse_to_number(digite))
            print()
        elif main == 2:
            digito = (input('\nEscreva os números \n>> ')).split()
            print(f'\n{number_to_prahse(decript(digito))}')
        else:
            print('\nAdeus!')
            break
main()