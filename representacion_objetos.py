#__str__ su objetivo es q la informacion se legible para el usuario
# __repr__ su objetivo es q la informacion no se ambigua
# se utliza para hacer debuggin (formato tipo constructor)
# La implementcaion por default del metodo str llama a repr

class Auto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
# Por defasult solo se muestra el nombre de la y el id del objeto (direccion de memoria)
audi_a3 = Auto('audi', 'A3', 'rojo')
print(f'Audi: {audi_a3}')

class AutoStr:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    def __str__(self):
        return f'str: Marca: {self.marca}, Modelo {self.modelo}, Color: {self.color}'
    # def __repr__(self):
    #     return f'repr: Marca: {self.marca}, Modelo {self.modelo}, Color: {self.color}'

    def __repr__(self):
        return (f'{self.__class__.__name__} ('
                f'{self.marca!r}, {self.modelo}, {self.color!r}')

audi_a1  = AutoStr('Audi', 'a1', ' blanco')
# tenemos diferentes formas de imprimir el objeto
print(audi_a1)
print(audi_a1.__str__())
print('{}'.format(audi_a1))
print(f'{audi_a1}')
# Sin embargo es recomendable usar __repr__ en lugar de __str__
# ej. cualquier coleccion utiliza repr en lugar de str para mostrar la informacion
print([audi_a1])
# tambien usan !r
print(f'[audi_a1!r]')
# tambien manuealmente podemos escoger q metodo utilizar
print(str(audi_a1))
print(repr(audi_a1))