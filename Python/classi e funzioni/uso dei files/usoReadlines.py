# readlines serve a leggere un file di testo e a passare ciò che è scritto come
# se fossero elementi di una lista
file = open("text2.txt", "r")
print(file.readlines()) # stampo gli elementi del file di testo in una lista
file.close()



print("\n*****\n")
# in maniera analogoa...
with open("text2.txt", "r") as txt:
    print(txt.read())

with open("text2.txt", "r") as txt:
    print(txt.readlines())
txt.close()