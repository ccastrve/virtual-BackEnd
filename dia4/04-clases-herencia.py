# DRY --> no te repitas a ti mismo Don't repeat yourself

class Usuario:
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
    
    def saludar(self):
        return 'Hola soy {}'.format(self.nombre)

# ahora crearemos la clase alumno que heredara de la clase usuario (clase padre)
class Alumno(Usuario):
    def __init__(self, nombre, apellido, correo, padres):
        # super() solo servira para acceder a los metodos de la clase padre que se esta heredando
        super().__init__(nombre, apellido, correo)
        self.padres = padres

    def info(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'padres': self.padres,
            'saludar': super().saludar()
        }

AlumnoPedro = Alumno('Pedro', 'Flores', 'pflores“gmail.com', [{
    'nombre_papa': 'Wilber',
    'apellido_papa': 'Martinez'
}, {
    'nombre_mama': 'Juliana',
    'apellido_mama': 'Perez'
}])

print(AlumnoPedro.info())






