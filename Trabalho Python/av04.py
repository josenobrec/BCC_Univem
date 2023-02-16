# Pedro Pazini, Vinicius Franzçozo e José Nobre

num = input('''Digite os números conforme exemplo: 100 9256
 >> ''').split(' ')

# Função do 1° método


def dms(num1, num2):
    if num1 < 10 and num2 < 10:
        return num1 + num2
    else:
        if num1 >= 10 and num2 >= 10:
            return dms(num1//10, num2//10)
        elif num2 >= 10 and num1 < 10:
            return dms(num1, num2//10)
        else:
            return dms(num2, num1//10)

# Função do 2° método


def dms2(a):
    if a < 10:
        return a
    else:
        return dms2(a//10)


print(dms(int(num[1]), int(num[0])))

print(dms2(int(num[1])) + dms2(int(num[0])))