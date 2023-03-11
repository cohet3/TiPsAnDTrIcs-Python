
#Comparacion del uso del operador == o el operador is en POO

# El operador == compara el contenido de dos objetos (igual)

# no necesariamente son el mismo objeto (pueden apuntar a objetos distintos

# Operador is revisa si dos objetos son iguales(identicos) ambos en la misma direccion de memoria

# ejemplo de lista
lista_a = [1,2,3]
lista_b = lista_a
print(f' contenido igual?: {lista_a == lista_b}')
print(f'apunta al mismo objeto? {lista_a is lista_b}')
# Sin embargo, si creamos un nuevo objeto
lista_c = list(lista_a)
# en este caso la lista a tiene el mismo contenido q c (== es true pero lista c apunta a un objeto distinto en memoria is False
print(f' contenido igual?: {lista_a == lista_c}')
print(f'apunta al mismo objeto? {lista_a is lista_c}')