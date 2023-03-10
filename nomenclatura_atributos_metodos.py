# from  mi_modulo import _funcion_protegida
# from  mi_modulo import funcion_publica
#
#
# class MiClase:
#     def __init__(self):
#         self.mi_variable_publica = 10
#         self._mi_variable_protegida = 11
# # Creamos la prueba de la clase
# if __name__ == '__main__':
#     objeto = MiClase()
#     print(objeto.mi_variable_publica)
#     # No deberiamos acceder a atributos o metodos con un guion bajo al inicio
#     print(objeto._mi_variable_protegida)
#
#     # Accedemos a las funciones del modulo importado
#     funcion_publica()
#     # Si utilizamos el import * no se puede acceder a las funciones que empiezan con guion bajo
#     _funcion_protegida()



# El guion bajo al final se usa para evitar conflictos con nombres (keywords)
#Ej. class, def, etc
def funcion1(nombre,class_):
    print('funcion que recibe una clase', nombre, class_)

#llamamos la funcion
funcion1('Juan', None)
