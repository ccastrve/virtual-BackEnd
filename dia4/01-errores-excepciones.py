# retorna los errores definidos en python y los atributos de los errores
# Dir nos lista los atributos como strings para leerlos fácilmente
# Locals nos devuelve todas las variables disponibles en python
#print(dir(locals()['__builtins__']))

try:
    # captura error
    numero = int(input("Ingresa un número: "))
    print(numero)

except ValueError: # ingresa el flujo cuando se presenta errores de conversion de tipos
    print('Error al ingresar el número, no se ingreso número')

except Exception as error: # con Exception capturamos el error que se presenta generalmente es el error por descarte
    print(error) # imprimimos el error, podemos usar el metodo args
    #ejecuta acción cuando se da el error

else:
    print('Yo soy el else')

finally:
    print('yo soy el finally')


# cuando ingresa a un except ya no ingresa a otro except    


while True:
    try:
        valor = int(input('Ingrese un número: '))
        break
    
    except:
        print('debe ingresar un número')
    
    else:
        # se ejecuta si no no entra a ningún excep
        print('yo soy el else') 

    finally:
        # se ejecuta si hay except o no
        print('Yo soy el finally')


productID = input('Ingresa el id del producto: ')
try:
    if(productID == '10'):
        raise Exception('El producto no existe en la BD') # con raise se genera un error manual

except Exception as error:
    print('Algo salió mal: ', error.args[0])

else:
    print('Yo soy el else')

finally:
    print('yo soy el finally')















