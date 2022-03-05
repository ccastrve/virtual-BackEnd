from flask import Flask
from datetime import datetime

app = Flask(__name__) # se crea una instancia
# variable __name__ muestra si el archivo es el archivo raiz o principal del proyecto
# si el archivo es el archivo principal del proyecto entonces el valor de __name__ es __main__ en caso contrario devuelve otro valor
# accediendo a los atributos(celeste) y metodos(morado)

@app.route('/') # ahora esta respuesta se obtendra del servidor cuando llamamemos a 127.0.0.1:5000/
# usamos decoradores para definir que se ejecutara de acuerdo a la llamada del cliente
# los decoradores es un patron de software que se utiliza para modificar el funcionamiento de un metodo o clase en particular sin la necesidad de emplear otros metodos como la herencia
# aqui se modifica el comportamiento del metodo route para cuando la ruta de peticion sea '/' y su nuevo comportamiento definido en la funcion inicial()
def inicial(): # puede ser cualquier nombre
    print('Me llamaron')
    # siempre en los controladores tenemos que devolver una respuesta
    return 'bienvenido a mi API 🤡' # para insertar emojies en vscode --> en mac --> ctrl + cmd + espacio/ en windows --> tecla windows + .

@app.route('/api/info') # ahora esta respuesta se obtendra del servidor cuando llamamemos a 127.0.0.1:5000/api/info
def info_app():
    return {
        'fecha': datetime.now().strftime('%d-%m-%Y %H:%M:%S') # devuelve hora y fecha actual del servidor
    }

# por cada decorador se define la ruta a llamar y la funcion que se ejecutara con su return

# inicializaremos nuestro servidor de flask
app.run(debug = True) # indicamos modo debugging es decir modo de prueba, con ello cada vez que guardemos el servidor se reinicia 

# debug mode: off --> cuando se hacen cambios en los parametros el servidor solo se pausar y reinicia

# cuando escribimos www.localhost:5000/ cliente solicitando al servidor el metodo get y los endpoint, tambien hay otros metodos HTTP (get, post, put, delete)
# todos los navegadores solamente puede utilizar el metodo get
# endpoint --> ejm /usuarios , /productos
# cuando se hace la peticion, el servidor responde con un status (ejm 404 not found), puede responder con un body (texto, json) finalizando la comunicacion
# el que inicia la comunicacion es el cliente

# todo lo que declaremos luego de la llamada del metodo run() nunca se ejecutara porque run() hace que el servidor se quede colgado esperando
# Todo el codigo irá entre la instancia de la clase y el metodo run()

# Todos estos metodos son GET







