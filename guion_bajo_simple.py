# eL GUION BAJO SIMPLE POR CONVENCION SE USA PARA INDICAR
# que una variable es temporal o sin importancia
for _ in range(3):
    print(f'Hola...{_}')

# También lo podemos utilizar cuando trabajamos con tuplas
valores = ('Juan', 'Perez', 31)
nombre, _ , edad = valores
print(nombre)
print(edad)
print(_)

# Se puede usar como variable temporal de cualquier tipo
_ = list()
_.append(1)
_.append(2)
_.append(4)
print(_)