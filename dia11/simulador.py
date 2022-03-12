from faker import Faker
from random import randint, choice

# no es necesario definir providers, fake por defecto carga todos los providers standar

#from faker.providers import internet, phone_number, person

fake = Faker()

#fake.add_provider(internet, phone_number, person)
# tanto el add_provider como el provider es necesario declararlo siempre que se este usando un standars provider (solamente será necesario cuando sea un provider de la comunidad)


def generar_alumnos(numero):

    for persona in range(numero):
        nombre = fake.first_name()
        apePat = fake.last_name()
        apeMat = fake.last_name()
        correo = fake.ascii_free_email()
        
        # generando un número aleatorio entre 911111111 y 999999999
        # telefono = fake.random_int(min=911111111, max=999999999)

        telefono = fake.bothify(text='9########')
        '''
        for _ in range(5):
            fake.bothify(text='Product Number: ????-########', letters='ABCDE')
        ...
        'Product Number: DCEB-66048764'
        'Product Number: EBCA-82421948'
        'Product Number: EBED-15781565'
        'Product Number: AEDC-78408016'
        'Product Number: EDAA-35139332'
        '''

        sql = '''INSERT INTO alumnos (nombres, apellido_paterno, apellido_materno, email, telefono_emergencia)
                        VALUES ('%s', '%s', '%s', '%s', '%s');''' % (nombre, apePat, apeMat, correo, telefono)


        '''INSERT INTO alumnos (nombres, apellido_paterno, apellido_materno, email, telefono_emergencia)
                        VALUES ('{}', '{}', '{}', '{}', '{}');'''.format(nombre, apePat, apeMat, correo, telefono)

        print(sql)


def generar_grados():
    secciones = ['A', 'B', 'C']
    ubicaciones = ['Sotano', 'Primer piso', 'Segundo piso', 'Tercer piso']
    niveles = ['Primero', 'Segundo', 'Tercer', 'Cuarto', 'Quinto', 'Sexto']
    grado = []

    
    
    for nivel in niveles:
        num_secciones = randint(2,3)

        for seccion in range(0, num_secciones):
            # ubicacion = random.randint(0,3)
            ubicacion = choice(ubicaciones)
            
            '''INSERT INTO grados (nombre, seccion, ubicacion)
                        VALUES ('%s', '%s', '%s');''' % (nivel, secciones[seccion], ubicacion)
            sql = '''INSERT INTO grados (nombre, seccion, ubicacion) 
                     VALUES ('{}', '{}', '{}');'''.format(nivel, secciones[seccion], ubicacion)
            print(sql)


# generar_alumnos(100)
generar_grados()

# ejercicio llenar la tabla matricula






# para llevarlo a un archivo python3 simulador.py > generacion_alumnos.sql




