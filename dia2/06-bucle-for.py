# se repite un número  limitado de veces

from audioop import reverse


notas = list(range(1,20,2))
print(notas)

i = 0
for nota in notas:
    print("nota {}: {}".format(i+1, notas[i]))
    i += 1

i = 0
for nota in notas:
    print("nota {}: {}".format(i+1, nota))
    i += 1

for indice in range(len(notas)): # en range(inicio, fin, step) solo recorre hasta fin-1, step es el salto (positivo o negativo)
    print(notas[indice])

print("Las 3 notas mayores")
notas.sort(reverse = True)
print(notas[0:3])





