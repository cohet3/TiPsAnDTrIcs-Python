# las funciones en python son ciudadanos de primera clase

def mayusaculas(texto):
    return texto.upper()
# Uso normal de una función
print(mayusaculas('Hola'))

# Uso de una funcion como un objeto
# ASignar la referencia de la funcion a una variable sin los parentesis

variable_funcion = mayusaculas
print(mayusaculas)
print(f'Funcion mayusculas: {mayusaculas}')
print(f' variable funcion: {variable_funcion}')

# Utilizamos la variable funcion en cualquier texto

print(variable_funcion('Nuevo texto'))
# Para demostrar que las funciones son objetos eliminamos la referencia original
# del mayusaculas

# Aun asi, podemos utilizar la funcion con la variable funcion
print(variable_funcion('Salidos....'))
# print(mayusaculas('Ya se elimino'))

#Podemos saber el nombre por default que se le asigna a una función
print(f'Nombre por default de la funcion: {variable_funcion.__name__}')

# Como almacenar una funcion es una estructura de datos (list)
lista_funciones = [mayusaculas, variable_funcion, str.upper]
print(lista_funciones)

for funcion in lista_funciones:
    print(funcion, funcion('Saludos dede la funcion'))
# también podemos acceder directamente a la funcion que deseemos
print(lista_funciones[1]('SAludos desde variable funcion'))

###############
# Podemos pasar funciones a otras funciones
# este tipo de funciones se conocen como higher-order functions
def saludar(argumento_funcion):
    # Usamos la funcion que recibimos como argumento y devolvemoms la referencia
    referencia_funcion_retornada = argumento_funcion('Hola , saludos desde la funcion')
    print(referencia_funcion_retornada)

# Llamamos la funcion saludar, pasamos la referencia de una funcion como argumento
saludar(mayusaculas)

# Podemos pasar una nueva implementacion de la funcion que pasamos como argumento
def minunsculas(texto):
    return texto.lower()
saludar(minunsculas)

# El clasico ejemplo de higher-order functions es la funcion map
# Esta funcion toma una funcion como referencia, y un iterable , llama a la funcion
# en cada elemento de iterable proporcionado
print(list(map(mayusaculas,['texto1', 'texto2', 'texto3'])))
print(list(map(minunsculas,['texto1', 'teXto2', 'texto3'])))

###################################
# funciones nidadas

def mostrar(texto):
    # Definicion de la funcion interna o anidada
    def convertir_minusculas(t):
        return t.lower()
    # una vez definida la funcion interna, la mandamos llamar
    return convertir_minusculas(texto)

    # Cada vez que se llama la funcion mostrar, se crea la funcion interna convertir minusculas
print(mostrar('Desde funcion anidada...'))

# No podemos utilizar la funcion interna desde el exterior
# convertir_minusculas('texto1')
# mostrar.convertir_minusculas('texto1')

# Retonar la funcion anidada
# Observar que en ningun momento se llama la funcion anidaada desde la fuincion externa
print(mostrar('Desde funcion anidada...'))

def hablar(volumen):
    def minusculas(texto):
        return texto.lower()
    def mayusculas(texto):
        return texto.upper()
    if volumen > 0.5:
        return mayusculas
    else:
        return minusculas

# Utilizamos la funcion anidada
print(hablar(0.6)('hablo fuerte'))
print(hablar(0.2)('hablo devil'))

variable_minusculas = hablar(0.4)
print(variable_minusculas('hablo suvemenTE'))

#################
# Closures
# Las funciones internas pueden capturar y guardar el estado dela funcion interna
def hablar(texto, volumen):
    # La funcion interna ya no recibe parametros
    #  Utiliza el estado de la funcion padre(externa)
    def minusculas():
        return texto.lower()
    def mayusculas():
        return texto.upper()
    if volumen > 0.5:
        return mayusculas()
    else:
        return minusculas()

print(hablar('hablo fuerte....', 0.8))
print(hablar('HABLO DESPACIO...', 0.2))

# oTRO EJEMPLO DE CLOSURE
# Podemos preconfigurar una funcion
def mostrar(titulo):
    # Definimos la funcion anidada
    def saludar(mensaje):
        return titulo + ' .' + mensaje
    return saludar
mostrar_ing = mostrar('Ingeniero')
mostrar_lic = mostrar('Licenciado')

# podemos seguir usando el estado de la funcion previamente configurada
# aunq el valor de titulo ya esta fuera de alcance(scope)
print(mostrar_ing('Alvaro Sanz'))
print(mostrar_lic('Alba Castaño'))

########################
# La funcion callable nos permite saber si un objeto se puede llamar o no
# Todas las funciones en python son obejtos pero no todos los objetos son funciones
print(f'Se puede llamar el objeto mostrar como funcion? {callable(mostrar)}')
print(f' Se puede llamar el objeto hablar como funcion?{callable(hablar)}')
print(f' Se puede llamar el objeto mostrar_inf como funcion?{callable(mostrar_ing)}')
print(f' se puede llamar el objeto str como funcion? {callable("cualquier texto")}')
# Si queremos que una clase defina objetos que se puedan llamar como funciones
# tenemos que sobreescribir el metodo __call__
class Mostrar:
    def __init__(self, titulo):
        self.titulo = titulo

    def __call__(self, mensaje):
        return self.titulo + ' . ' + mensaje
    # se modifica el call para q el objeto se pueda llamar comon funcion

mostrar_doc = Mostrar('Doctor')
print(mostrar_doc('Carlitos Ugalde'))