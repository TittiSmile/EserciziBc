# init, in python, è visto come un costruttore in java. 
# anche se init non viene specificato, esiste lo stesso. è un costruttore ja ja ja
# init viene chiamato anche metodo magico, è facoltativo però. può anche non starci

class myClass():
    def __init__(self):
        print("sono nel metodo magico init")


obj = myClass()
obj.attr = 10   # attributo di istanza!!!! non è presente in myClass. solo obj può accedervi e visualizzarlo
print(obj.attr)
# come si può notare, quando si va a stampare l'attributo di istanza, non solo si stamperà 10 (valore assegnato ad attr)
# ma si stamperà anche la stampa di init. questo perchè init è intrinseco nella classe myClass.
# il suo parametro è self ma non gli si passa nulla... è considerato vuoto

# quindi, ogni volta che stampo un attributo di istanza, mi va a stampare anche la print di init. questo perchè
# è una funzione speciale di python.
# init inizializza metodi ed attributi





#RICORDA  che se init ha dei parametri (al di là di self) gli vanno passati.




# esempio che poi devi passargli il parametro sennò fa storie... è un costruttore