def calcexpre(num):
    num1 = 2
    num2 = 3
    soma = 0
    while num1 <= num:
        print('{}/{}'.format(num1, num2))
        soma += num1/num2
        num1 += 1
        num2 += 2
    return soma

num = int(input('Digite um número:'))
while num <= 0:
    print('Por favor digite um número positivo')
    num = int(input('Digite um número:'))

print(calcexpre(num))