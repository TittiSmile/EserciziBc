def outerFunc():
    def innerFunc():
        a = 10
        b = 1
        print(a+b)
    return innerFunc()      # ritornerĂ  una stampa in questo caso...


outerFunc()                 # quando vado a richiamarla, mi ritornerĂ  innerfunc
