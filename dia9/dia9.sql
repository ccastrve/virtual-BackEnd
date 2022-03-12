create database ejemplo_clase;
use ejemplo_clase;
CREATE TABLE vacunas(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) UNIQUE NOT NULL ,-- nombre que no se pueda repetir y que no admita valores vacios
    estado BOOL DEFAULT TRUE, -- estado que solo acepte bools [su valor por defecto sea true]
    fecha_vencimiento DATE, -- fecha_vencimiento fecha
    procedencia ENUM('USA', 'CHINA', 'RUSIA', 'UK'), -- procedencia sus valores pueden ser USA, CHINA, RUSIA, UK
    lote VARCHAR(10) -- lote no puede superara los 10 caracteres
);

CREATE TABLE vacunatorios (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    latitud FLOAT,
    longitud FLOAT,
    direccion VARCHAR(200),
    horario_atencion VARCHAR(100),
    -- La llave foranea (FK Foreign Key) es la representacion de la relacion entre la otra tabla e indicara todo su contenido
    -- representado solo por su id
    vacuna_id INT,
    FOREIGN KEY (vacuna_id) REFERENCES vacunas(id)
);

-- DDL Data Definition Language > se usara para la definicion de donde se almaceran los datos en mi bd
-- Para Renombrar una tabla con un nuevo nombre
-- RENAME TABLE valor_antiguo TO nuevo_valor;
-- CREATE TABLES | CREATE DATABASE 
-- DROP elimina la tabla y su contenido a diferencia del DELETE que solo elimina el contenido
-- DROP TABLE vacunatorios;
-- DROP DATABASE prueba;

-- Eliminara la columna de la tabla y perderemos todos los datos que hubiesen en ella
-- ALTER TABLE vacunatorios DROP COLUMN latitud;

-- Agregara una nueva columna indicando el tipo de dato 
-- No podemos agregar valores por defecto a los tipos de datos BLOB, TEXT, GEOMETRY o JSON
ALTER TABLE vacunatorios ADD COLUMN imagen VARCHAR(100) DEFAULT 'imagen.png' AFTER horario_atencion;

-- RENAME COLUMN > renombra la columna
ALTER TABLE vacunatorios RENAME COLUMN imagen TO foto;
-- ALTER TABLE vacunatorios CHANGE imagen foto VARCHAR(100) DEFAULT 'imagen.png'; -- Para versiones de mysql 5.6.x hasta 5.7.x
-- MODIFY COLUMN > cambiar el tipo de dato y los configuraciones adicionales 
-- NO PODREMOS CAMBIAR EL TIPO DE DATO si ya hay informacion en esa columna y no corresponde con el nuevo tipo de dato
-- ALTER TABLE vacunatorios MODIFY COLUMN imagen INT UNIQUE NOT NULL ;

-- Un vacunatorio podra tener una sola vacuna pero una vacuna puede estar presente en varios vacunatorios
-- vacunas < vacunatorios

-- SOLO FUNCIONA EN MYSQL 
DESC vacunatorios;



INSERT INTO vacunas (nombre, estado, fecha_vencimiento, procedencia, lote) VALUES
					('PFIZER', true, '2022-08-16', 'USA', '123jkl'),
                    ('SINOPHARM', true, '2022-10-10', 'CHINA', 'vxcvxc'),
                    ('MODERNA', true, '2022-09-14', 'USA', 'zxczxc'),
                    ('SPUTNIK', false, '2022-10-04', 'RUSIA', 'ghjkhjfg');

INSERT INTO vacunatorios (nombre, latitud, longitud, direccion, horario_atencion, foto, vacuna_id) VALUES
						('CAMINO REAL', 14.121, -21.121, 'AV GIRASOL 115', 'LUN-VIE 07:00 - 15:00', null, 1),
                        ('HOSP. GNRAL.', 17.521, 11.1891, 'AV CIRCUNVALACION S/N', 'LUN-VIE 07:00 - 15:00', 'hospital.jpg', 2),
                        ('POSTA CERRO AZUL', 11.258, 67.447, 'AAHH LOS QUERUBINES LOTE 3 MZ J', 'LUN-SAB 07:00 - 15:00', 'foto01.png', 1),
                        ('ESTADIO LOS PALITOS', 24.121, -21.121, 'CALLE ESPINOSA 1115', 'LUN-MIE-VIE 07:00 - 15:00', 'est0001.jpg', 3),
                        ('PLAZA DEL AMOR', 4.116, -21.121, 'AV DE LOS HEROES ANONIMOS S/N', 'LUN-VIE 07:00 - 15:00', null, 1);
                        
                        
