# Diccionarios -dicts
# maps, hashmaps, lookuptables, etc (llave-valor)
# Ejemplo clasico: directorio (llave=nombre, valor = telefono)
directorio = {
    'Juan': 58689001,
    'Alicia': 5425145,
    'Pepitou': 7485778,
}
# Imprimir diccionario
print(directorio)

# recuperar un elemento
print(directorio['Juan'])

# Podemos utilizar una expresion para crear un diccionario
valores_al_cuadrado = {x: x*x for x in range(5)}
print(valores_al_cuadrado)

#Los tipos mutables no pueden ser llaves de un diccionario[listas]
lista = [1,2,3]
# diccionario_erroneo = {lista: 'A'}
# print(diccionario_erroneo)

#LOs imnutables como las tuplas si pueden ser llaves del dic
tuple = (1,2,3)
diccionario_correcto = {tuple: 'A'}
print(diccionario_correcto)

# Si queremos garantizar un orden de insercion, OrderdDict
from collections import OrderedDict
diccionario_ordenado = OrderedDict(uno=1,dos=2,tres=3)
print(diccionario_ordenado)
# Agregamos un nuevo elemento
diccionario_ordenado['cuatro']=4
print(diccionario_ordenado)
# obtenemos las llaves
print(diccionario_ordenado.keys())
# Si cambiamos algún valor de alguna llave, se mantiene el orden inserccion
diccionario_ordenado['uno']=-1
print(diccionario_ordenado)

# Eliminamos una llave
diccionario_ordenado.pop('tres')
print(diccionario_ordenado)

# volvemos a insertar el elemento eliminado
diccionario_ordenado['tres']=3
print(diccionario_ordenado)

# defaultdict es una subclase de dict
from collections import defaultdict

diccionario_default = defaultdict(lambda : 'Valor Erroneo')
diccionario_default['a']=1
diccionario_default['b']=2
print(diccionario_default.items())
# Imprimir un elemento no existente
print(diccionario_default['c'])

# Podemos crear valores  por default como una lista
diccionario_default_lista = defaultdict(list)
# si accedemos a una llave no existente, la crea y los valores se asignan como una lista
diccionario_default_lista['nombres'].append('Juan')
diccionario_default_lista['nombres'].append('Karla')
diccionario_default_lista['nombres'].append('Pedro')
print(diccionario_default_lista)
print(diccionario_default_lista.items())
print(diccionario_default_lista.keys())
print(diccionario_default_lista.values())

# Buscar en multiples diccionarios como si fuera un diccionario unico
from collections import  ChainMap

diccionario1={'Uno':1, 'dos':2, 'tres':3, 'cinco': 'A'}
diccionario2={'cuatro':4, 'cinco':5, 'seis':6}
# Combinacion de ciccionarios
combinacion_diccionarios = ChainMap(diccionario1, diccionario2)
print(combinacion_diccionarios)
# buscamos en todos los diccionarios de izquierda a derecha
print(combinacion_diccionarios['cinco'])
# Una llave no existente arroja un keyerror
# print(combinacion_diccionarios['sei'])

# diccionarios de solo lectura(read-only)
from types import MappingProxyType
diccionario_modificable = {'uno':1, 'dos':2, 'tres':3}
diccionario_solo_lectura = MappingProxyType(diccionario_modificable)
# Leemos el valor del diccionario
print(diccionario_solo_lectura)
# Intentamos modificar arroja error
# diccionario_solo_lectura['uno']=-1
# si modificamos el diccionario mutable , afecta al de solo lectura
diccionario_modificable['dos']=22
print(diccionario_modificable)
print(diccionario_solo_lectura)