# operadores de comparacion

num1, num2 = 10, 20

# igual que, mayor que, menor que
print(num1 == num2) # igualdad
print(num1 != num2) # diferente
print(num1 >= num2) # mayor igual
print(num1 <= num2) # menor igual

# operadores logicos

print((10 > 5) and (10 < 20)) # y
print((10 < 5) or (10 < 20)) # o


# operadores de identidad

# is , is not para verificar si las variables estan apuntando a un mismo objeto (la misma direccion)

verduras = ['apio', 'peregil', 'lechuga']
verduras2 = verduras # en colecciones al asignar se creo un apuntador a la variable para no duplicar y ambas variables apuntan al mismo objeto y se actualizan ambas si actualizo una de ellas
verduras3 = verduras.copy() # aqui no asigna apuntador, sino una copia crea otro objeto, este metodo solo es para colecciones

print(verduras is verduras2)
print(verduras is verduras3)

# en string (y datos primitivos) tambien se hace pero cuando cambian de valor ya se mueve el apuntador a otro objetos
nombre1 = 'Cristhian'
nombre2 = nombre1
nombre2 = 'Juan'
print(nombre1 is nombre2)

num5 = 10
num6 = num5
print(num5 is num6)

nombre = 'eduardo'
nacionalidad = 'colombiano'

print((nombre == 'eduardo') and (nacionalidad == 'peruano' or nacionalidad == 'colombiano'))














