# anche in python come in java esistono le funzioni nidificate :D
def outer(a,b):         # dichiaro una funzione con 2 parametri
    def inner(x,y):     # funzione interna con 2 parametri
        return x+y      # ritorno la somma dei parametri della funzione interna

    print(inner(a,b))   # nella funzione outer, stampo la funzione inner (chiaramente a e b sono passati come parametri)

outer(1,2)              # fuori da tutto, richiamo outer che andrà a stampare la somma da inner!
# chiaramente non posso fare un'invocazione di una classe interna... sarebbe errore
"""in JAVA o C una cosa del genere non esiste. al più, in java, abbiamo le classi nidificate."""




"""def outerFunc():
    def innerFunc():
        a = 10
        b = 1
        print(a+b)      sto stampando nella classe interna... chiaramente questo è fine a se stesso perchè l'esterna non
                        vede la stampa... può accedere, al più, al risultato di ritorno della funzione

print(outerClass())"""