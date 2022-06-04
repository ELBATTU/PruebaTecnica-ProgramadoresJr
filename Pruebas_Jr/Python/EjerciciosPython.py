import re
##1.- Invertir una cadena
##String = String = input("Ingrese una cadena: ")
print ("INVERTIR UNA CADENA\n")
##FORMA 1
print ("FORMA 1")
String = "Hola Mundo"
String = String[::-1]
print("La cadena invertida es: ", String,"\n")
##FORMA 2
print ("FORMA 2")
def invertirCadena(cadena):
    cadena = cadena[::-1]
    return cadena
print("La cadena invertida es: ",invertirCadena("Hola Mundo"),"\n")

##2.- Calcular cuantas veces se repite un caracter en una cadena
##String = String = input("Ingrese una cadena: ")
print ("CALCULAR CUANTAS VECES SE REPITE UN CARACTER EN UNA CADENA\n")
##FORMA 1
print ("FORMA 1")
String = "Hola Mundo"
contador = 0
for i in range(len(String)):
    if String[i] == "o":
        contador += 1
print("El caracter 'o' se repite: ", contador," veces\n")
##FORMA 2
print ("FORMA 2")
def contarCaracter(cadena, caracter):
    contador = 0
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            contador += 1
    return contador
print("El caracter 'o' se repite: ", contador," veces\n")
##FORMA 3
print ("FORMA 3")
print ("El caracter 'o' se repite: ", String.count('o')," veces\n")

##3.- Distancia de Hamming
##String = String = input("Ingrese una cadena: ")
print ("DISTANCIA DE HAMMING\n")
String1 = "patitosw"
String2 = "paratosa"
distancia = 0
if(len(String1) != len(String2)):
    print("Las cadenas no tienen la misma longitud")
for i in range(len(String1)):
    if String1[i] != String2[i]:
        distancia += 1
print("La distancia de Hamming es: ", distancia,"\n")

##4.- Contador de palabras de una cadena
##String = String = input("Ingrese una cadena: ")
print ("CONTADOR DE PALABRAS DE UNA CADENA\n")
Stringt = "    un   texto     con  muchas    palabras "
contador = 0
for i in range(len(Stringt)):
    if Stringt[i] == " ":
        contador -= 1
    else:
        contador += 1
print("El numero de palabras es: ", contador,"\n")

##5.- Contador de numeros de una cadena
##String = String = input("Ingrese una cadena: ")
print ("CONTADOR DE NUMEROS DE UNA CADENA\n")
text = "an1298jq???da!22121230001masA"
pattern = '[0-9]'
regex = re.findall(pattern, text)
print("La cantidad de numeros es: ", len(regex),"\n")



