"""È possibile assegnare una borsa di studio se il voto dell’esame di stato è compreso
tra 75 e 90. Il voto deve essere inserito da tastiera."""

voto = eval(input("qual è stato il tuo voto di maturità? "))
if voto >= 75 and voto <= 90:
    print("complimenti, avrai la tua borsa di studio")
elif voto > 90:
    print("sei troppo bravo, avrai un'altra borsa di studio")
else:
    print("niente borsa di studio. impegnati di più")