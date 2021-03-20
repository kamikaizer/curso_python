dolares = input("indica cuantos dolares: ")
dolares = float(dolares) ##transforma el valor en un numero decimal
valor_peso = 750
pesos = dolares * valor_peso
pesos = round(pesos, 2) ##redondea a 2 decimales
pesos = str(pesos) ##se conveirte el valor del dolar a texto
print("Tienes $" + pesos + " " + "CLP")