# tip. Las aserciones nos pueden ayudar a depurar nuestros programas de errores que no podemos recuperar
# Ejempo 1. Revisamos si la division es entre 0
def dividir(a,b):
    # Nos aseguramos que el valor de b no es cero para poder continuar
    assert b != 0, 'Division entre cero'
    print(f'Resultado division : {a/b}')

# Ejemplo2 . Realizamos el calculo promedio de una lista
def obtener_promedio(calificaciones):
    # Si la lista de calificaciones esta vacia no deberia continuar el programa
    assert len(calificaciones) !=0, ' Lista de calificaciones vacia'
    print(f'El promedio de calificaciones es {sum(calificaciones)/len(calificaciones)}')

# Ejemplo3. Realizamos un descuento al producto proporcionado
def aplicar_descuento(productos, descuento):
    precio_con_descuento = productos['precio'] * (1.0 - descuento )
    print(f'Nuevo precio del producto: {precio_con_descuento}')
    assert 0<= precio_con_descuento <= productos['precio'],f'descuento invalido'
    print('Descuento valido...')
if __name__ == '__main__':
    #Prueba Ejemplo 1. Division entre cero
    dividir(10,2)
    dividir(10,10)
    # dividir(10,0)
    # Prueba del Ejemplo 2. calculo del promedio de notas
    calificaciones = [10,8,7,9]
    # calificaciones = []
    obtener_promedio(calificaciones)
    # prueba Ejemeplo3. Aplicar descuento a un producto
    productos = {'nombre':'camisa', 'precio':1500}
    aplicar_descuento(productos, 1.10)