# uso di continue

while True:
    val = int(input("inserisci valore: (0 per terminare 5 per continue)"))
    if val == 0:
        break
    if val == 5:
        continue    # salta l'istruzione di print val ed esegue nuovamente il codice.
    print(val)

# sia break che continue funzionano in maniera analoga col for. 