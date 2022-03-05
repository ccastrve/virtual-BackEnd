# para evitar el salto de linea en una impresion de pantalla print() podemos declarar un parametro end=''
# print('hola',end='*')
# print('estos son los ejercicios')

# Ejercicio 1
# Escriba una funcion que le pida al usuario ingresar la altura y el ancho de un rectangulo y que lo dibuje usando *, ejemplo:
# altura: 5
# ancho: 4
# Resultado:
# ****
# ****
# ****
# ****
# ****
# dibujar_rectangulo()


def rectangulo():
    '''
    Esta función imprime patron rectangular con asterísticos (*) a partir del alto y ancho ingresados por el usuario.
    Alto y ancho son números enteros.

    Args:
        Ninguno

    return:
        Ninguno
    
    '''

    print('Rectangulo procedimiento 1 con funciones isdigit')
    print('*' * 60)
    
    alto = input('Ingresar alto del rectángulo: ')
    while not alto.isdigit():
        print('Sólo ingrese números enteros')
        alto = input('Ingresar alto del rectángulo: ')
    
    ancho = input('Ingresar ancho del rectángulo: ')
    while not ancho.isdigit():
        print('Sólo ingrese números enteros')
        ancho = input('Ingresar ancho del rectángulo: ')
    
    for i in range(int(alto)):
        print('*' * int(ancho))

def rectangulo_2():
    '''
    Esta función imprime patron rectangular con asterísticos (*) a partir del alto y ancho ingresados por el usuario.
    Alto y ancho son números enteros.

    Args:
        Ninguno

    return:
        Ninguno
    
    '''
    print('\n\n')
    print('Rectangulo procedimiento 2 con captura de errores con Try')
    print('*' * 60)
    while True:
        try:
            alto = int(input('Ingresar alto del rectángulo: '))
            break
        except ValueError:
            print('Sólo ingrese números enteros')

    while True:
        try:
            ancho = int(input('Ingresar ancho del rectángulo: '))
            break
        except ValueError:
            print('Sólo ingrese números enteros')

    for i in range(alto):
        print('*' * ancho)


#rectangulo()
rectangulo_2()


# Ejercicio 2
# Escribir una funcion que nosotros le ingresemos el grosor de un octagono y que lo dibuje
# Ejemplo:
# Grosor: 5
#       *****
#      *******
#     *********
#    ***********
#   *************
#   *************
#   *************
#   *************
#   *************
#    ***********
#     *********
#      *******
#       *****
# dibujar_octagono()

def octogono():
    '''
    Esta función imprime patron de octogono regular con asterísticos (*) a partir del tamaño del lado ingresado por el usuario.
    El lado es un número entero.

    Args:
        Ninguno

    return:
        Ninguno
    
    '''

    print('\n\n')
    print('Octógono procedimiento con captura de errores con Try')
    print('*' * 60)

    while True:
        try:
            lado = int(input('Ingresar lado del octógono: '))
            break
        except ValueError:
            print('Sólo ingrese números enteros')

    ancho = lado
    for i in range(int(lado)):
        #for j in range(int(ancho)):
        print(' ' * (lado - i), '*' * (lado + 2 * i))
    
    for i in range(int(lado - 2)):
        print(' ', '*' * (lado + 2 * (lado -1)))

    for i in range(int(lado) - 1, -1, -1):
        #for j in range(int(ancho)):
        print(' ' * (lado - i), '*' * (lado + 2 * i))
    
octogono()




# Ejercicio 3
# Ingresar un numero entero y ese numero debe de llegar a 1 usando la serie de Collatz
# si el numero es par, se divide entre dos
# si el numero es impar, se multiplica por 3 y se suma 1
# la serie termina cuando el numero es 1
# Ejemplo 19
# 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
# serie_collatz()


