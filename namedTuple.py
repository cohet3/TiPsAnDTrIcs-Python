 # Namedtuples son una extencion del tipo tupla
  #Son una alternativa para escribir claSES  (ATRIBUTOS TIPOS IMUTABLES)
 # Asiganar un identificador a cada elemento de la tupla

from  collections import namedtuple
#Definimos una clase con atributos inmutables usando namedtuple
Persona1 = namedtuple('Persona1',  'nombre apellido edad')
# Creamos una instancia de la clase( se agrega un constructor por default con los atributos )
persona1 = Persona1('JUan', 'Robles', 22)
# En automatico se crea un metodo __repr__ con los atributos que ha proporcionado
print(persona1)
# Creamos nuestra clase con los atrib usando una lista
Persona2 = namedtuple('Persona1',  ['nombre', 'apellido','edad'])
persona2 = Persona2('Karla', 'Gonmes', 30)
print(persona2)

# Podemos acceder a los atributos de manera individual por nombre
print(f'Nombre {persona2.nombre}')
print(f'apellido {persona2.apellido}')
print(f'edad {persona2.edad}')
# Acceder a los atributos por indice
print(f'Nombre {persona2[0]}')
print(f'apellido {persona2[1]}')
print(f'edad {persona2[2]}')
# Podemos convertir los valores a una tupla
print(tuple(persona2))
# Podemos hacer unpacking de los elementos de la tupla
nombre, apellido, edad = persona2
print(f'Valores tupla persona: {nombre}, {apellido}, {edad}')
# Podemos hacer unpacking pasando como argumento
print(*persona2)
# LAs tuplas son inmutables al igual que namedtuple
# persona2.edad = 38

# Subclases de namedtuples
class Persona3(Persona2):
    # Agregamos un nuevo metodo a la clase hija
 def convertir_mayus(self):
     return f'Nombre completo: {self.nombre.upper()} {self.apellido.upper()}'

persona3 = Persona3('MAria','Lara',35)
print(persona3.convertir_mayus())

# Existe otra forma de hacer extends de la clase( la forma recomendadada)
Persona4 = namedtuple('Persona4', Persona2._fields + ('email',))
# Creamos un onjeto de la clase persona4 con el nuevo atributoi
persona4 = Persona4('Armando', ' Quintero', 34, 'armando@gmail.com')
print(persona4)

#Metodos de ayuda build -in en namedtupleç
print(persona4._fields)
# Ej. convertir a un diccionario
diccionario_persona4 = persona4._asdict()
print(diccionario_persona4)
