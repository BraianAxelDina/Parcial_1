#Escribir un programa que le solicite al usuario ingresar una
#calificación del 0 al 100, la asigne a una variable y muestre la
#calificación alfabética correspondiente (A, B, C, D, F) según el
#numero ingresado. Correspondiendo cada letra con valores de 20 en
#20. Es decir: 0 a 19 = A, de 20 a 39 = B, etc

#En primer lugar, partimos tomando informacion del usuario

numero = int(input("Ingrese un numero: "))


#En este caso, se aplica una modificacion al rango posible de ingresar por parte del usuario
#para poder asi abarcar todo el alfabeto siguiendo la condicion establecida
#Al igual que en el caso de la estructura if, se utilizara el mismo metodo, pero esta vez analizando el rango para cada letra para asi definir que letra sera retornada
letra_Correspondiente = (
    "A" * (0 <= numero <= 19) +
    "B" * (20 <= numero <= 39) +
    "C" * (40 <= numero <= 59) +
    "D" * (60 <= numero <= 79) +
    "E" * (80 <= numero <= 99) +
    "F" * (100 <= numero <= 119) +
    "G" * (120 <= numero <= 139) +
    "H" * (140 <= numero <= 159) +
    "I" * (160 <= numero <= 179) +
    "J" * (180 <= numero <= 199) +
    "K" * (200 <= numero <= 219) +
    "L" * (220 <= numero <= 239) +
    "M" * (240 <= numero <= 259) +
    "N" * (260 <= numero <= 279) +
    "O" * (280 <= numero <= 299) +
    "P" * (300 <= numero <= 319) +
    "Q" * (320 <= numero <= 339) +
    "R" * (340 <= numero <= 359) +
    "S" * (360 <= numero <= 379) +
    "T" * (380 <= numero <= 399) +
    "U" * (400 <= numero <= 419) +
    "V" * (420 <= numero <= 439) +
    "W" * (440 <= numero <= 459) +
    "X" * (460 <= numero <= 479) +
    "Y" * (480 <= numero <= 499) +
    "Z" * (500 <= numero <= 519))
#La estructura "if" se encargara de verificar que la informacion ingresada sea de tipo "int" y que al mismo tiempo se encuentre dentro del rango establecido
if isinstance(numero, int) == True and (numero > 0 and numero < 520):
    print("La letra correspondiente al número ingresado es: ",letra_Correspondiente)
#La estructura "elif" se encarga de los casos en los cuales la informacion es de tipo "int" pero se encuentra fuero de los parametros permitidos
elif isinstance(numero, int) == True and (numero < 0 or numero > 519):
    print ("El numero ",numero," esta fuera del rango permitido.")
#Finalmente, la estructura else es la encargada de informar algun error inesperado. Esto dado que al utilizar "int" en el input, el programa generara una excepcion al momento
#de intentar ingresar cualquier informacion no numerica. 
else:
    print ("Error inesperado")


