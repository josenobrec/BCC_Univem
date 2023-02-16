#Pedro Pazini, Vinicius Franzçozo e José Nobre
def secs_to_hours(num):
    if num < 100000:
        return f'{num//10000} horas, {(num//100)%100} minutos e {num%100} segundos'
    else:
        return 'Este tempo não é possível!'

def hours_to_secs(num):
    num = str(num)
    num = num.replace(':','')
    num = int(num)
    return num

def Krunensberg_to_normal(num):
    resultado = hours_to_secs(num)
    return f'{resultado//3600} horas, {(resultado//60)%60} minutos e {resultado%60} segundos'

def main():
    escolha = int(input('''Escolha a funcionalidade que deseja
[1] De segundos para horas Krunensberg
[2] De horas para segundos de Krunensberg
[3] De horas de Krunensberg para horas normais
>>> '''))
    if escolha == 1:
        num = int(input('\nDigite os segundos desejados >> '))
        print(secs_to_hours(num))      
    elif escolha == 2 or escolha == 3:
        num1 = input('''\nDigite o horário desejado
conforme o exmemplo: '1:56:90'
>>> ''')
        if escolha == 2:
            print(f'{hours_to_secs(num1)} segundos')
        else:
           print(Krunensberg_to_normal(num1))
    else:
        print('Nenhuma dessas escolhas é a correta!')

main()