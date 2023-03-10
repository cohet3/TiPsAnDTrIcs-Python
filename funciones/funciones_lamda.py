# Las funciones lambda nos permiten declarar funciones anonimas en una solo linea de cod

def sumar(a, b):
    return a + b
print(sumar(3, 5))

# funcion lambda es una funcion anonima
sumas_lambda = lambda a, b: a + b
print(sumas_lambda(2, 4))

# utilizando una solo linea de codigo
print((lambda a, b: a+ b)(8, 9))

# ORdenar lista de tuplas, por su segundo valor porporcionado, una llave (key)
# Podemos usar una funcion lambda simpre que necesitemos una funcion muy concreta
lista_tuplas = [(1, 'b'), (6, 'f'), (0, 'd'), (4, 'a')]
lista_tuplas_ordenada = sorted(lista_tuplas, key=lambda tupla: tupla[0], reverse=True)
print(lista_tuplas_ordenada)
lista_tuplas_ordenada = sorted(lista_tuplas, key=lambda tupla: tupla[1])
print(lista_tuplas_ordenada)

# otro ejemplo de ordenamiento usando una expresion lambda
print(list(range(-3, 4)))
for valor in range(-3, 4):
    print(valor, valor*valor)

# Ahora lo aplicamos a una expresion lambda
lista_ordenada = sorted(range(-3, 4), key=lambda valor: valor*valor)
print(lista_ordenada)

# Las funciones lambda tambien podemos aplicar el concepto de closure

def mostrar(titulo):
    return lambda mensaje: titulo + '. ' + mensaje

mostrar_ing = mostrar('Ingeniero')
mostrar_lic = mostrar('Licenciado')
print(mostrar_ing('Calors Laracro'))
print(mostrar_lic('Armando Casas'))

# Ejemplos de casos de funciones lambda que no son recomendables
class Prueba:
    mostrar = lambda self: print('Funcion mostrar...')
    saludar = lambda  self: print('Funcion saludar')


prueba = Prueba()
prueba.mostrar()
prueba.saludar()

# Otro ejemplo donde una funcion lambda agregaria complejidad inecesaria
lista_pares = list(filter(lambda valor: valor % 2 == 0, range(10)))
print(lista_pares)
# Resolviendo el mismo ejercicio pero utilizando list comprehension
lista_pares_modificada = [valor for valor in range(10) if valor % 2 == 0]
print(lista_pares_modificada)
