#Cracion de variable y asignacion de valor. Contenido tipo String
mi_nombre="Braian Axel"
#Presentar por pantalla el tipo de la variable
print ("El tipo de la variable es" , type(mi_nombre) , "\n")
#Acceder y mostrar la primera y ultima letra de la variable usando indices
#Para esto, sabemos que el primer valor de todo string comienza en la posicion 0, pudiendo entonces establecer con dicha posicion, siempre la primera letra.
#para el ultimo valor, podemos utilizar la funcion len que retorna la longitud de un string y restarle 1. La resta es debido a que el conteo ignora la posicion inicial
#Por ende, si utilizamos su retorno puro, obtendremos un error de tipo "string index out of range". Restandole 1, podemos acceder siempre a la ultima posicion, sin importar
#Que tan grande sea la cadena
#Asteriscos agregados en los laterales de cada letra para mayor legibilidad
print ("El contenido de la variable en la posicion inicial es *",mi_nombre[0],"* y su contenido en la ultima posicion es *",mi_nombre[len(mi_nombre)-1],"*\n")
#Uso de la funcion len() para calcular longitud de string y presentar por pantalla
print ("El string contenido por la variable posee una longitud total de ", len(mi_nombre),"\n")
#Impresion del contenido de la variable completa en mayuscula y minuscula
print ("El contenido del string original es: ",mi_nombre)
print ("El contenido del string en minuscula, es: ",mi_nombre.lower())
print ("Y, finalmente, el contenido del string en mayuscula, es: ",mi_nombre.upper())
