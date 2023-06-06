import random

mat = [[random.randint(10, 50) for i in range(10)] for i in range(10)]
for lin in mat:
    print(lin)

maior = float('-inf')  

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if i != j:
            valor = mat[i][j]
            if valor > maior:
                maior= valor

print("Maior valor encontrado:", maior)
