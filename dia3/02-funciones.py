# se definen con def

from cmath import rect


def suma(* numeros): # numero infinitos de parametros de diferente tipos con *
    '''Suma n números y lo imprime''' # definicion de la variable
    suma = 0
    for n in numeros:
        suma += n
    return suma

print(suma(1, 2, 3, 4, 5))
print(suma.__doc__) # imprime la definicion de la funcion

usuario = []
def registrar(nombre, email, telefono):
    '''Registrar un usuario e imprimirlo'''

    usuario.append({
        'nombre': nombre,
        'email': email,
        'telefono': telefono
    })
    return {
        'message': 'Usuario registrado correctamente',
        'usuario': usuario[0]
    }, 1, True # retorna una tupla, no es necesario poner parentesis para la tupla
    # tambien podria retornarse tupla --> return ('usuario creado exitosamente', usuario[0], 201)

result_dict, result_num, result_bool = registrar('ccastrve', 'ccastrve@gmail.com', '945293978') # destructuramos la tupla de retorno el numero de parametros debe coincidir con las variables
# si no se quiere desempaquetar, asignar solo a una variable

print(result_dict)
print(result_num)
print(result_bool)

productos = []
def registrar_productos(nombre, precio, estado = True, almacen = 'Cercado'): # los parametros opcionales deben ir al final
    productos.append({
            'nombre': nombre,
            'precio': precio,
            'estado': estado,
            'almacen': almacen
    })

    return 'Producto registrado exitosamente'

registrar_productos('Tomate', 4.5)
registrar_productos('Apio', 1.4, False, 'Piura')
registrar_productos(almacen='Chiclayo', nombre='Pescado', estado=True, precio=10) # pueden ponerse parametros en diferentes orden pero se indica el nombre
print(productos)
print(productos[0]['nombre']) # imprimiendo un valor especifico de la lista


def alumnos(grupo, *args): # el primer parametro se guarda en uno y el resto en la tupla args
    print(grupo)
    print(args)

alumnos('Grupo 12', 'Pedro', 'Aaron', 'Abel', 'Jack')

# ** si se requiere agregra un numero indeterminado de parametros y se almacenen en un diccionario con el nombre de las claves que les ponemos en el parametro

def ingresarProducto(** kwargs):
    print(kwargs)
    if (kwargs.get('nombre')):
        print('El usuario quiere agregar un producto con el nombre')
    
    if (kwargs.get('cantidad')):
        print('El usuario quiere ingresar la cantidad del producto')

ingresarProducto(nombre = 'Manzan', precio = 2, estado = True, pais = 'Peru')
ingresarProducto(tamanio = 'XG', cantidad = 100, nombre = 'Pera')

def factorial (n):
    if n == 0:
        return 1
    return   n * factorial (n - 1)

print(factorial(5))

# funciones lambda varios parametros en una sola linea

rect = lambda base, altura: base * altura

print(rect(4, 5))











