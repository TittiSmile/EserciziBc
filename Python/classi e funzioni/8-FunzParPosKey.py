# esempio di funzioni parametriche posizionali E keyword
# si possono unire le due tecniche di parametri.

def f(a,b,c,d):
    print(a,b,c,d)

f(10,4,c=11,d=51)       # uso sia parametri passati come numeri (posizionali) che keyword(c=11...)
                        # più in particolar modo, 10 e 4 sono POSIZIONALI, c e d sono KEYWORD

# è importante che l'ordine delle keyword sia lo stesso dei posizionali sennò c'è errore!!



# f(10,3,a=4,c=1) # ERRORE!!!!!!
#questo perchè a è in posizione 1 e c è in posizione 3 e qui, invece, prende la posizione di d.
# l'ordine posizionale viene dato dai parametri dichiarti dalla funzione. quindi bisogna attenersi a quelli!!!




# f(1,2,d=5,c=11)   # anche qui, ERRORE!!!!! devono avere il giusto ordine.