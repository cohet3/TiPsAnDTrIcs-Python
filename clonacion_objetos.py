import copy
# CLanacion o copia  de objetos
# copia superficial (shallow) o copia poco profunda
lista_a = [[1,2],[3,4],[5,6]]
# Copia superficial
lista_b = list(lista_a)
# las listas son objetos distintos, apuntan a diferentes en memoria
# pero los niveles internos solo se copio la referencia

print(f' imprimimos la lista {lista_a}')
print(f' lista b {lista_b}')
# Comprobacion de que los objetos son distintos (a nivel superior)
# un cambio en el nivel superior, no afecta a la otra lista
lista_a.append([7,8])
print(f' imprimimos la lista {lista_a}')
print(f' lista b {lista_b}')
# Comprobacioon de que los objetos internos tiene la misma referencia(copia superficial)
# un cambio en la sublista afecta a la   lista q se copio
lista_a[0] [1]= 'A'
print(f' imprimimos la lista {lista_a}')
print(f' lista b {lista_b}')

# Copia profunda     (import copy)ç
lista_c = [[1,2],[3,4],[5,6]]
lista_d = copy.deepcopy(lista_c)
# Comprobacion de que son objetos distintos
lista_c.append([7,8])

print(f' imprimimos la lista c {lista_c}')
print(f' lista d {lista_d}')
# Ahora si, los elementos internos son nuevos objetos,no solo se copio la referencia
lista_c[0][1]='A'
print(f' imprimimos la lista c {lista_c}')   
print(f' lista d {lista_d}')
# El metodo copy sirve para realizar copias poco profundas (shallow)

