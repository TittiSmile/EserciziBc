"""Per poter viaggiare gratis bisogna iscriversi al sito ed avere i seguenti requisiti:
• fino a 25 anni un reddito inferiore ai 15000 euro annui
• dopo i 25 anni un reddito inferiore a 35000 euro annui"""

anni = eval(input("quanti anni hai? "))
reddito = eval(input("qual è il tuo reddito? "))

if anni <= 25 and reddito < 15000:
    print("puoi viaggiare gratis")
elif anni > 25 and reddito < 35000:
    print("puoi viaggiare gratis")
else:
    print("non rientri nei requisiti")