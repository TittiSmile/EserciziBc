file = open("text3.txt", "w")   # metti w per scrivere
file.write("ciao a tutti")      # faccio scrivere una frase
file.close()                    # chiudo il file

file = open("text3.txt","r")    # apro il file
print(file.read())              # stampo la lettura del file
file.close()                    # chiudo il file


"""alcune cose buone a sapersi: se il file che vogliamo aprire per scrivere NON esiste (quindi immagina che
text3.txt non esiste) verrà automaticamente creato e ci verrà scritto quello che gli passiamo.
RICORDA che la write sovrascrive tutto quello che c'era prima."""