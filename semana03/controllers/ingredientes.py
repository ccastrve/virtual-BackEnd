
from flask_restful import Resource, request
# todos los métodos HTTP que vamos a utilizar se definen como métodos de la clase
# request sirve para utilizar la información que envía el usuario
# para apis más escalables se deben utilizar flask_restful con esto se puede almacenar los request y otros componente en múltiples archivos
# con flask todo los request se meten en un solo archivo

class IngredientesController(Resource):
    # se definen cada uno de los métodos de acceso a los request de la web
    def get(self):
        return {
            'message': 'Yo soy el get de los ingredientes'
            
        }

    def post(self):
        # en el método post siempre nos envían información por el body de la web
        # para obtener esa información utilizamos el método request.get_json() nos devuelve un diccionario
        print(request.get_json())
        return {
            'message': 'Yo soy el método post'
        }
        











