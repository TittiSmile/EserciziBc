file = open("text1.txt", "r")
print(file.read())  # leggo dal file appena aperto
file.close()        # ricorda sempre di chiudere il file aperto


# uso di with e alias as
print("\n******\n")
with open("text2.txt", "r") as txt:     # in maniera equivalente a sopra
    print(txt.read())
file.close()