def palindromo(palabra):
    palabra = palabra.replace(' ', '') ##elimina los espacios
    palabra = palabra.lower() ##deja todo en minuscula
    palabra_invertida = palabra[::-1] ##invierte la palabra
    if palabra == palabra_invertida: ##verifica que la palabra invertida sea igual o no a la palanbra incial
        return True
    else:
        return False


def run():
    palabra = input("escrube la palabra: ") ##input
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("es palindromo")
    else:
        print("no es palindromo")


if __name__ == '__main__':
    run()



