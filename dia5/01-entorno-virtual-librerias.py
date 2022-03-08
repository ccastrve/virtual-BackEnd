# para que el print no haga salto de linea se puede agregar el caracter cualquiera al print
# print('Hola', end = '') deja vacio

#pip3 list --> lista todas las librerias instaladas en el scope de python
# en python cualquier libreria esta presente de manera global
# tener cuidado con las actualizaciones porque hay proyectos con versiones de librerias pasadas y si actualizamos y los cambios son fuertes quizas ya ni funcionene
# entorno virtual --> se instalan las librerias en este entorno y no valen para fuera de este entorno

# python3 -m venv entorno_prueba --> con este comando se crea un entorno virtual se genera uan carpeta, son lugares aislados aqui todas librerias que instalemos solo seran usadas aqui, ni tampoco las librerias globales pueden utilizarse aqui

# para activar el entorno de prueba utilizar 'source entorno_prueba/scripts/activate', para mac es 'bin' en lugar de 'scripts'con esto nos movemos al entorno virtual (en el caso de pwshell y cmd no es necesario poner source, para gitbash si es necesario poner source)
# con esta activacion se activa el interprete del entorno virtual, si no se activa clic en el la version de la barra inferior y cambiar el interprete python3 que esta en la carpeta del entorno virtual/bin
# podemos darnos cuenta en el terminal de vscode que aparece activado el entorno_prueba
# el entorno virtual se apaga/desactiva con 'deactivate'


# para instalar una libreria se ejecuta --> pip3 install 'nombre_libreria'
# para desinstalar --> pip3 uninstall 'nombre_libreria

# para utilizar una libreria se usa --> from 'nombre_libreria' import 'nombre_clase'
# ejemplo --> from camelcase import CamelCase

# en el caso de mac el entorno tiene crearse en el nivel superior donde esta las carpetas de los demas proyectos no puede estar en subcarpeta, debe estar en el nivel mas alto del workspace

from cgitb import text
from camelcase import CamelCase

instanciaCC = CamelCase('al', 'de') # creamos una instancia y si queremos ponemos excepciones de palabras que no debe considerar
texto = 'bienvenidos al mundo de backend'
print(instanciaCC.hump(texto)) # convierte todo a formato Camel Case --> primera letra de cada palabra mayuscula

# ejercicio hacer lo mismo que el CamelCase pero sin librerias
# con cmd + clic te lleva al detalle de la libreria

# si vemos en el icono de git (lado izquierdo de la barra), vemos que tenemos mas de 1000 archivos con cambios, pero esto se debe a la creacion de mi entorno virtual
# estos no debemos subir al github
# para ellos se crea un archivo .gitignore y se pone los archivos o carpetas que no queremos subir al repositorio (ignoramos) pero solo funciona a partir que lo creamos, los archivos que anteriormente se hicieron commit ya no les aplica la ignoracion
# se recomienda que vaya a fuera de todo, y se recomienda que solo se tenga uno
# en el caso de los entornos no es necesario subirlos porque son configuraciones de python, en esos entornos no se guarda nada de logica

# resumen
'''
Para activar el entorno:
* Para Windows con gitbash:
$ source nombre_entorno/Scripts/activate
* Para Windows con Powershell o CMD:
$ nombre_entorno/Scripts/activate
* Para Mac o Linux: 
$ source nombre_entorno/bin/activate
Para desactivar el entorno:
$ deactivate
Para listar las librerias:
$ pip list
Para instalar una libreria:
$ pip install nombre_package
Para desinstalar una libreria:
$ pip uninstall nombre_package

'''

# instalar flask --> pip3 install flask --> no s instalará otras librerías de las que depende

# no se puede crear un archivo con el nombre de una libreria existente













