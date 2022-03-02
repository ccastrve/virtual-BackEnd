# coleccion desordenada pero cada elemento esta relacionada con una llave

from multiprocessing.sharedctypes import Value


persona = {
    'nombre': 'Cristhian',
    'apellido': 'Castro',
    'edad': 33
}

# añadimos nueva clave, si no existe la agrega, pero si existe la actualiza
persona['correo'] = 'ccastrve@gmail.com'

print(persona['nombre'])

print(persona.keys()) # devuelve todas las llaves 
print(persona.values()) # devuelve todos los valores
print(persona.items()) # tuplas llave valor


for key, Value in persona.items():
    print(key, ": ", Value)

for item in persona.items():
    print(item)

for key in persona:
    print(key, ": ", persona[key])

# con esto buscamos una llave y si no la encuentra nos arroja un mensaje
print(persona.get('apellidos', 'no existe clave'))

persona.pop('correo') # con esto eliminamos una llave del dict

print(persona)



