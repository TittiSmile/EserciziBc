# esempio di funzioni in python

def funzione(x, y):     # parametri classici... senza tipo nè niente.
    z = x+y
    return z

print("la somma è: ", funzione(1,3))        # da notare l'indentazione diversa rispetto alla funzione!!!





#ALTERNATIVA
def funzione2(x, y):           # come in java, o C, che si chiamano x y fregacazzi. tanto sono dichiarazioni di parametri...
                               # basta che il nome della funzione è diverso da quelle dichiarate finora
    z = x+y
    print("la somma è: ", z)
    # non c'è return ma poco importa. è come se fosse "sottinteso" VISTO CHE NON CI SONO I TIPI DI RITORNO 


funzione2(4,4)      # chiamata alla funzione. gli passo come parametri 4 e 4
a = 1
b = 2
funzione2(a, b)     # dichiaro prima a e b... non cambia molto





#VARIANTE
def somma(x, y):
    s = x+y
    return s

val = eval(input("\n\ninserisci valore 1: "))
val2 = eval(input("inserisci valore 2: "))
print("la somma di è: ",  somma(val, val2))