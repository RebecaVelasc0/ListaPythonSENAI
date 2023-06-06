num = int(input('Digite o valor: '))
fatorial = 1

if num > 0  and num < 3:
    num = num**3
    print(num)
elif num % 3 == 0:
    for i in range(1, num + 1):
        fatorial = fatorial * i
        num = fatorial
    print(num)
elif num > 3 and num < 9:
    num = num / 9
else:
    num = print('Valor inválido')

