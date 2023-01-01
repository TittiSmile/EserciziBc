class A:
    x = 1

class B:
    x = 2

class C(A,B):
    x = 3

c = C()
print(c.x)      # stampa 3


"""
ereditarietà multipla.
praticamente, per ovviare al problema che se eredito tutto da tutti ed estendo tutte le classi del mondo, python si è inventato
questo metodo super affascinante.

abbiamo 3 attributi/variabili con lo stesso nome. 
c.x stampa 3 -> perchè fa capo all'attributo x che si trova in C
c.x stampa 2 -> quando tolgo l'attributo x da C e, allo stesso tempo, dichiaro C(B,A). il sistema di python risale alla prima 
                superclasse dichiarata (in questo caso B) e stampa la x di B cioè 2
c.x stampa 1 -> quando tolgo l'attributo x da C e, allo stesso tempo, dichiaro C(A,B). python "risale" gerarchicamente alla ricerca
                della prima classe scritta nel parametro della dichiarazione di C e va a prendere quello.
                
la regola a cui fa capo python è la regola MRO:
-l'attributo si ricerca nella classe stessa. se è presente, si prende quello altrimenti...
    - ricerco l'attributo nella gerarchia salendo di 1 livello andando a vedere l'ORDINE di dichiarazione. 


"""
