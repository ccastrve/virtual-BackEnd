from datetime import datetime
from flask import Flask, request # importamos clase Flask y funcionalidad request
from datetime import datetime

app = Flask(__name__)

clientes = []
# enviamos información
@app.route('/') 
def estado():
    hora_del_servidor = datetime.now()
    return {
        'status': True,
        'hour': hora_del_servidor.strftime('%Y/%m/%d %H:%M:%S')
    }

# recibimos información
@app.route('/clientes', methods=['POST']) 
# con el parámtero methods (que es una lista o tupla) indicamos el método que aceptará esta llamada, en este caso el método POST (ya no aceptará el método GET, si lo vemos en un navegador arrojará que el método POST no es soportado)

def obtener_clientes():
    # el request solo puede ser llamado en cada controlador (funcion que se ejecutará cuando se realice una petición desde el front)
    print(request.method) 
    # mostrará el tipo de método a la cual esta haciendo la consulta el front
    #print(request.data)
    print(request.get_json()) 
    #devuelve la información enviada por el body y la convertirá en un diccionario para que python pueda entender
    data = request.get_json()
    clientes.append(data)


    return {
        'message': 'Cliente agregado exitosamente',
        'cliente': data    
    }
# para recibir información del cliente se usa un método post. Los navegadores solo pueden usar métodos get de manera nativa, pero si pueden hacer post pero con complementos, en este caso instalaremos postman de https://www.postman.com/downloads/, para generar otros métodos diferentes a GET. usuario ccastrve, contraseña Ccastrve1@
# en postman, utilizamos el m{etodo post y en la pestaña de body, sección raw, escribimos el json que qeremos devolver (ahora se usa json, antes se utilizaba string)

# ** se pasa diccionario con llave - valor







app.run(debug=True)
# para que el servidor actualice los cambios automáticamente. debug si esta habilitado (True) se reiniciará automáticamente el servidor cada vez que guardemos cambios en cualquier archivo.







