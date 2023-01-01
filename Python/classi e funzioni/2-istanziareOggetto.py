class B:
    y = 44
    # print("classe B (superclasse): ")
    # print(y)

class C:
    z = 41

class A(C,B):       # ATTENZIONE!!! l'ordine dei parametri di estensione, qui, è INDIFFERENTE.
                    # questo perchè C e B sono classi senza estensioni o dipendenze varie... fare A(B,C) era uguale
    x = 1



a = A()         # niente più A a = new A()! questa è la dichiarazione di un oggetto di (tipo) A.
                # le () NON sono per il costruttore. non esistono costruttori in python
print("\nstampo attributi ereditati e non:")
print(a.y)              # tramite a, accedo all'attributo y di B (B è superclasse di A)
print(a.x)              # tramite a (oggetto di "tipo" A) accedo all'attributo x della classe A
print(a.z)
# queste 2 istruzioni sono molto simili a java. la dichiarazione è completamente diversa lol

#CHIARAMENTE tutto questo va fatto al di fuori della classe A altrimenti non ha senso.
