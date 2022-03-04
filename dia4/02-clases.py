# POO programación orientada a objetos

class Persona:
    # estos atributos pueden accederse desde la llamada de la clase
    fec_nac = '2000-01-01'
    nombre = 'Juan' # cada campo pasa a llamarse atributo
    soltero = True
    estatura = 1.70

    # Las acciones que pueden tener cada clase se definen como funciones y se llaman métodos
    def saludar(self): # en todos los metodos se utiliza el parametro self paea referirse a la misma clase
        print('Hola soy ', self.nombre)

    def decir_nombre(self):
        self.saludar() # se referencia con el self

persona1 = Persona()
persona2 = Persona() # son una copia en su totalidad de la clase, se llaman instancia
print(Persona.nombre)
print(persona1.nombre)
persona1.saludar()

# cuando una instancia se modifica un atributo ya no afecta si cambiamos el valor del atributo de la clase
persona1.nombre = 'Carolina'
Persona.nombre = 'Roberto'
print(Persona.nombre)
print(persona1.nombre)
print(persona2.nombre)
persona2.decir_nombre()


class Animal:
    nombre = ''
    sexo = ''
    patas = 0

    # metodo constructor
    def __init__(self, nombre, sexo, patas):
        self.nombre = nombre
        self.sexo = sexo
        self.patas = patas
    
    def descripcion(self):
        return 'Yo soy un {}, soy {} y tengo {} patas'.format(self.nombre, self.sexo, self.patas)

foca = Animal('Foca', 'M', 2)
caballo = Animal('Caballo', 'M', 4)
gato = Animal('Gato', 'F', 4)

print(foca.descripcion())
print(caballo.descripcion())
print(gato.descripcion())
















