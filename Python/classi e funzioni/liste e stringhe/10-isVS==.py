l = [1, 2, 3]
l2 = []
l2 = l.copy()
print("lista l: ", l)
print("lista l2: ", l2)

if l is l2:
    print("ok")
else:
    print("ko")

if l == l2:
    print("ok")
else:
    print("ko")

"""
il 1 output dà ko perchè sono due liste diverse (l2 ha fatto copy su l. se avesse fatto = allora usciva ok)
il 2 output dà ok perchè le due liste sono effettivamente la stessa cosa cioè contengono la stessa cosa. 
"""