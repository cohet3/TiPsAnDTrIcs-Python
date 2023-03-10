from contextlib import contextmanager

with open('prueba.txt','w') as archivo:
    archivo.write('Hola desde Python')

# Esto es equivalente a:
# archivo = open('prueba.txt', 'w')
# try:
#     archivo.write('hola desde Python')
# finally:
#     archivo.close()

# Esto NO es equivalente
archivo= open('prueba.txt', 'w')
archivo.write('hola sin with')
# Esto no asegura el cierre de recursos en caso de error
archivo.close()
# Manejo de Context Manager en clases
# 1. Implementando el protocolo con las funciones(__enter__) y (__exit__)
# 2. utilizando la libreria de contextlib

# Veamos la opcion 1
class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        self.archivo= open (self.nombre, 'w')
        return self.archivo
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.archivo:
            self.archivo.close()

# Este metodo es un generador, en primer lugar adquiere el recuerso
# posteriormente suspende temporalmente la ejecución al utilizar yield
# cuando termina de ser utilizado este metodo, regresa a la ejecución y cierra el recurso
@contextmanager
def manejador_archivos(nombre):
    try:
        archivo = open(nombre, 'w')
        yield archivo
    finally:
        archivo.close()
# Ejercicio de identador
class Identador():
    def __init__(self):
        self.nivel = 0
    def __enter__(self):
        self.nivel += 1
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.nivel -= 1
    def imprimir(self, texto):
        print('  '*self.nivel + texto)


# Mismo ejercicio de identador con contextlib
class Identador2():
    def __init__(self):
        self.nivel = 0
    @contextmanager
    def identador(self):
        try:
            self.nivel += 1
            yield self
        finally:
            self.nivel -= 1
    def imprimir(self, texto):
        print('  ' * self.nivel + texto)

if __name__ == '__main__':
    # Prueba implementando el protocolo de Context Manager
    with ManejoArchivos('prueba.txt') as archivo:
        archivo.write('prueba desde ManejoArchivo')

    # Prueba con la libreria de contextlib
    with manejador_archivos('prueba.txt') as archivo:
        archivo.write('prueba desde decorador')
        archivo.write('\nadios')

    # Prueba de Identador
    with Identador() as identador:
        identador.imprimir('primer nivel')
        with identador:
            identador.imprimir('segundo nivel')
            identador.imprimir('continua segundo nivel')
            with identador:
                identador.imprimir('segundo tercer')
                with identador:
                    identador.imprimir('segundo cuarto')
    with identador:
        identador.imprimir('fin primer nivel')

    # Prueba Identador2
    print()
    objeto = Identador2()
    with objeto.identador():
        objeto.imprimir('primer objeto')
        with objeto.identador():
            objeto.imprimir('segundo nivel')
            with objeto.identador():
                objeto.imprimir('tercero nivel')
                with objeto.identador():
                    objeto.imprimir('cuarto nivel')
                    with objeto.identador():
                        objeto.imprimir('quinto nivel')
                        with objeto.identador():
                            objeto.imprimir('sexto nivel')
    with objeto.identador():
        objeto.imprimir('7 nivel')
