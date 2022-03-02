# las tuplas no se pueden modificar

cursos = ('backend', 'frontend')
print(cursos[1])

# si dentro de la tupla tenemos colecciones de datos modificables estas si se pueden modificar

tupla2 = (1, 2, 3, [4, 5, 6])
tupla2[3][0] = 'Hola'
print(tupla2)

lista = list(tupla2)
print(lista)
print(len(tupla2))












