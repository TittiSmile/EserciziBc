"""
È necessario scrivere uno script che richiede un valore
all'utente. Il valore deve essere utilizzato come un numero
intero in un calcolo, anche se l'utente immette un valore
decimale.
"""
print("inserisci un valore numerico (altrimenti errore): ")
valore = float(input()) # float è più grande di int quindi anche se metto int al posto di float, non dà problemi. il viceversa sì
print("valore: ", valore)

s = "ciao"
a = 5
print("stampo valore: ", a)
print("stampo valore: " , s)