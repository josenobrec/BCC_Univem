# Pedro Pazini, Vinicius Franzçozo e José Nobre

def insertion(valor):
    return tuple(valor.split(' '))


def consult(cor, vet):
    for i in range(len(vet)):
        if cor == vet[i][1].lower():
            return vet[i][0]
    return 'Cor não cadastrada'


def main():
    # vet = [('#000000', 'Black'), ('#363636', 'grey21'), ('#696969', 'DimGray')]
    vet = []
    while True:
        try:
            choose = int(input('''\nEscolha entre as opções:
[1] Inserção
[2] Consulta
[3] Listagem
[4] Sair
>> '''))
            if choose == 1:
                vet.append(insertion(input(
                    '''\nDigite o código e a cor, conforme exemplo: #000000 Preto
>> ''')))
            elif choose == 2:
                color = input('\nDigite a cor que deseja procurar >> ').lower()
                print(consult(color, vet))
            elif choose == 3:
                print()
                for valor in vet:
                    print(f'{valor[0]} = {valor[1]}')
            elif choose == 4:
                break
            else:
                print('Valor não encontrado')
        except ValueError:
            print('Valor Inválido!')

main()

