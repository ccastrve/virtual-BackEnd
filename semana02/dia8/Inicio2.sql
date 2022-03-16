# esto es un comentario
# SQL Structure Query Language

-- SQL se divide en 2 o 3 partes
-- DML: Data Manipulation Language (insert, select, update, delete)
-- DDL: Data Language ()

CREATE DATABASE mydb;

USE mydb;

# con el atributo ENUM("A", "B", ...) puede ponerse el tipo de valores que puede aceptar el campo

CREATE TABLE clientes
(
	id					int unsigned NOT NULL auto_increment, #no es necesario especificar NOT NULL
    num_documento		varchar(15) UNIQUE, 
    tipo_documento		varchar(20),
    nombre				varchar(100) NOT NULL,
    apellido			varchar(100),
    edad				int unsigned,
    nacionalidad		varchar(100),
    estado				bool,
    PRIMARY KEY			(id)
);

# debemos poner el nombre de los campos se debe ingresar en el mismo orden
# los valores del insert pueden ir en comillas simples o dobles

INSERT INTO clientes (num_documento, tipo_documento, nombre, apellido, edad, nacionalidad, estado)
VALUES ("12345678", "DNI", "Cristhian", "Castro", 33, "Peru", True);

INSERT INTO clientes (num_documento, tipo_documento, nombre, apellido, edad, nacionalidad, estado)
VALUES 	("87654321", "CE", "Pedro", "Guinochio", 23, "España", True),
		("1068134432", "RUC", "Helly", "Sarango", 43, "Peru", False);

# SELECT columnas_visualizar FROM nombre_tabla

SELECT * FROM clientes;

# en mysql los boolean se guardan como 0 y 1
# tinyint valores de 0 a 255 (entero pequeño), el tamaño de los tinyint y bool son similares en tamaño

SELECT id, nombre, num_documento, estado FROM clientes;

SELECT * FROM clientes WHERE estado = true AND (apellido = 'Castro' OR apellido = 'Guinochio');

# mostrar las base de datos del servidor
SHOW databases; 

SELECT * FROM clientes WHERE tipo_documento = 'DNI' AND estado = 1;

# LIKE para ver la presencia de un patrón, con % reemplaza cualquier cantidad de caracteres
SELECT * FROM clientes WHERE nombre LIKE '%h%n%';

UPDATE clientes SET nombre = 'Cristhian Jesus', apellido = 'Castro Veliz' WHERE id = 1;

# no se puede actualizar datos con update y eliminaciones cuando en el where no hay un índice o Primary KEY
# a esto se llama modo seguro, se desactiva con SET SQL_SAFE_UPDATES = false; esta configuración es para 
# todo el usuario y servidor, también puede modificarse en preferencia, SQL editor

UPDATE clientes SET apellido = 'Guinochio Sarango' WHERE nombre = 'Pedro';


SELECT * FROM clientes;


DELETE FROM clientes WHERE id = 3;

# para cerrar doc  ctrl + W
# nuevo ctrl + T



DROP TABLE vacunas;

CREATE TABLE vacunas
(
	id 					INT AUTO_INCREMENT,
    nombre				VARCHAR(100) NOT NULL UNIQUE,
    estado				BOOL DEFAULT true,
    fecha_vencimiento	DATE,
    id_pais				INT,
    lote				VARCHAR(10),
    PRIMARY KEY			(id, lote),
    CONSTRAINT fk_pais FOREIGN KEY (id_pais) REFERENCES pais (id)
);


INSERT INTO vacunas (nombre, fecha_vencimiento, id_pais, lote)
VALUES 	('Sinopharm', '2023-12-31', '1', '0001'), 
		('Pfizer', '2024-12-31', '2', '0030'),
        ('AstraZeneca', '2024-07-01', '4', '0012'),
        ('Johnson & Johnson', '2023-04-20', '2', '0002'),
		('Sputnik', '2024-08-01', '3', '0005');

select * from vacunas;


DROP TABLE pais;

CREATE TABLE pais
(
	id			INT PRIMARY KEY AUTO_INCREMENT,
    nombre		VARCHAR(100) NOT NULL
);

INSERT INTO pais (nombre)
VALUES 	('China'),
		('Estados Unidos'),
        ('Rusia'),
        ('Reino Unido');

select * from pais;

CREATE TABLE vacunatorios
(
id			INT AUTO_INCREMENT PRIMARY KEY,
nombre		VARCHAR(100) NOT NULL,
latitud		FLOAT,
longitud	FLOAT,
direccion	VARCHAR(300) NOT NULL,
ubigeo		VARCHAR(5),
horario		VARCHAR(100)
);

drop table vacunatorios;

select * from vacunatorios;

# cambiar nombre de tablas RENAME TABLE tabla_origen TO nuevo_nombre
# DDL Data Definition Language, se usa para la definición de tablas, base de datos alter
# DROP TABLE nombre_tabla; para eliminar tabla
# DROP DATABASE nombre_base_datos;   elimina la base de datos
# ALTER TABLE nombre_tabla DROP COLUMNN nombre_columna; borrar columna
# ALTER TABLE nombre_tabla ADD COLUMN nombre_campo tipo_campo NOT NULL UNIQUE DEFAULT 'imagen.png' AFTER/FIRST columna_existente; agregar una columna después de la columna_existente, o FIRST si queremos que sea la primera columna
# no se puede agregar valores por defecto a los tipos de datos BLOB, TEXT, GEOMETRY o JSON
# ALTER TABLE nombre_tabla MODIFY COLUMN nombre_columna SET NUEVO_TIPO_DATO UNIQUE NOT NULL --> para cambiar el tipo de dato de una columna y configuraciones adicionales
# no se podrá cambiar el tipo de dato si ya hay información en esa columna y no corresponde con el nuevo tipo de dato

# DESC nombre_tabla --> arroja la descripcion de la tabla solo funciona en mysql

# al momento de ingresar la fecha se usa el ISO 8601  '2024-08-16'

# ================================================================================
 drop table vacunas;
 drop table pais;
 drop table vacunatorios;
    
                        
-- 1. Mostrar los nombres de las vacunas
-- 2. Mostrar las vacunas que sean de procedencia USA
-- 3. Mostrar las vacunas que NO sean de procedencia USA , signo diferente es != | <> | NOT campo = "..."
-- 4. Mostrar las vacunas que en su lote tengan los digitos 'xc'
-- 5. Mostrar todos los vacunatorios que tengan horario de atencion los dias miercoles
-- 6. Mostrar todos los vacunatorios que tengan la vacuna_id 1 pero que tengan foto , foto IS NOT NUL                        
                    
select * from clientes;
select * from vacunas;
select * from pais;
select * from vacunatorios;




