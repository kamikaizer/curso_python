def conversor(tipo_pesos, valor_dolar):
    pesos = input("indica cuantos Pesos " + tipo_pesos + " tienes: ")
    pesos = float(pesos) ##transforma el valor en un numero decimal
    dolares = pesos / valor_dolar ##op para calcular el cambio
    dolares = round(dolares, 2)  ##redondea decimales
    dolares = str(dolares) #trasnforma en str
    print("Tienes $" + dolares + " " + "dolares") ##imprime el campo dolar mas texto


menu = """
Conversor de monedas 📀

1 - Pesos colombianos
2 - Pesos Argentino
3 - Pesos chilenos

Elije una opcion: """ ##triple comilla genera un cuadro de texto


opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)  ## linea 1 se definio el parametro conversor con ("tipo moneda", "valor moneda")
elif opcion == 2:
    conversor("argentino", 65)
elif opcion == 3:
    conversor("chilenos", 750)
else:
     print("Porfavor ingresa una opcion")

