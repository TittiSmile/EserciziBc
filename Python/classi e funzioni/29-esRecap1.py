"""
1. Scrivere una funzione a cui verrà passata una stringa inserita, e dovrà restituire il suo contrario.
2. Scrivere una funzione ricorsiva che calcola il fattoriale di un numero dato.
3. Scrivere una funzione che crei una lista che contenga la lunghezza delle parole inserite dall’utente. Per ciascuna
lunghezza si stampi un asterisco creando un istogramma.
"""

def istogramma(parola):
    dim = len(parola)
    i = 0
    while i < dim:
        print("*")      
        i+=1


def f1 (x):
    temp=""
    i = len(x)-1
    while i >= 0:
        temp+=x[i]
        i-=1
    print(temp)

def fattoriale(x):
    i = 1
    res = 1
    if(x<0):
        print("errore")
    elif (x==0):
        res = 0
        print(res)
    else:
        while i <= x:
            res*=i
            i+=1
        print(res)
    #return res


f1("ciao")
fattoriale(3)
istogramma("libro")


