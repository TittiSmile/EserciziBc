# cioè si esce fuori da un intervallo stabilito

l = [1, 2, 3, 4]
indice = int(input("inserisci un indice: "))
try:
    print(l[indice])
except IndexError as i:     # alias facoltativo. mettere IndexError è ancora facoltativo
    print("errore di indice")
else:
    print("indice corretto")
finally:
    print("sono nel finally")

"""else DOPO except vuol dire che non è andato in eccezione quindi ti stampa quando tutto va bene! ne posso avere
solo 1 dopo except"""

"""se non avessi usato try except, il compilatore, all'inserimento di indice > 3, mi avrebbe dato errore.
così facendo, invece, gli faccio stampare comunque un errore ma lo decido io"""







"""in JAVA quando abbiamo try-catch, devo PER FORZA mettere il tipo di eccezione giusta sennò fa problemi
chiaramente, NON esiste ELSE in Java (dopo try-catch). al più abbiamo finally. """