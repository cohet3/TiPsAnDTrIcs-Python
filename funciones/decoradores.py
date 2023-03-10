# Los decoradores permiten extender y modificar el comportamiento de las funciones
# Ejemplos comunes_ logging, seguridad, caching
# un decorador es codigo reutilizable
# primer ejempo de un decorador
def decorador_envolvente(funcion_a_decorar):
    # Recibir la funcion y regresarla
    print('Estamos dentro de la funcion decoradora')
    return funcion_a_decorar
# Ahora utilicemos este decorador
def saludar():
    return  'Saludos desde mi funcion...'
# llamamos manualmente el decorador (no es lo comun en python)
funcion_retornada = decorador_envolvente(saludar)
print(funcion_retornada)

@decorador_envolvente
def saludar_funcion_a_decorar():
    return  'Saludos desde mi funcion  A decorar...'
print(saludar_funcion_a_decorar())
# Decorador que convierte el texto a mayusculas
def mayusculas(funcion_a_decorar):
    def envolvente():
        print('antes de la llamada a la funcion a decorar')
        # Mandamos a llamar la funcion original (closure)
        resultado_original = funcion_a_decorar()
        print('despues de la llamada a la funcion a decorar')
        resultado_modificado = resultado_original.upper()
        return resultado_modificado
    return envolvente
@mayusculas
def saludar_minusculas():
    return 'hola...'
print(saludar_minusculas())
#################################################################
#decoradores multiples

# <strong><em>'hola'</em></strong>
def negrita(funcion):
    def funcion_envolvente():
        return '<strong>' + funcion() + '</strong>'
    return funcion_envolvente
def enfatizar(funcion):
    def funcion_envolvente():
        return '<em>' + funcion() + '</em>'
    return funcion_envolvente

@negrita
@enfatizar
def saludar_html():
    return 'Hola con HTML'

print(saludar_html())

###############################
# Decoradores con Argumentos
# *args y **kwargs
def decorador_con_argumentos(funcion):
    def funcion_envolvente(*args, **kwargs):
        print('se esta ejecutando guapi')
        print('args', args)
        print('kwargs', kwargs)
        # Modificar los argumentos antes de enviarlos
        lista_arg = []
        for indice, valor_tupla in enumerate(args):
            lista_arg.append(args[indice].upper())
        # agregamos mas elementos a la lista
        lista_arg.append('nuevo arg 1')
        lista_arg.append('nuevo arg 2')
        # Agregamos informacion al diccionario
        kwargs['valor1'] = 'Nuevo valor 1'
        kwargs['valor2'] = 'Nuevo valor 2'
        #Propagamos los parametros a la funcion original
        # return funcion(*args, **kwargs)
        # Propagar los valores modificados
        return funcion(*lista_arg, **kwargs)
    return funcion_envolvente

@decorador_con_argumentos
def funcion_saludar(titulo, nombre, *args, **kwargs):
    #Imprimir titulo con el nombre
    print(f'{titulo}. {nombre}')
    # Imprimimos los argumentos variables
    print('args:', args)
    print('kwargs:', kwargs)
funcion_saludar('Ingeniera','Maria Rios')