numero = eval(input("inserisci un intero: "))
tipoNumero = isinstance(numero,int)
try:
    if tipoNumero == True:      # cioè sto dicendo se il tipo inserito è davvero intero
        print("è un intero")
    else:
        raise   # così sto dicendo di alzare un'eccezione (viene presa sotto)
except:
    print("no")
finally:
    print("stampo sempre blocco finally")

# posso avere solo 1 finally per volta