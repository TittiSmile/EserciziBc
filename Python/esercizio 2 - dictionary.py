"""
Tipi di dati Python
Esercizio:
Data un dizionario:
• Si stampi il contenuto
• Si verifichi la dimensione
• Verificare le proprietà
• Estrarre elementi

"""
d = {'Pippo' : 1 ,
     'Pluto' : 2 ,
     'Topolino' : 3,
     'Paperino' : 'Papera'}
print("dizionario:", d)
print("lunghezza:", len(d))
print("tipo:", type(d))
print("key al primo posto", d['Pippo'])
print("tutti valori: ", d.values())
print("tutte le chiavi: ", d.keys())    
del(d['Topolino'])
print("dizionario dopo aver eliminato un elemento:", d)