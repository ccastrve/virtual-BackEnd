use colegio;
# renombrar una columna --> alter table alumnos rename column nombre_inicial to nombre_final

select * from alumnos;
select * from grados;

# alter table nombre_tabla drop index nombre_indice_a_eliminar, para eliminar un indice (llave, unique, etc)
select * from grados;

DROP TABLE 	matricula;

insert into matricula (id_alumno, id_grado, fecha_cursada)
		values 	(1, 1, 2000),
				(1, 1, 2001),
                (1, 4, 2002),
                (1, 8, 2003),
                (2, 6, 2002),
                (2, 9, 2003),
                (3, 4, 2002);
                

select * from matricula;
select * from vacunatorios as h
inner join vacunas as v on h.vacuna_id = v.id
where h.horario_atencion like '%LUN-VIE%' and v.nombre = 'SINOPHARM';


-- tarea
-- 1 todas los alumnos que tienen correo de gmail

select * from alumnos
where email like '%@gmail%';


-- 2 todos los alumnos que hayan cursado el año 2002

select * from alumnos
join matricula on alumnos.id = matricula.id_alumno
where matricula.fecha_cursada = '2002';


-- 3 todos los grados donde su ubicacion sea el sotano o segundo piso

select * from grados
where ubicacion in ('Sotano', 'Segundo piso');

-- 4 todos los grados que han tenido alumnos en el año 2003, mostrar la seccion y nombre grado

select nombre, seccion, fecha_cursada as año
from grados
join matricula on grados.id = matricula.id_grado
where matricula.fecha_cursada = '2003';

-- 5 mostrar todos los alumnos del quinto A
select *
from alumnos join matricula on alumnos.id = matricula.id_alumno
			 join grados on grados.id = matricula.id_grado
where grados.nombre = 'Segundo' and grados.seccion = 'B'


-- 6 mostrar todos los correos de los alumnos de primero B






