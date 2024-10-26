#Escribir un programa que tome dos números y muestre el mayor
#de ellos. Utilizando unicamente la sentencia If-else.

#Tomando como certero que el usuario siempre ingresara numeros como informacion, se procede a tomar los valores necesarios

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

if a > b:
    print ("El numero ",a," es mayor que ",b,)
else:
    print ("El numero ",b," es mayor que ",a,)

