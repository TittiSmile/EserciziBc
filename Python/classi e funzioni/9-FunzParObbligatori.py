# esempio di funzioni con parametri obbligatori

def f(a,b,c=4,d=11):
    print(a, b, c, d)

f(1, 2)      # passo solo a e b (rispettivamente 1 e 2).
# in questo caso, a e b sono OBBLIGATORI mentre c e d sono OPZIONALI e, in questo caso, contengono un valore di default

f(4,11,9,5)     # il valore di default di c e d può essere tranquillamente sovrascritto...
                # se ti sta bene quello di f te lo tieni sennò lo cambi

# CHIARAMENTE, devo specificare per forza i parametri a e b altrimenti mi dà errore

f(a=5,b=1,c=22,d=555)   # posso usare la keyword per tutti quanti e non se ne parla più :D