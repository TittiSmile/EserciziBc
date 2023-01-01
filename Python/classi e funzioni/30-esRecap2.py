"""
Si creino due funzioni a partire da un input dato: una funzione “vocali” e una funzione “cerca palindromi”,
con la gestione dell’errore nel caso il parametro è alfanumerico. Nel primo caso si deve considerare
l'input di un carattere da parte dell'utente, nel secondo caso l'input di una parola
"""
def palindromi(parola):
   dim = len(parola)
   i = 0
   if dim == 0 or dim == 1:
       print("parola troppo corta")
   else:
       while i < dim:
           pass
       #FINISCI

parola = input("inserisci una parola ")
"""lista =[parola]
print(lista)"""
palindromi(parola)


##########################################################################
def vocali(carattere):
   if len(carattere) > 1:
       print("hai inserito una stringa")
   else:
       if carattere == "a" or carattere == "e" or carattere == "i" or carattere == "o" or carattere == "u":
           print("vocale")
       else:
           print("consonante")


carattere = input("inserisci un carattere ")      
vocali(carattere)



"""
if dim == 0 or dim == 1:
    print("parola troppo breve. non palindroma")
else:
    while i < (dim / 2) and lista[i] == lista[dim - i - 1]:
        if i == dim / 2:
            print("palindroma")
        else:
            print("non palindroma")
        i += 1"""