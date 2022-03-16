
from crypt import methods
from flask import Flask, request # importamos clase Flask y funcionalidad request
from datetime import datetime
from flask_cors import CORS, cross_origin
# pip3 es el gestor de descarga de python
# insomnia es igual que postman
# cross_origin es un controlador personalizado para modificar el cross

app = Flask(__name__)
CORS(app=app, origins=['http://127.0.0.1:1000', 'http://127.0.0.1:5500', 'http://miapp.vercel.app'], methods='*', allow_headers=['Content-Type'])
# creará los permisos para que todos puedan acceder (allowed-origin), para que cualquier metodo pueda ser consultado (allowed-method) y para cualquier header (allowed-header), * es el valor por defecto
# esto es muy abierto, debemos configurarlo por ejemplo agregando origenes, métodos, cabeceras
#Content-Type indicará el tipo de contenido que estamos aplicando, cuando enviemos un json su valor será 'application/json', un xml 'application/xml', etc.
# en el caso de mi pagina se debe poner la dirección de mi página web para que haga interacciones y se elimina las otras direcciones.
# aqui deben anotarse los puertos que van a acceder desde el front en este caso el live server usa el 5500, incluso no puede ir el de mi servidor el :5000.
#  en origins se indican los dominios que van a tener accesos a mi servidor
#  en methods se indican los metodos que se atenderán


clientes = [
    {
        "id": 1,
        "nombre": "Cristhian",
        "apellido": "Castro",
        "edad": 33,
        "pais": "Peru",
        "Especialidad": "Informatica"
    }
            ]

# enviamos información
@app.route('/') 
def estado():
    hora_del_servidor = datetime.now()
    return {
        'status': True,
        'hour': hora_del_servidor.strftime('%Y/%m/%d %H:%M:%S')
    }

# recibimos información
@app.route('/clientes', methods=['POST', 'GET']) 
# con el parámtero methods (que es una lista o tupla) indicamos el método que aceptará esta llamada, en este caso el método POST (ya no aceptará el método GET, si lo vemos en un navegador arrojará que el método POST no es soportado)

#  ======== OJO MODIFICAR CORS PARA UNA RUTA PARTICULAR ============
# @cross_origin(origins=['https://127.0.0.1:7000', 'http://mipagina.com'])
# con esto se modifica las reglas globales de la aplicación (CORS) implantados al inicio y que solamente se respeten estas nuevas reglas en estos nuevos endpoint con sus métodos correspondientes, es decir solo podrán acceder las solicitudes desde estos lugares frontend


def obtener_clientes():
    # el request solo puede ser llamado en cada controlador (funcion que se ejecutará cuando se realice una petición desde el front)
    if request.method == 'POST':
        print(request.method) 
        # mostrará el tipo de método a la cual esta haciendo la consulta el front
        print(request.data)
        print(request.get_json()) 
        #devuelve la información enviada por el body y la convertirá en un diccionario para que python pueda entender
        # el método data.get no sirve para traer, devolver
        data = request.get_json()
        data['id'] = len(clientes) + 1 
        # coge
        clientes.append(data)

        return {
            'message': 'Cliente agregado exitosamente',
            'cliente': data    
        }

    elif request.method == 'GET':
        return {
            'message': 'La lista de clientes',
            'cliente': clientes  
        }
    # para recibir información del cliente se usa un método post. Los navegadores solo pueden usar métodos get de manera nativa, pero si pueden hacer post pero con complementos, en este caso instalaremos postman de https://www.postman.com/downloads/, para generar otros métodos diferentes a GET. usuario ccastrve, contraseña Ccastrve1@
# en postman, utilizamos el m{etodo post y en la pestaña de body, sección raw, escribimos el json que qeremos devolver (ahora se usa json, antes se utilizaba string)

# ** se pasa diccionario con llave - valor

# @app.route('/cliente/<int:id>/<int:id_dpto>/<int:id_employee>', methods=['GET'])
# # el parámetro de la función debe ser el mismo de la app.route
# def gestion_usuario(id, id_dpto, id_employee): # se puede enviar varios parámetros
#     print(id)
#     return {
#         'id': id,
#         'id_dpto': id_dpto,
#         'id_employee': id_employee

#     }
# http://localhost:5000/cliente/1 , dominio (http://localhost:5000) y endpoint (/cliente/1)

def buscar_cliente(id):
    # resultado = None , lo hacemos así para obtener la ubicación, tratemos de enviar la pos y el contenido de esa posición para no volver a llamar nuevamente
    for pos in range(0, len(clientes)):
        if clientes[pos].get('id') == id:
            return (clientes[pos], pos)


@app.route('/cliente/<int:id>', methods=['GET', 'PUT', 'DELETE'])
# el parámetro de la función debe ser el mismo de la app.route
def gestion_cliente(id): # se puede enviar varios parámetros
    
    resultado = buscar_cliente(id)
    if resultado is not None: # antes de unzip verificamos que el resultado no sea None
        [resultado, pos] = buscar_cliente(id)    

    if request.method == 'GET':
        print(resultado,)
        if resultado:
            return resultado
        else:
            return ({
                    'message': 'El cliente no se encontró'
            }, 404)
            #  en Flask al retornar, podemos agregar una tupla, el primer elemento será el cuerpo del retorno (puede ser un mensaje), el segundo será el estatus (si no lo encuentra nos devolverá estatus 200 OK)
    
    elif request.method == 'PUT':
        if resultado:
            data = request.get_json()
            data['id'] = id # con esto agregamos a data el campo ID que no debería venir en la actualización
            clientes[pos] = data # aquí actualizamos el cliente con lo pasado en data incluyendo el ID que se agregó
            return clientes[pos]

        else:
            return ({
                    'message': 'El cliente a modificar no se encontró'
            }, 404)

    elif request.method == 'DELETE':
        if resultado:
            cliente_eliminado = clientes.pop(pos) # pop devuelve el cliente en la posición indicada por defecto el último
            return {
                'message': 'Cliente eliminado exitosamente',
                'cliente': cliente_eliminado
            }
        else:
            return ({
                    'message': 'El cliente a eliminar no se encontró'
            }, 404)
        
# endpoint registrados
# /clientes - GET POST (visualizar, crear)
# /cliente/:id - GET PUT DELETE (visualizar, actualizar, borrar)
# el servidor recibe solicitud, se verifica los servicios y pasaremos a llamar al controlador y responder (return) y también devolvemos status

#  en postman, nos devuelve información importante
#  status 200 OK , Time 6ms, Size: 196 B
#  Estados: respuestas informativas (100-199). Respuestas satisfactorias (200-299). redirecciones (300-399). Errores de los clientes (400-499). Errores de los servicios (500-599)
# metodo PUT y PATCH se usa para actualizar base de datos

# CRUD: Crear, leer, actualizar, borrar



app.run(debug=True) 
# también acepta un parámetro port para asignar puerto específico y no el 5000 que es el por defecto de flask-python (port='8080' por ejemplo)
# para que el servidor actualice los cambios automáticamente. debug si esta habilitado (True) se reiniciará automáticamente el servidor cada vez que guardemos cambios en cualquier archivo.







