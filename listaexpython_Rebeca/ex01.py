vet = []
num = 0

def subst(vet):
    for i in range(len(vet)):
        if vet[i] < 0:
            vet[i] = 0
        elif vet[i] > 0:
            vet[i] = 1
    return vet

for i in range(30):
    num = int(input("Digite um número: "))
    vet.append(num)

print(subst(vet))