menu = """
Conversor de monedas 📀

1 - Pesos chilenos
2 - Pesos Argentino
3 - Pesos mexicanos

Elije una opcion: """ ##triple comilla genera un cuadro de texto
opcion = int(input(menu))

if opcion == 1:
    
    dolares = int(input("indica cuantos Pesos Chilenos: "))
    dolares = float(dolares) ##transforma el valor en un numero decimal
    valor_peso = 750
    pesos = dolares / valor_peso
    pesos = round(pesos, 2) ##redondea a 2 decimales
    pesos = str(pesos) ##se conveirte el valor del dolar a texto
    print("Tienes $" + pesos + " " + "dolares")

elif opcion == 2:

    dolares = int(input("indica cuantos Pesos Argentinos: "))
    dolares = float(dolares) ##transforma el valor en un numero decimal
    valor_peso = 65
    pesos = dolares / valor_peso
    pesos = round(pesos, 2) ##redondea a 2 decimales
    pesos = str(pesos) ##se conveirte el valor del dolar a texto
    print("Tienes $" + pesos + " " + "dolares")

elif opcion == 3:

    dolares = int(input("indica cuantos Pesos Mexicanos: "))
    dolares = float(dolares) ##transforma el valor en un numero decimal
    valor_peso = 45
    pesos = dolares / valor_peso
    pesos = round(pesos, 2) ##redondea a 2 decimales
    pesos = str(pesos) ##se conveirte el valor del dolar a texto
    print("Tienes $" + pesos + " " + "dolares")

else:
     print("Porfavor ingresa una opcion")

