import math

def triangulo(vet):
    if vet[0] > vet[1] and vet[0] > vet[2]:
        hipot = vet[0]
        catet1 = vet[1]
        catet2 = vet[2]
    elif vet[1] > vet[0] and vet[1] > vet[2]:
        hipot = vet[1]
        catet1 = vet[0]
        catet2 = vet[2]
    else:
        hipot = vet[2]
        catet1 = vet[0]
        catet2 = vet[1]
    if hipot == math.sqrt(catet1**2 + catet2**2):
        return 1
    else:
        return 2

vet = [0]*3

for i in range(3):
    vet[i] = int(input('Digite um número: '))

if triangulo(vet) == 1:
    print('É triângulo retângulo')
else:
     print('Não é triângulo retângulo')



