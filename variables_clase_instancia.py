
# Diferencia entre variables de clase y de instancia(objeto)
class Perro:
    no_patas = 4 # Variable de clase
    def __init__(self, nombre):
        self.nombre = nombre  # variable de instancia
# Definimos objetos
layla = Perro('Layla')
venus = Perro('Venus')
# Cada objeto tiene su porpio atributo de nombre
print(layla.nombre, venus.nombre)
# la var de clase se puede acceder con el nombre de la clase o con los objetos
print(layla.no_patas, venus.no_patas, Perro.no_patas)
# Si tratamos de acceder la variable de instancia desde la clase no es posible
# print(Perro.nombre)

# si queremos modificar el no_patas para todos los perros
Perro.no_patas = 5
print(layla.no_patas, venus.no_patas, Perro.no_patas)

# Si queremos modificar el no_patas para un solo perro
venus.no_patas = 6
print(layla.no_patas, venus.no_patas, Perro.no_patas)
# Imprimimos el valor de la variable de instancia y ademas la variable declase
print(venus.no_patas, venus.__class__.no_patas)

# Si creamos una variable desde la clase
Perro.nombre = 'Clase Perro'
print(layla.nombre, venus.nombre, Perro.nombre)
# si definimos una variable de clase q no esta en los objetos
Perro.no_orejas = 2
print(layla.no_orejas, venus.no_orejas, Perro.no_orejas)

# Contador de objetos de una clase
# Implementacion Erronea
class ContadorObejtoErronea:
    no_instancias =  0
    def __init__(self):
        # aca esta el erro
        self.no_instancias += 1

print('Contador de instancias Erroneo: ')
print(ContadorObejtoErronea.no_instancias)
print(ContadorObejtoErronea().no_instancias)
print(ContadorObejtoErronea().no_instancias)

# Implementacion corregida
class ContadorObejtos:
    no_instancias = 0
    def __init__(self):
        # Incrementamos la variable de clase
        self.__class__.no_instancias +=1
print('Contador Instancias: ')
print(ContadorObejtos.no_instancias)
print(ContadorObejtos().no_instancias)
print(ContadorObejtos().no_instancias)
print(ContadorObejtos().no_instancias)
print(ContadorObejtos().no_instancias)
print(ContadorObejtos.no_instancias)