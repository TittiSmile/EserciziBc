import pandas
import pandas as pd
df = pd.DataFrame({"Name" : ["Simon", "Kate", "Francis", "Laura", "Mary", "Julian", "Rosie", "Simon", "Lausa"],
                   "Height" : [180, 165, 170, 164, 163, 175, 166, 180, 164],
                   "Weight" : [85, 65, 68, 45, 43, 72, 46, 85, 45],
                   "FavoriteFood" : ["steak", "pizza", "pasta", "pizza", "vegetables", "steak", "seafood", "steak", "pizza"],
                   "Sex" : ["m", "f", "m", "f", "f", "m", "f", "m", "f"]})
print(df)

print("*********************************************")
# mi va a sostituire maschi e femmine con 0 e 1. è una funzione dummy
dfDummy = pd.get_dummies(df["Sex"], prefix="Sex")
print(dfDummy)

print("*********************************************")
# unisco ciò che ho ottenuto in un nuovo dataframe
df2 = df.join(dfDummy)
print(df2)

print("*********************************************")
# stampo le prime 2 righe del df
print(df2.head(2))

print("*********************************************")
# tolgo la colonna sex dal nuovo df ottenuto
del df2["Sex"]
print(df2)