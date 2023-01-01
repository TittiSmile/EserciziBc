"""
Si crei un programma che calcoli il la lunghezza della parola
inserita fino a quando non viene inserita la parola exit
"""
scelta=""
while scelta!="exit":
    s = input("inserisci una stringa: ")
    print("la lunghezza della stringa ", s , " è: ", len(s))
    scelta= input("continuare? (digita exit per uscire): ")
