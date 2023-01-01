"""Si desidera scrivere un programma che, con febbre alta e con i seguenti sintomi riscontrabili:
• tosse
• febbre
• stanchezza
• difficoltà respiratorie (casi gravi)
L’utente ha probabilmente il Covid -19.
Se ha i decimi di febbre deve riposare altrimenti sta bene"""

tosse = False
febbre = False
stanchezza = False
respiro = False

scelta1=(input("hai la tosse? s/n: "))
if scelta1 == "s":
    tosse = True
else :
    tosse = False

scelta2=(input("hai la febbre? s/n: "))
if scelta2 == "s":
    febbre = True
    temperatura = float(input("qual è la tua temperatura?  "))
else :
    febbre = False

scelta3=(input("hai stanchezza? s/n: "))
if scelta3 == "s":
    stanchezza = True
else :
    stanchezza = False

scelta4=(input("hai difficoltà a respirare? s/n: "))
if scelta4 == "s":
    respiro = True
else :
    respiro = False


if febbre == True and respiro == True and stanchezza == True and tosse == True:
    print("probabilmente hai il covid")

#elif febbre == True and (respiro == False or stanchezza == False or tosse == False):
elif febbre < 37.5 :    # perchè se metto and febbre > 36.7 non mi entra più qui?
    print("hai solo i decimi di febbre. riposa")
else:
    print("stai bene")
