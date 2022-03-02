#lista (list) : colecciones de datos ordenadas, pueden contener valores heterogeneos
# empiezan en la posicion 0
# si ponemos una posición inexistente nos arroja error fuera de rango

nombres = ['Pedro', 'Luis', 'Danny', 'Cesar', 'Magaly']
combinada = ['Aaron', 80, False, 15.8, [1, 2, 3]]

print(nombres[2])
print(nombres[-2])

print(nombres)

print(nombres.pop()) # remueve y muestra el ultimo elemento de la lista

print(nombres)

nombres.append('Ana') # agrega un elemento al final de la lista

print(nombres)

print(nombres[1:3]) # para seleccionar rango de elementos
# con .copy() se copia toda la lista y se crea el mismo puntero, es los mismo que asignar [:] pero aqui no se asigna el mismo puntero
x = nombres[:] # si se quiere que una lista no se asigne al mismo puntero podemos hacer una copia con [:]
y = x

print(id(nombres))
print(id(x))
print(id(y))
busqueda = input()
print(busqueda in nombres)

nombres.insert(3, 'Marina') # inserta en la posición indicada
print(nombres)

del nombres[1] # elimina el contenido de la posición en mención
print(nombres)

nombres.clear() # elimina todos los elementos de la lista
print(nombres)







