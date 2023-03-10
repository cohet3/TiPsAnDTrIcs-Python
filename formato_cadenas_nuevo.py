# 2. Nuevo Estilo formato de canedas en python

nombre = 'juan'
mi_cadena = 'Hola, {}'.format(nombre)
print(mi_cadena)
# Podemos convertir enteros a hexadecimales

error = 500
cadena_hexadecimal = 'Error en hexadecimal: {error:x}'.format(error=error)
print(cadena_hexadecimal)

# Ejemplo enterp a flotante
entero = 50
cadena_flotante = 'NUmero flotante: {entero:.2f}'.format(entero=entero)
print(cadena_flotante)

# Podemos hacer lo mismo, pero usando String Interpolation(f.string)
mi_cadena = f'hola, {nombre}'
print(mi_cadena)

# Mandar a imprimir directamente
print(f'Hola, {nombre}')
# Este es el mismo ejemplo de hexadecimal con String Interpolation
print(f'Error en hexadecimal: {error:x}')
# de entero a flotante
print(f'Error en hexadecimal: {error:.2f}')
# Podemos incluir expresiones o llamadas a funciones
a = 10
b = 3
print(f'Dividimos y damos formato: {a/b:.2f}')
