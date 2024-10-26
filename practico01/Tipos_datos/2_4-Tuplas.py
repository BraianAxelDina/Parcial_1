#Creacion de tupla con tres tipos diferentes de datos
#siendo estos int, string y bool
mi_tupla=(1, "Uno", True)
#Creacion de tupla con unico elemento e impresion de tipo de dato
#Se imprimen el tipo de de la variable al igual que del contenido
#dado que no se termina de comprender cual de los dos se solicita
tupla_elemento_unico=("Hola",)
no_tupla_elemento_unico=("Hola")
#La razon de la existencia de la coma luego del unico valor dentro de la variable de tupla con elemento unico es que,
#dada la forma en la que trabaja el lenguaje, si agregamos un valor a la variable, entre parentesis SIN agregar una coma luego del elemento
#el lenguaje interpreta la informacion entre parentesis como una agrupacion de expresion regular, no como una tupla.
#Se agrega un print adicional, no solicitado en el trabajo, para demostrar dicho caso
print ("Tipo de dato de variable:",type(tupla_elemento_unico))
print ("Tipo de dato de contenido de la variable: ",type(tupla_elemento_unico[0]))
print ("Tipo de dato de variable demostrativa de comentario:",type(no_tupla_elemento_unico))


