# Crear una clase para definir una clase de excepcion personalizada
# ej. Validar que un nombre no pueda tener mas de tres caracteres

  # Este tipo de validacion no indica cual es el problema en especifico
def validar(nombre_completo):
    if len(nombre_completo) < 3:
        raise ValueError
    else:
        print('Validacion correcta...')
nombre = 'juanmagane'
validar(nombre)
# Validacion personalizada, indica cual es el problema, y queda autodocumentado
# class NombreDemasiadoCorto(ValueError):
#     pass
# def validar_mejorado(nombre_completo):
#     if len(nombre_completo) < 3:
#         raise  NombreDemasiadoCorto(nombre_completo)
#     else:
#         print('validation nice...')
#
# nombre='Ka'
# validar_mejorado(nombre)

# Es buena idea crear una clase base de alli extender las demas clases
class ClaseExcepcionBase(TypeError):
    pass

class NombreDemasiadoCorto(ClaseExcepcionBase):
    pass
def validar_mejorado(nombre_completo):
    if len(nombre_completo) < 3:
        raise NombreDemasiadoCorto(nombre_completo)
    else:
        print('validation nice...')
nombre='Ka'
try:
    validar_mejorado(nombre)
except ClaseExcepcionBase as e:
    print(f'{type(e).__name__}, linea {e.__traceback__.tb_lineno} en {__file__}: {e}')
    