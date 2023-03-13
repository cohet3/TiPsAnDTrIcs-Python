# ABC - Abstract Bse Class
# ABC permite escribir una jerarquia de clases mar robusta y codigo mas mantenible
#nos permite asegurar que las clases q heredan implementen los metodos
#Ej. Sin usar ABC y los posibles problemas
from abc import ABCMeta, abstractmethod


class ClaseBase1:
    def metodo_1(self):
        raise  NotImplementedError
    def metodo_2(self):
        raise NotImplementedError
class ClaseConcreta1(ClaseBase1):
    # Implementacion de la clase padre
    def metodo_1(self):
        print('Metodo 1 implementado...')
        #el metodo 2 no se va a implementar
        # Esto ya es un problema porq no se reporta la falta de implementacion
# Hay un problema , se puede instanciar la clase Base
clase_base = ClaseBase1()
# clase_base.metodo_1()
# Esto funciona segun lo esperado
clase_concreta = ClaseConcreta1()
# clase_concreta.metodo_1()
# El metodo2 , se llama el metodo heredado
# clase_concreta.metodo_2()
# Vamos a resolver los detalles anteriores usando ABC
class ClaseBase2(metaclass=ABCMeta):
    # No tenemos que agregar la implementacion al ser un metodo abstrabto
    @abstractmethod
    def metodo_1(self):
        pass
    @abstractmethod
    def metodo_2(self):
        pass
class ClaseConcreta2(ClaseBase2):
    def metodo_1(self):
        print('Metodo 1 implementado...')
    # estamos obligados a implementar todos los metodos abstractos
    def metodo_2(self):
        print('metodo 2 implementado')
# Intentamos crear un objeto de la clase base no es posible
# clase_base = ClaseBase2()

# Instanciamos la clase 2
clase_concreta = ClaseConcreta2()
clase_concreta.metodo_1()
clase_concreta.metodo_2()

