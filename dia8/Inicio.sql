# esto es un comentario
# SQL Structure Query Language

CREATE DATABASE mydb;

USE mydb;

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


    
    