-- 1. Mostrar los nombres de las vacunas
SELECT nombre FROM vacunas;
-- 2. Mostrar las vacunas que sean de procedencia USA
SELECT * FROM vacunas WHERE procedencia = 'USA';
-- 3. Mostrar las vacunas que NO sean de procedencia USA != | NOT LIKE | <> | NOT campo = '...'
SELECT * FROM vacunas WHERE procedencia != 'USA';
-- 4. Mostrar las vacunas que en su lote tengan los digitos 'xc'
SELECT * FROM vacunas WHERE lote LIKE '%xc%';
-- 5. Mostrar todos los vacunatorios que tengan horario de atencion los dias miercoles
SELECT * FROM vacunatorios WHERE horario_atencion LIKE '%MIE%' 
							OR horario_atencion LIKE '%LUN-VIE%' 
							OR horario_atencion LIKE '%LUN-SAB%';
-- 6. Mostrar todos los vacunatorios que tengan la vacuna_id 1 pero que tengan foto
SELECT * FROM vacunatorios WHERE vacuna_id = 1 AND foto IS NOT NULL; 


select * from vacunatorios where vacuna_id = 1;

# inner join es una intersección

select * from vacunatorios 
inner join vacunas on vacunatorios.vacuna_id = vacunas.id
where vacuna_id = 1;


-- inner join es por defecto join
select * from vacunatorios 
inner join vacunas on vacunatorios.vacuna_id = vacunas.id;


INSERT INTO vacunatorios (nombre, latitud, longitud, direccion, horario_atencion, foto, vacuna_id) VALUES
						 ('POSTA JOSE GALVEZ', 14.26598, 32.2569, 'AV. EL SOL 755', 'LUN-VIE 15:00 22:00', null, null);


select * from vacunatorios 
left join vacunas on vacunatorios.vacuna_id = vacunas.id;

select * from vacunatorios 
right join vacunas on vacunatorios.vacuna_id = vacunas.id;

# mysql no soporta full outer join, pero este se puede realizar con un left y un right join

select * from vacunatorios 
left join vacunas on vacunatorios.vacuna_id = vacunas.id UNION
select * from vacunatorios 
right join vacunas on vacunatorios.vacuna_id = vacunas.id;

-- para columnas que se repiten el nombre en varias tablas, se debe especificar el nombre de la tabla, para reducir el 
-- nombre se puede utilizar alias con AS

select v.nombre, h.nombre
from vacunatorios h join vacunas as v on h.vacuna_id = v.id
where v.nombre = 'Pfizer';

select * from vacunatorios;
select * from vacunas;


-- 1. Devolver todos los vacunatorio en los cuales la vacuna sea Sinopharm y su horario de atencion sea de LUN-VIE

select * from vacunatorios as h
inner join vacunas as v on h.vacuna_id = v.id
where h.horario_atencion like '%LUN-VIE%' and v.nombre = 'SINOPHARM';


-- 2. Devolver solamente las vacunas cuyo vacunatorio este ubicado entre la latitud -5.00 y 10.00 IN()

select * from vacunas as v
inner join vacunatorios as h on h.vacuna_id = v.id
where h.latitud between -5 and 10; --  o tambien puede ser >= -5 and h.latitud <= 10;


-- 3. Devolver todas las vacunas que no tengan vacunatorio y solamente su procedencia y nombre

select v.nombre, v.procedencia 
from vacunas as v
left join vacunatorios as h on h.vacuna_id = v.id
where h.vacuna_id is null;










                        
                        
                        
                        
                        
                        
                        
                        
                        
                        