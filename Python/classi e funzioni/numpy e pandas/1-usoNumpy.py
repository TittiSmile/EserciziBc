# creo array e faccio operazioni su array

import numpy as np


array = np.array([1, 2, 3])
print(array)

"""gli array di numpy sono tutti omogenei. abbiamo visto come posso avere una lista con vari tipi (numeri o stringhe)
negli array questa cosa è impossibile. vengono dichiarati tutti con lo stesso tipo (a seconda del tipo, si può fare
upcast o downcast... se inserisco solo un solo elemento float, saranno tutti float. questo perchè float > int)"""
array2 = np.array([1,2,"cocco"])
print(array2)
print(type(array2[0]))  # è di tipo numpy string



# matrice
array3 = np.array([ [1, 2], [3, 4] ])
print(array3)

# creazione array con range
array4 = np.array(range(1,5), dtype=np.float64) # posso mettere anche int come tipo
print(array4)
print(array4.ndim)  # non ti dice il numero di elementi ma a quanti dimensioni è l'array... tipo matrice->dim2









