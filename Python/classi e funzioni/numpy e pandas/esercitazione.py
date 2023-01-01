"""
Scrivete un programma che scarichi una pagina web richiesta dall’utente e indichi quali sono le dieci parole
usate più frequentemente, non sovrapposte. Il programma dovrà trattare tutte le parole senza
distinguere fra maiuscole e minuscole. I valori devono essere raggruppati come (parola,numero),
utilizzando Counter(…).most_common(…) Per lo scopo di questo esercizio, immaginate che una
parola sia descritta dall’espressione regolare r"\w+".

Indizio bisogna utilizzare la funzione re.findall Successivmente salvare tutte le parole e le rispettive
frequenze in un file csv, inserendo una riga: parola, frequenza

Si crei un database con DataFrame, quindi con libreria pandas contenente solo le prime 10 parole, si proietti il
tutto su un grafico a barre (.plot.bar) per poi salvare il tutto in un file csv
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


url = pd.read_csv("sample4.csv", header=None, sep=" ")   # assicurati che il file da leggere sta nella cartella del project
print(url)
