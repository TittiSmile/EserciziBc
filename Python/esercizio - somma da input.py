print("inserisci il primo valore: ")
a = int(input())
print("inserisci il secondo valore: ")
b = int(input())
somma = a + b
print("primo valore: " ,  a , "\nsecondo valore: ", b, "\nsomma dei valori: ", somma)
# ATTENZIONE AL CAST DI RIGA 2 E 4!!!! se non avessi messo il cast, avrebbe considerato a e b come 2 strinche perchè di
# default il loro tipo è string!!!! quindi, quando avrei messo somma, mi avrebbe concatenato le due stringhe senza fare la somma!
