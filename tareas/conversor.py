dolares = input("indica cuantos dolares: ")
dolares = float(dolares) ##transforma el valor en un numero decimal
valor_peso = 750
pesos = dolares * valor_peso
pesos = int(pesos)
##pesos = round(pesos, 0) redondea a 2 decimales
pesos = str(pesos) ##se conveirte el valor de pesos a texto
print("Tienes $" + pesos + " " + "CLP")