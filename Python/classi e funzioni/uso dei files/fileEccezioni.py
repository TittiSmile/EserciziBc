# posso gestire le eccezioni anche con i file
try:
    file = open("provolone.txt", "r")
    print(file.read())
    file.close()
except:
    print("errore. file inesistente. non si può leggere")
