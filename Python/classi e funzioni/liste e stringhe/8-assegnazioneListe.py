# posso assegnare una lista ad un'altra
l = [1, 2, 3]
l2 = []
l2 = l
print("lista l: ", l)
print("lista l2: ", l2)
l2.append(555)  # visto che c'è stata l'assegnazione, se modifico l2 modifico l e viceversa
print("lista l dopo append: ", l)
print("lista l2 dopo append: ", l2)