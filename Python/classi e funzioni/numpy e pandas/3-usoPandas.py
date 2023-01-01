import pandas as pd
"""la serie può basarsi su: liste, tuple, set, dizionari"""
a = pd.Series(["ciao", "come", "stai?"])    # series è, in questo caso, una lista di stringhe.
print(a)    # stamperà, nella prima colonna, un indice e, nella seconda colonna, i valori della lista
print("valori: ", a.values)
print("indici: ", a.index)
print("indici di valori: ", a.index.values)
print("lunghezza serie: ", len(a))
print("*******")
a.index.name="Stringhe di prova su lista"   # do il nome alla serie
print(a)

a.name = "nome di prova"
print(a)