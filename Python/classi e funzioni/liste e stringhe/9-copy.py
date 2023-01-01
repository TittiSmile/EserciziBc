# se faccio copy, invece, a differenza di 8, se modifico l'una NON modifico l'altra
l = [1, 2, 3]
l2 = []
l2 = l.copy()
print("lista l: ", l)
print("lista l2: ", l2)
l2.append(555)
print("lista l dopo append: ", l)
print("lista l2 dopo append: ", l2)