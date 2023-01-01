# if not funziona solo con valori vuote (stringhe vuote, liste vuote...) o con valori dichiarate false.
# in pratica NON funziona come una negazione. è valido (cioè esegue il blocco di codice) solo se ha a che fare con false o vuoto

a = True
b = False
s = ""
l = []
t = (1, 5, 9)
print("a: ", a, "\nb: ", b, "\ns: ", s, "\nl: ", l, "\nt: ", t)
if not a:
    print(a, " è falso")
elif not b:
    print(b, " è falso")    # chiaramente stamperà solo questo (e non gli altri, SEPPUR VERI) perchè appena trova la condizione true esce (tipo break)
elif not s:
    print(s, " è vuota")
elif not l:
    print(l, " è vuota")
elif not t:
    print(t, " è vuota")

if not s:
    print(s, " è vuota")

