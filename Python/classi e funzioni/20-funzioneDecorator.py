
def funz1(f):
    def decorator():            # è la keyword della funzione decoratore. si trova internamente ad una funzione
                                # fa qualcosa e poi al suo interno ha la funzione dichiarata come parametro nella
                                # funzione esterna.
        print("funzione decoratore")
        f()
    return decorator

@funz1                          # richiamo direttamente la funzione
def funz2():
    print("funzione normale")

funz2()



"""anche in java esistono i decoratori. sono solo diversi concettualmente. i decoratori java servono solo a rendere
il codice più pulito... (ad esempio usando @override)
qui il concetto è diverso, ti va a sostituire proprio una parte di codice..."""