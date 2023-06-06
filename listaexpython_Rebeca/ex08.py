import random

mat = [[random.randint(0, 99) for i in range(5)] for i in range(5)]
for lin in mat:
    print(lin)

maior = float('-inf')  
segmaior = float('-inf')  

for lin in mat:
    for valor in lin:
        if valor > maior:
            segmaior = maior
            maior = valor
        elif valor > segmaior and valor != maior:
            segmaior= valor

print("Segundo maior valor:", segmaior)
