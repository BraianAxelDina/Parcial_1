#Creacion de un diccionario con tres pares Clave:valor de 3 tipos diferentes
mi_diccionario={1:2, "hola":"mundo", 4:True}
#Impresion del valor de la primera clave
print ("Valor presente en primera clave: ",mi_diccionario[1],"\n")
#Adicion de nuevo par de Clave:valor al diccionario
mi_diccionario[10] = "Adicion"
print ("Diccionario con adicion de nuevo par: ",mi_diccionario,"\n")
#Intento de modificacion de valor de la segunda clave
print ("Valor presente en segunda clave previa modificacion: ",mi_diccionario["hola"])
mi_diccionario["hola"] = "planeta"
print ("Valor presente en segunda clave posterior a modificacion: ",mi_diccionario["hola"],"\n")
#Impresion del contenido del diccionario completo en pantalla
print ("Impresion de diccionario completo, con sus previas modificaciones: ",mi_diccionario)