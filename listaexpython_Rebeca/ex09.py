num = int(input('Digite o valor: '))

if num > 0 and num < 4:
    num = num**2
elif num == 4 or num == 9:
    num = num ** 0.5
elif num > 5 and num < 9:
    num = num / 9

print(num)