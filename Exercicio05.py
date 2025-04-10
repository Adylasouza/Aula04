negativo= 0
for x in range(0,10):
    numero = int(input("Informe um número natural: "))
    if numero <0:
        negativo= negativo + 1
print(negativo)