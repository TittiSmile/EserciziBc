# esempio sulle classi in python

# classe semplice
class A:        # dichiarazione di una classe di nome (impropriamente: tipo) A
    x = 10  # dichiaro una variabile x (sottinteso di tipo int) con valore di 10
    print("classe A: ")
    print(x)    # stampo la variabile x
# ATTENZIONE!!! se avessi stampato in maniera non indentata rispetto ad A, ci sarebbe stato errore



# classe che ne estende un'altra
class B (A):        # classe B che estende A. l'estensione si nota come parametro nella classe
    y = 5           # dichiaro una variabile a cui assegno 5
    x = 11          # dichiaro una variabile x a cui assegno 11 (anche se c'è già x in A)
    print("\nclasse B:" )
    print(y)
    print(x)



class C (B, A): # questa classe estende sia A che B.
                # ATTENZIONE!!!!! l'ordine di estensione è importante! visto che python va avanti tramite il
                # concetto di MRO (cioè sale piano piano su con le classi), bisogna dichiarare (come estenzione)
                # prima la classe creata per ultima e poi quella principale. nel senso: B estende A ed A non
                # estende nessuno. va messo prima B perchè è a sua volta una classe che estende.
    zz = 1
    tt = 3
    print("\nclasse C:")
    print(zz)
    print(tt)
    # print(x)        # C eredita il parametro x da A ma se lo stampo, non rilascerà nulla
                      # (darà errore perchè non è stato definito...
