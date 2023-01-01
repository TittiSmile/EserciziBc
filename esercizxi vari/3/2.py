"""
1 - Stampa solo la colonna Colore
2 - Associa in automatico valori al colore
3 - Stampare il tutto
4 - Si applichi il metodo one hot encoding sulla colonna che contiene le variabili categoriali.
5 - Si crei una nuova colonna e si applichi il metodo dummy alla colonna del colore, con prefisso
    colore.
6 - Ristampare il tutto"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({"Prodotto" : ["Penna", "Penna", "Penna"],
                   "Azienda" : ["Bic", "Bic", "Bic"],
                   "Quantità" : [10, 15, 30],
                   "Colore" : ["Blu", "Nera", "Rossa"]})

print("***************************************")
print(df["Colore"])


print("***************************************")
df["Colore"] = LabelEncoder().fit_transform(df["Colore"])
print(df)


dfColor = pd.get_dummies(df["Colore"], prefix = "Colore")
print(dfColor)
df2 = df.join(dfColor)
print("***************************************")
print(df2)
