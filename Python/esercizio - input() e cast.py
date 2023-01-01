print("inserisci qualcosa: ")
val = input()
print(val)
print(type(val)) # anche se passo un numero intero, il valore di val sarà sempre STRING

print("inserisci qualcosa (faccio cast di int): ")
val2 = int(input()) # attenzione al cast!! se gli passo qualcosa diverso a int, mi dà problemi
print(val2)
print(type(val2))

print("inserisci qualcosa (faccio cast di float): ")
val3 = float(input()) # questo cast di float, che è più grande di int, accetta sia float che int
print(val3)
print(type(val3))


