# Pedro Pazini, Maria Eduarda Santos, Mariana Amaro, Vinicius Françoso, José Nobre e Marcel Tamada

cantores = {}
musicas = []
pCantor = []
pMusica = []


def cadastro():
    while True:
        x = input('Digite o nome do cantor >> ')
        if x not in cantores:
            while True:
                y = input('Digite o código do cantor >> ')
                if y not in cantores.values():
                    cantores[x] = y
                    print(f'Cadastro do cantor(a) {x} efetuado!!')
                    break
                else:
                    print('Código já cadastrado, informe outro!')
                    print()
            break
        else:
            print('Cantor já cadastrado!')
            print()


def listagem():
    print('Código   Nome')
    print('-'*20)
    for i, j in cantores.items():
        print(f"{j}      {i}")


def consulta():
    x = input('Digite o nome do cantor >> ')
    if x in cantores:
        for i, k in cantores.items():
            if x == i:
                print(f'O código do cantor {i} é {k}')
    else:
        print("Cantor não cadastrado!")


def menucantor():
    while True:
        print('='*50)
        print('Cantor'.center(50))
        print('='*50)
        choose = (input('''\nEscolha entre as opções:
[a] Cadastro
[b] Listagem
[c] Consulta
[d] Voltar
>> '''))
        if choose == 'a':
            print('='*50)
            cadastro()
        elif choose == 'b':
            print('='*50)
            listagem()
        elif choose == 'c':
            print('='*50)
            consulta()
        elif choose == 'd':
            break
        else:
            print('Valor não encontrado')


def cadMusica():
    boolean = True
    while boolean:
        tit = input('Titulo >>  ')
        if len(musicas) == 0:
            musica = dict()
            cod = input('Código do Cantor >> ')
            if cod in cantores.values():
                boolean = False
                for i in cantores.keys():
                    if cod in cantores.get(i):
                        print('*'*20, i, '*'*20)
                        gn = input('Estilo >>  ')
                        musica['titulo'] = tit
                        musica['cantor'] = cod
                        musica['estilo'] = gn
                        musicas.append(musica)
            else:
                print('Cantor não cadastrado, faça o cadastro do cantor primeiramente.')
                break
        else:

            for m in musicas:
                if tit in m.values():
                    print("Musica já existe, Cadastre outra musica")
                    print()
                    cadMusica()

            musica = dict()
            cod = input('Código do Cantor >> ')
            if cod in cantores.values():
                boolean = False
                for i in cantores.keys():
                    if cod in cantores.get(i):
                        print('*' * 20, i, '*' * 20)
                        gn = input('Estilo >>  ')
                        musica['titulo'] = tit
                        musica['cantor'] = cod
                        musica['estilo'] = gn
                        musicas.append(musica)
            else:
                print('Cantor não cadastrado, faça o cadastro do cantor primeiramente.')
                print()
                menuMusica()


def consulMusica():
    print('='*50)
    nome = input('Digite a música >>  ')
    for m in musicas:
        if nome in m.values():
            return f"Cantor: {m.get('cantor')} Estilo: {m.get('estilo')}"
    return f"Música não cadastrada!"


def menuMusica():
    while True:
        print('='*50)
        print('Música'.center(50))
        print('='*50)
        choose = (input('''\nEscolha entre as opções:
[a] Cadastro
[b] Listagem
[c] Consulta
[d] Voltar
>> '''))
        if choose == 'a':
            print('='*50)
            cadMusica()
        elif choose == 'b':
            print('Título--Cantor--Estilo')
            for m in musicas:
                print(m.get('titulo'), end=' ')
                for i in cantores.keys():
                    if m.get('cantor') in cantores.get(i):
                        print(i, end=' ')
                print(m.get('estilo'))
        elif choose == 'c':
            print(consulMusica())
        elif choose == 'd':
            break
        else:
            print('Valor não encontrado')


def playlistMusica():
    print('Montando sua Playlist... Informe suas músicas.')
    while True:
        tit = input('Informe o nome da música ou FIM para encerrar >> ')
        if tit == 'FIM':
            if len(pMusica) > 0:
                print('='*50)
                print('Playlist criada')
                for i, value in enumerate(pMusica):
                    print(f'{i + 1} - {value}')
                break
            else:
                print("Não foram escolhidas músicas cadastradas, playList vazia.")
                break
        else:
            a = False
            for m in musicas:
                if tit in m.values():
                    pMusica.append(m.get('titulo'))
                    a = True
                    print('Música Cadastrada')
            if a == False:
                print('Musica não cadastrada')


def playlistCantor():
    a = False
    x = input("Digite o nome do cantor >> ")
    if x in cantores:
        for i, k in cantores.items():
            if x == i:
                cod = k
        for m in musicas:
            if cod in m.values():
                pCantor.append(m.get('titulo'))
                a = True
            else:
                print("Não há músicas cadastradas para o cantor escolhido!")
                break
    else:
        print("Cantor não cadastrado!")
    if a:
        print('='*50)
        print('Playlist Criada')
        for i, value in enumerate(pCantor):
            print(f'{i + 1} - {value}')
    else:
        print("PlayList vazia.")


def menuPlaylist():
    while True:

        print('='*50)
        print('Playlist'.center(50))
        print('='*50)
        choose = input('''Escolha entre as opções:
[a] Gerar PlayList pelas músicas
[b] Gerar PlayList pelo artista
[c] Voltar ao Menu Principal
>> ''')
        if choose == 'a':
            print('='*50)
            playlistMusica()
        elif choose == 'b':
            print('='*50)
            playlistCantor()
        elif choose == 'c':
            break
        else:
            print('Valor não encontrado!')


def main():
    while True:
        try:
            print('='*50)
            print('Menu Principal'.center(50))
            print('='*50)
            choose = int(input('''\nEscolha entre as opções:
[1] Cantor(a)
[2] Musica
[3] Playlist
[4] Sair
>> '''))
            if choose == 1:
                menucantor()
            elif choose == 2:
                menuMusica()
            elif choose == 3:
                menuPlaylist()
            elif choose == 4:
                print('='*50)
                break
            else:
                print('Valor não encontrado')
        except ValueError:
            print('Valor Inválido!')


main()
