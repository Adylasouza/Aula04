intervalo= 0
fora = 0
for x in range(10):
    numero = int(input("Informe um número natural: "))

    if numero < 10 or numero > 20:
        print("Número não se encontra no intervalo.")
        fora+=1
    else:
        intervalo+=1
#intervalo=10-fora
print(intervalo)