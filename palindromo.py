def palindromo(palabra):
    palabra = palabra.lower()    #convierte palabra/frase en minusculas
    palabra = palabra.replace(" ", "")    #Quita los espacios entre las palabras de una frase
    palabra = palabra.replace("á", "a")    #Quita las tildes
    palabra = palabra.replace("é", "e")    #Quita las tildes
    palabra = palabra.replace("í", "i")    #Quita las tildes
    palabra = palabra.replace("ó", "o")    #Quita las tildes
    palabra = palabra.replace("ú", "u")    #Quita las tildes

    a = 0                                # empieza en la posicion 0 es decir el inicio de la palabra
    b = len(palabra) -1                  # empieza en la ultima posicion 

    for i in range(0, len(palabra)):     # usamos un ciclo for  para ir recorriendo la palabra
        if palabra[a] == palabra[b]:     # aqui se comparan amabas posiciones
            a += 1
            b -= 1
        else:
            return False                 # si no son iguales entonces devuelve un false

    return True                          # si se cumple el ciclo entonces en true

palabra = input("Ingresa una palabra o frase: ")
if palindromo(palabra):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
