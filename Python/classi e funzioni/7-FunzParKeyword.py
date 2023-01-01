# funzioni con parametri keyword (esempi)
# abbiamo visto prima i parametri posizionali... ora vediamo l'esempio ocn le keyword

def f(a, b, c, d):
    print(a,b,c,d)


f(c=1, b=5, d=9, a=44)
# in questo caso, ho assegnato nella chiamata di funzione i valori di a,b,c,d. sono messi in maniera sparsa.
# questo vuol dire che verrà stampato l'ordine: c b d a????
# assolutamente NO!!!!!!
# la posizione è ciò che conta per prima. quindi, anche se a viene assegnata alla fine della dichiarazione, verrà comunque
# stampata per prima perchè la funzione f prende l'ordine a, b, c,d. fregacazzi in che ordine hai messo la keyword!!!