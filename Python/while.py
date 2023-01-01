# il while funziona in maniera simile agli altri linguaggi di programmazione
# c'è una condizione booleana (presa come true). si utilizza il while quando si sa già quante volte si vuole
# eseguire il ciclo. viceversa, è preferibile il for.

i = 5
while i < 10:   # ciclo infinito!!!! questo perchè 5 sarà sempre minore di 10.
    print("ok")
    i+=i      # non è un incremento giusto. così facendo, uscirò sì dal while ma la mia i sarà 10 perchè faccio 5+5

print(i)

print("**********")
j = 6
while j < 10:
    print("ok ", j)
    j+=1                # si incrementa così in python... non c'è la notazione i++, sob


# nel while, devi dichiararti prima l'indice e poi puoi usarlo (a differenza del for).

print("**********")

# uso di while con else
k = 4
while k < 6:
    print("ok")
    k+=1
else:
    print("while terminato")
# diciamo che else funziona come default nello switch (ha poco senso ma gg)