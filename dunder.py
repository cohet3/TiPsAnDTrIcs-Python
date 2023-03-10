#dunder = Double underscore

class Padre:
    def __init__(self):
        # Al usar dunder (double underscore) al inicio y al final
        # No se aplica el conceptoo de name mangling
        self.__variable_privada = 10
        self.__variable_dunder__ = 15



if __name__ == '__main__':
    padre = Padre()
    print(dir(padre))
    print(f' Accediendo a la variable privada: {padre._Padre__variable_privada}')
    print(f' Accediendo a la variable dunder: {padre.__variable_dunder__}')