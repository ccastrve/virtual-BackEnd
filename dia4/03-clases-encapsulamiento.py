# encapsulamiento es declarar tipos de accesibilidad a los atributos y metodos

from pickletools import anyobject


class Producto:
    # existen 3 tipos de accesibilidad a los atributos y metodos: public
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

        # privado puede ser accedido desde la clase, pero no desde fuera de la clase o     de     la     instancia
        # un atributo se pone privado cuando no necesitamos que sea modificado desde afuera o que no varie su valor o calculo (en el caso de metodos)
        self.__ganancia = self.precio * 0.30

    def mostrar_info(self):
        return {
            'nombre': self.nombre,
            'precio': self.precio,
            'ganancia': self.__ganancia,
            'IGV': '{:.3f}'.format(self.__calcular_igv()) # para formatear cifras decimales
        }

    def aumentar_ganancia(self):
        self.__ganancia *= 1.1

    def __calcular_igv(self):  # no se podria acceder a este metodo desde afuera porque es privado
        return self.precio * 0.18


# aqui tenemos un atributo publico porque puede accederse desde afuera
cepillo = Producto('Cepillo dental', 3.8)
print(cepillo.nombre)
#print(cepillo.__ganancia()) # dara error porque este atributo es privado y no puede accederse desde afuera
print(cepillo.mostrar_info())
cepillo.aumentar_ganancia()
print(cepillo.mostrar_info())












