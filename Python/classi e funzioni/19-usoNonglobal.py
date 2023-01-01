# pag 67
# nonlocal funziona con le innerfunz
x = 10
def funz1():
    x = 20
    def funz2():
        nonlocal x      # nonlocal fa sì che il valore di x dichiarato in funz2 sia così anche per la x di funz1
        x = 30
        print("x in interna",x)
    funz2()
    print("x in esterna",x)


funz1()

print("x dichiarata",x)