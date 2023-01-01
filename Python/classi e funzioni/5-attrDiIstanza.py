# si possono creare attributi di istanza

class A:
    x = 10
    y = 4


a = A()     # dichiaro un oggetto a della classe A
a.x=77      # do al valore x di a 77 (NON vado a cambiare x = 10 della classe A. stessa cosa succede in JAVA)
a.x2 = "ciaoBello"  # alla vista, potrebbe sembrare errore ma non lo è! x2 vale solo per a
print(a.x)
print(a.x2)

a2 = A()
# print(a2.x2)        # chiaramente errore perchè x2 non è visibile per a2

a2.x2="eee"         # questo però posso farlo. sono due x2 diversi per a ed a2. non hanno niente da che spartire. saranno visibili
                    # ed accessibili solo da coloro che lo dichiarano



# in java una cosa del genere sarebbe totalmente ILLEGALE. roba che ti denunciano. però hey, è python quindi gg