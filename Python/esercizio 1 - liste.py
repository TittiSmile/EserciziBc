"""
data una lista
-si stampi il contenuto
-si verifichi la dimensione
-verificare le proprietà
-estrai elementi
"""
x=10
l = [1,2,4] #dichiarazione della lista
print("stampo la lista: ", l)
print("lunghezza lista: ", len(l))
print("informazioni lista: ", dir(l))
print("tipo della lista: ", type(l))
print("valore di posizione 1: ", l[1])
print("identità della lista: ", id(l))
print(l[0])
l[0] = 44 #cambio valore all'elemento 0 della lista
print("stampo lista modificata: ", l) #mi stamperà 44 al posto di 1

#######################################

l2 = [1,2,"ciao", 4.5] #le liste in python, a differenza di altri linguaggi, contengono oggetti generici. quindi possono avere tipi
                        #diversi. questo perchè in python non esiste un vero e proprio tipo
print("lista 2: ", l2);


