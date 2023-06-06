num = int(input('Digite o valor: '))

if num < 0:
    num = abs(num)
elif num > 10:
    print('Digite outro valor')
    num2 = int(input('Digite o valor: '))
    num = num - num2
else:
    num = num/5

print(num)