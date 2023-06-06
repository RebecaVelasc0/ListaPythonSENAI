import random

mat = [[random.randint(10, 50) for i in range(10)] for i in range(10)]
for lin in mat:
    print(lin)

diagsec = [mat[i][9-i] for i in range(10)]
med_diagsec = sum(diagsec) / len(diagsec)

print("Média da diagonal secundária:", med_diagsec)
