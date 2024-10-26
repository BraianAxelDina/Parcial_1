#Escribir un script que le asigne a una variable un número y
#muestre si es positivo, negativo o cero. Utilizando unicamente la
#sentencia IF.

#Si bien este problema puede ser aproximado haciendo uso 3 veces de la estructura "if", se tomara una aproximacion 
#mas complicada, pero que a nivel estructural parece mas logica y limpia

numero = 0
#En primer lugar, tomamos como posibilidad que el usuario intentase ingresar
#algo que no fuese un numero, por ende necesitamos controlar esto
#En caso que esto no fuese a ocurrir, se sugiere comentar esta seccion

#while True:
#    try:
#        numero = int(input("Ingrese un numero: "))
#        break
#    except:
#        print("¡Ingreso un numero invalido o un tipo de dato no numerico!")
        
#A continuacion, el caso en el que el usuario siempre ingresara informacion
#numerica. ¡Dejar solo descomentada una de las dos opciones!

numero = int(input("Ingrese un numero: "))

#Luego de captar el numero ingresado por el usuario, y almacenarlo, procedemos a 
#analizar que tipo de condicion cumple el numero.
#Para esto, utilizaremos una variable que contendra strings, operaciones logicas
# y concatenaciones entre ellos.

tipo_Num = ("El número es positivo" * (numero > 0) + \
            "El número es negativo" * (numero < 0) + \
            "El número es neutro" * (numero == 0))


#Lo que ocurre aqui es lo siguiente. Al analizar la variable numero con una comparacion
#esto arrojara siempre un valor bool, el cual puede ser interpretado como (1 = true o 0 = false)
#en cada seccion de la variable.
#Teniendo estos resultados, en python, la multiplicacion de strings por un entero 
#causa una repeticion del string, dicho número de veces.
#Considerando entonces, que siempre habra solo 1 condicion que arrojara positiva y que, un string multiplicado
#por 0 siempre resultara en "", determinamos, por ejemplo, que una situacion posible podria ser:
# "" + "" + "El numero es neutro".
#Lo cual, al momento de imprimir, la concatenacion presentaria:
#"El numero es neutro"
#Esto nos permite entonces realizar lo siguiente:
if numero != None:
    print (tipo_Num)

#Planteando la condicion "Numero != None" causamos que mientras "numero" no demuestre falta de valor (caso que nunca se dara siempre y cuando se utilize el metodo de captado
#del valor al usuario correspondiente al escenario), presente la informacion correspondiente