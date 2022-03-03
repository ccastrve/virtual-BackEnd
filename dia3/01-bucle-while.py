# pass sirve para indicar dentro de un bloque de codigo que aun no definimos la logica que no haga nada pero que no de error

from calendar import c


numero = 0
while numero < 10:
    print(numero)
    numero += 1
else:
    print('El bucle termino correctamente')

lista = [1, 5, 16, 28, 234, 67, 29, 0]
pares = 0
impares = 0
i = 0
while i < len(lista):
    
    if lista[i] % 2 == 0:
        pares += 1
    else:
        impares += 1
    i += 1

print('Hay {} numeros pares'.format(pares))
print('Hay {} numeros impares'.format(impares))










