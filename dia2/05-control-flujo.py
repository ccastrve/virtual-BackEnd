
# if <>
# debes respetar la identacion


edad = int(input("Ingresa tu edad: ")) # siempre captura en string y se debe convertir a entero

if edad >= 18:
    print("Eres mayor de edad") 
elif edad >= 15: 
    print("Eres adolescente")  # else es opcional
elif edad >= 3:
    print("Eres un niño")
else: 
    print("Eres un bebe")

print("Fin del programa")


ingreso = int(input("Ingresar numero: "))

if ingreso > 500:
    print("No recibe bono Yanapay")
elif (ingreso >= 250) and (ingreso <= 500):
    print("Si recibe el bono Yanapay")
else:
    print("Si recibe bono Yanapay y Balón de gas")


# operador ternario

n = int(input('Ingrese numero: '))
msg = 'numero par' if n % 2 == 0 else 'numero impar'







