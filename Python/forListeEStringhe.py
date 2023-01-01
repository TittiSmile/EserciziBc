# esempio su come funziona il for con le liste

lista = [1, 3, 6]
stringa = "ciaoATutti"
# scorro la lista di interi
for i in lista:
    print(i)

print("*******")

# scorro la lista di stringhe
for j in stringa:
    print(j)    # stampa 1 carattere per volta di stringa. questo perchè j, chiaramente, è un indice di questo "array
                # di stringhe".



# stampare tante volte quanto l'indice la stringa
for h in stringa:
    print(stringa) # chiaramente stamperà 10 volte la stringa perchè 10  è la dimensione di stringa.
                   # il senso è far andare avanti h finchè non finisce ciò che è contenuto in stringa.
                   # h sarà quindi il contatore di caratteri di stringa (che è proprio 10)
