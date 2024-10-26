#a. Escribir un programa que muestre los números del 1 al 10
#utilizando un bucle for.

#Se agrega una estructura interna if-else para dar un formateo a la impresion de la informacion. Esto no afecta de ninguna forma a la consigna
#dado que el bucle for es el encargado de generar la informacion para cada impresion
for numero in range(1, 11):
    if numero < 10:
        print(numero, end=", ")
    else:
        print(numero)


#b. Escribir un programa que muestre la suma de los números del
#1 al 100.
#Para realizar la sumatoria de todos los numeros del 1 al 100, generamos un bucle que por cada iteracion, incremente el valor de la variable suma (iniciado en 0 como contador)
#por el valor del numero actual dentro del rango
suma = 0
for numero in range(1, 101):
    suma += numero

print("La suma de los números del 1 al 100 es:", suma)


