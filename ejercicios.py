#8.-__________MAYOR DE 3 NUMEROS___________
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))

mayor = max(num1, num2, num3)  # la funcion max nos da el numero mayor de un grupo de numeros

print("El numero mayor es:", mayor)
#__________________________________________

#9.-__________SUMA DE DIGITOS______________
num = int(input("Ingresa un numero: "))

suma = 0
for digito in str(num):   # la funcion str convierte el numero en una cadena, el for recorre cada caracter
    suma += int(digito)   #  vuelve a convertir los caracteres en numeros para sumarlos

print("La suma de los digitos es:", suma)
#__________________________________________

#10.-________CONTADOR DE PALABRAS__________
frase = input("Escribe una frase: ")

palabras = frase.split()  # frase.split crea una lista con todas las palabras de la frase
cantidad = len(palabras)  # Cuenta las palabras

print("La cantidad de palabras es:", cantidad)
#__________________________________________

#11.-__________LISTA INVERSA_______________
lista = list(range(1, 11))  # Crea la lista del 1 al 10
inversa = lista[::-1] # aqui se invierte la lista

print(inversa)
#__________________________________________

#12.-__________NUMEROS ALEATORIOS__________
import random

lista = [random.randint(1, 20) for _ in range(5)] # el random.randint genera numeros aleatorios del 1 al 20 
# el for in range es para que solo sea en un rango de 5 numeros
print(lista)
#__________________________________________

#13.-__________ADIVINAR NUMERO_____________
import random

numero = random.randint(1, 10)

num_c = False    # sirve para que mientras el usuario no adivine el numero seguira siendo falso
while not num_c: # minetras no adivine entonces se seguira repitiendo el ciclo while
    intento = int(input("Adivina el numero (entre 1 y 10): "))
    
    if intento == numero: # si el numero del usuario es igual al nuumero alatorio que se genero entonces manda el mensaje 
        print(" Adivinaste el numero")
        num_c= True  # se convierte en true y termina el bucle
    elif intento < numero: 
        print("Es mayor.")  # si el numero que ingreso el usuario es menor al numero generado le da una pista de que es mayor
    else:
        print("Es menor.")  # si el numero que ingreso el usuario es mayor al numero generado le da una pista de que es menor
#__________________________________________

#14.-__________SECUWNCIA PERSONALIZADA_____________
lista = list(range(3, 61, 3))
print(lista)
#__________________________________________