def conjetura_collatz():
    '''
    Esta función ejecuta la conjetura de Collatz, que dice, que sea cual sea el número inicial, tras un número finito
    de repeticiones de la operación se llega a 1.
    El número inicial (semilla) es un entero ingresado por el usuario.

    - Si el numero es par, se divide entre dos
    - Si el numero es impar, se multiplica por 3 y se suma 1
    - La serie termina cuando el numero es 1

    Args:
        Ninguno
    
    Return:
        lista_collatz (lista): lista con los números de la serie de collatz 
    '''

    print('\n\n')
    print('Conjetura de Collatz')
    print('*' * 60)

    while True:
        try:
            semilla = int(input('Ingresar número inicial: '))
            break
        except ValueError:
            print('Sólo ingrese números enteros')

    lista_collatz = [semilla]
    numero = semilla    
    
    while numero != 1:
        
        if numero % 2 == 0:
            numero = numero // 2
        else:
            numero = numero * 3 + 1 
        lista_collatz.append(numero)
    
    return lista_collatz

print(conjetura_collatz())




# Ejercicio 4
# Cambiar una cadena de caracteres a formato CamelCase

def camel_case(* excepciones):
    '''
    
    Esta función convierte a mayúscula la primera letra de cada palabra de una oración ingresada por el usuario (formato Camel Case).
    Tiene opción de poner excepciones a no considerar en formato tupla.

    Arg:
        Excepciones (tupla): tupla con las palabras que no serán consideradas en la conversión, las palabras deben estar separadas por comas
    
    return:
        nueva_cadena (string): frase con la frase en formato Camel Case

    '''

    print('\n\n')
    print('Convertir frase ingresada a formato Camel Case')
    print('*' * 60)

    cadena = input('Ingrese una oración: ').lower()
    nueva_cadena = ''
    lista_cadena = cadena.split(' ')

    for c in lista_cadena:
        if c in excepciones:
            nueva_cadena = nueva_cadena + c + ' '
        else:
            nueva_cadena = nueva_cadena + c.capitalize() + ' '

    nueva_cadena.strip()
    return nueva_cadena

print(camel_case())


# Ejercicio 5

# crear una clase Persona en la cual se guarden su nombre, fecha_nacimiento, nacionalidad, dni, 
# ademas tambien una clase Alumno y una clase Docente en la cual el alumno , a diferencia del docente, 
# tenga una serie de cursos matriculados, y el docente por su parte tenga un numero del seguro social y 
# su cuenta de la CTS. En base a lo visto de herencia codificar las clases y ademas ver si hay algun atributo 
# o metodo que deba de ser privado.

print('\n\n')
print('Ejercicio de clases Persona, Alumno y Docente con Herencia')
print('*' * 60)

class Persona:

    def __init__(self, nombre, fecha_nacimiento, dni):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.dni = dni
    
    def mostrar_info(self):
        return {
            'nombre': self.nombre,
            'fecha_nacimiento': self.fecha_nacimiento,
            'dni': self.dni
        }

class Alumno(Persona):

    def __init__(self, nombre, fecha_nacimiento, dni, * cursos):
        super().__init__(nombre, fecha_nacimiento, dni)
        self.cursos = cursos

    def mostrar_info(self):
        info = super().mostrar_info()
        info['cursos'] = self.cursos
        return info

class Docente(Persona):

    def __init__(self, nombre, fecha_nacimiento, dni, seguro_social, cta_cts):
        super().__init__(nombre, fecha_nacimiento, dni)
        self.seguro_social = seguro_social
        self.__cta_cts = cta_cts # este atributo debe ser privado porque es crítico y debe manejarse solo al interior de la clase

    def mostrar_info(self):
        info = super().mostrar_info()
        info['seguro_social'] = self.seguro_social
        info['cta_cts'] = self.__cta_cts
        return info


persona1 = Persona('Juan', '1980-10-01', '12345678')
alumno1 = Alumno('Pepito', '2006-06-26', '98765432', 'Matemáticas', 'Comunicación', 'Ciencias')
docente1 = Docente('Carlos', '1978-12-28', '24686420', 'C-12345678', '0011-0287-03456783737')

print(persona1.mostrar_info())
print(alumno1.mostrar_info())
print(docente1.mostrar_info())
















