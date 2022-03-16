from flask import Flask
from flask_restful import Api
from datetime import datetime
from controllers.ingredientes import IngredientesController
# con eso importamos la clase IngredientesController del archivo de python controllers/ingredientes.py 


app = Flask(__name__)
# creamos la instancia de flask_restful.Api y le indicamos que toda la configuración
# que haremos se agregue a nuetsra instancia Flask

api = Api(app = app)

@app.route('/status', methods=['GET'])
def status():
    return {
        'status': True,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:$S')
    }


# ahora definimos las rutas que van a ser utilizadas con un determinado controlador
# IngredientesController se puede agregar como paremétro por esta definido como clase Resource en controler.ingredientes
api.add_resource(IngredientesController, '/ingrediente', '/ingredientes')
# se puede poner varias direcciones donde se active el api en este caso para /localhost/ingrediente y para /localhost/ingredientes
# cuando corremos el servidor se crea una carpeta __pycache__ aqui guarda un cache para hacer más rápido y más eficiente el uso de los archivos



# ======================================================================================================
# comprobará que la instancia de la clase Flask se está ejecutando en el archivo principal del proyecto, 
# esto se usa para no crear múltiples instancias y generar un posible error en Flask
# no se puede instanciar flask dos veces en el mismo proyecto porque ocasionará errores
# el archivo principal es el que se corre con python xxx.py, los otros archivos que se llaman dentro de la aplicación son secundarios
# por proyecto se puede tener una sola instancia de flask, patron singletton para un framework solo debe crearse una sola instancia


# ahora se conecta nuestro framework con una ORM (object Relational Mapping), es una herramienta que nos permite utilizar python para la mayoria de las operaciones de creación y consultas de nuevos registros sin utilizar SQL
# los ORM aceptan multiple conexión, es decir, utilizar múltiples y diferentes BD
# en este caso utilizaremos SQLAlchemy es un ORM para python, otro es Ponny ORM
# usaremos la librería FlaskSQAlchemy abre soporte pars SQLALquemy


# aqui verificamos si estamos en el módulo principal
if __name__ == '__main__': 
    # con esto arrancamos nuestro servidor y cada vez que hagamos cambio se vuelva a areancar en automático
    app.run(debug = True)

# esto se imprimirá cuando ya se pare el servidor
print('Hola')


# en postman crear una coleccion (para manejar historial de request) y luego crear variables que serviran para toda la coleccion
# primera variable --> BASE_URL     valor --> http://localhost:5000/
# luego en la colección (hacer clic en los tres puntos) y poner añadir un request, y ponerle nombre
# en el GET poner el nombre de la variable creada {{BASE_URL}} y aparecerá en color naranja
# Los tipos de variables con C colecction, G Global y E enviroment
# para probar el get, escribir {{BASE_URL}}/status

# FlaskRESTful extensión de flask que ayuda a mantener el código limpio
# creamos una carpeta controllers para manejar el backend, cuando lo manejamos con el front es vista controlador, aqui van a estar todos mis controladores de Flask



















