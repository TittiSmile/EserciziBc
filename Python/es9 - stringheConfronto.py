s = "ciao"
if s < "t":
    print("primo")
else:
    print("secondo")

# può sembrare un confronto wtf ma in python funziona così: si va a confrontare il primo elemento della stringa con il carattere
# in Java o C questa cosa sarebbe un'eresia (bisogna usare le funzioni sulle stringhe). qui semplicemente prendi c e vedi se viene
# prima di t alfabeticamente parlando. < vuol dire, in questo caso, se viene prima o no 