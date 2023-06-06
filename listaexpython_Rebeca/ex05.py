vetor = [0]*6
matriz = [0]*6
for i in range(6):
    matriz[i] = [0]*6

for lin in range(6):
    for col in range(6):
        matriz[lin][col] = input('Digite um número: ')
print(matriz)

for lin in range(6):
    for col in range(6):
        print (lin,col)
        if lin == col:
            print ('Diagonal Principal', lin, col)
            vetor[lin] = matriz[lin][col]
print (vetor)
