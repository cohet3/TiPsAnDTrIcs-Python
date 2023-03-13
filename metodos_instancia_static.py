# Metodos de instancia, clase y static y sus diferencias
class MiClase:
    def metodo_instancia(self):
       # Retornamos una tupla
        return 'Metodo de instancia ejecutado...', self

    @classmethod
    def metodo_clase(cls):
        # Retornar una tupla
        return ' Metodo de clase ejecutado...', cls
    @staticmethod
    def metodo_estatico():
        return ' Metodo estatico ejecutado...'

# Caso 1 . Ejecutamos el metodo de instancia
objeto =  MiClase()
print(objeto.metodo_instancia())
# Caso 2 . Ejecutamos el metodo de instancia de manera explicita
print(MiClase.metodo_instancia(objeto))
# Caso 3. Ejecutamos el metodo de instancia desde la clase
print(MiClase.metodo_instancia(MiClase))
# Caso 4. Ejecutamos el metodo de clase
print(MiClase.metodo_clase())
# Caso 5. Desde las instancias podemos acceder a los metodos de clase
print(objeto.metodo_clase())
# Caso 6. Ejecutamos el metodo estatico
print(MiClase.metodo_estatico())
# Caso7 desde la instancia
print(objeto.metodo_estatico())