# assert lancia un'eccezione se c'è un confronto FALSO
x = 10
try:
    #assert(x==41)   # andrà in except
    assert(x==10)   # andrà nell'else
except:
    print("errore!!!")
else:
    print("ok")