#Creacion de variable tipo lista con contenido de 3 valores con diferentes tipos
#[0] = int, [1]= string , [2]= bool
mi_lista = [1, "Uno", True]
print ("Contenido de la lista en estado inicializado: ",mi_lista)
#Adicion de un nuevo elemento en la ultima posicion de la lista utilizando append()
mi_lista.append("Hola")
print ("Contenido de la lista luego de adicion mediante append: ",mi_lista)
#Modificacion de valor de elemento en posicion inicial
mi_lista[0] = 2
print ("Contenido de la lista luego de modificacion de valor en posicion inicial: ",mi_lista)
#Eliminacion del ultimo elemento en la lista mediante pop()
mi_lista.pop()
print ("Contenido de la lista luego de eliminacion de ultimo elemento mediante pop: ",mi_lista)
#Presentacion del contenido de la lista
print ("Contenido de la lista final: ",mi_lista)

