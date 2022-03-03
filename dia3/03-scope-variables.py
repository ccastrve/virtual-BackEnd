nombre = 'Cristhian'

def saludar(): # si queremos utilizar la variable definida fuera de la funcion debemos utilizar global
    # si no utilizamos global la trata como una variable diferente
    global nombre
    nombre = 'abc'
    print(nombre)

# Aqui imprimirá el mismo resultado
saludar()
print(nombre)
