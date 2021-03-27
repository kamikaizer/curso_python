# def imprimir_mensaje(): ##def definicion funcion
#     print('mensaje especial: ')
#     print('estoy aprendiendo a usar funciones!')    

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()


# def conversacion(mensaje): ## dentro del parentecis va el parametro (lo que cambia)
#     print('Hola')
#     print('como estas')
#     print(mensaje)
#     print('adios')

# opcion = int(input('Elije una opcion (1,2,3): '))
# if opcion == 1:
#     # print('Hola')
#     # print('como estas')
#     # print('elejiste la opcion 1')
#     # print('adios') para evitar el repetir se define primero en las linea 10 
#     conversacion('elejiste la opcion 1')
# elif opcion == 2:
#     conversacion('elejiste la opcion 2')
# elif opcion == 3:
#     conversacion('elejiste la opcion 3')
# else:
#     print('Escribe una opcion valida')

def suma(a, b):
    print('se suman dos numeros')
    resultado = a + b
    return resultado

sumatoria = suma(1, 4)
print(sumatoria)