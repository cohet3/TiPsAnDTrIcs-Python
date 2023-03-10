# Distintas formas de dar formato a cadenas en Python
# 1. Estilo antiguo
nombre = 'Juan'
mi_cadena = 'Hola, %s' % nombre
print(mi_cadena)

# convertir un entero a hexadecimales
error = 500
cadena_hexadecimal=' Error en hexadecimal: %x' % error
print(cadena_hexadecimal)

# Si queremos pasar varios valores, tenemos que usar una tupla
cadena = 'Hola %s hay un error: %x' %(nombre, error)
print(cadena)

# Podemos referenciar por sustitucion de variables usando un diccionario
cadena = 'Hola %(nombre)s hay un error: %(error)x' % {'nombre':nombre, 'error':error}
print(cadena)
