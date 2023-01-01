x = 10
def funz():
    global x
    x = 444
    print(x)


def funz2():
    x = 11
    print(x)





funz()
funz2()
print(x)


"""x parte dal valore di 10. in funz viene dichiarata x come globale cioè il valore che verrà assegnato ad x da 
 lì in poi (nella funzione funz, in questo caso) sarà quello stabilito. 
 
 stampando funz 2 x ha il valore di 11 perchè in quella funzione il suo valore cambia
 
 se stampo x normalmente allora è 444 perchè x è stata dichiarata come globale"""