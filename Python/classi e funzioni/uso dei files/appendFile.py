# se voglio scrivere senza dover sovrascrivere quello che c'era prima, uso append

file = open("text3.txt", "a")
file.write("\n ok")
file.close()

file = open("text3.txt", "r")
print(file.read())
file.close()