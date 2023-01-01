def sum(a, b):
    print(a+b)

def f(z,x,y):
    z(x,y)


f(sum,1,4)

# semplicemente, come parametro di f posso passare la funzione sum (senza parametri)
# questo perchè f prende come parametro z che è una funzione (viene specificata sotto f
