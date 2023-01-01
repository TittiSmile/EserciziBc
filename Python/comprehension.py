# esercizi di list, set, dictionary comprehension
# serve a scrivere una condizione tutto su una riga.

# list
l = [1, 2, 3, 4, 5]
l = [i*i for i in l if i % 2 == 0]
# moltiplico gli elementi del contatore. vado da i fino alla fine di l e controllo che i loro quadrati
# (ricorda che ho fatto i*i) sono pari.
print(l)


# set
s = {1, 2, 3}
s = {i + 1 for i in s if i < 5}
print(s)




#dictionary
d = {1 : "aaa", 2 : "bbb", 3 : "ccc"}
d = { k : "ppp" for k in d }
print(d)