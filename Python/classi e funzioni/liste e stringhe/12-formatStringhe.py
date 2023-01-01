s = "sono {n} e ho {x} anni".format(n="pippo",x=10)
print(s)
s2 = "numero {0:1.2f}".format(0.456234794)
print(s2)
"""la sintassi di format è: 
{} -> ci metto qualcosa dentro
{[argomentoIndiceDellaParola] : [lunghezza][.precisione][formato]}
 quindi 0 vuol dire che è l'indice della parola/numero
 1 è la lunghezza della parte intera
 2f vuol dire che vado a prendere i primi 2 dopo la virgola   (f sta per float) 
  """


s3 = "numero {0:3.4f}".format(412.552135)   # a quanto pare, cambiare il 3 non mi dà nulla di diverso...
print(s3)
# l'indice di partenza è sempre 1. prendo 4 numeri dopo la virsola


s4 = "numero {0:7d}".format(2412563)    # non capisco cosa dovrebbe cambiare ma ok 
print(s4)