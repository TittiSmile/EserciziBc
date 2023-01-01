"""
qui vediamo come possiamo chiamare un metodo a partire dalla classe.
"""
class myClass():
    def metodo(self):
        print("sono nel metodo della classe")
    def metodo2(self,a):
        print(a)
    #def metodo3():        # darà errore SOLO quando la andiamo a richiamare c.metodo3(). questo perchè devo passare self
        #print("ciaooooo")


c = myClass()
"""funziona un po' come i metodi statici in java... bisogna ricordarsi, però, che se si usa questa notazione, DEVI
passare gli argomenti!!!! in questo caso, devi passare anche self OSSIA un oggetto  di tipo myClass"""
myClass.metodo(c)
myClass.metodo2(c,1)
#in maniera     EQUIVALENTE:
c.metodo()
c.metodo2(22)



"""
        in JAVA
ovviamente in java la dichiarazione di un nuovo oggetto è:
myClass c = new myClass()       //fa capo al costruttore senza argomenti. 

altra differenza, in java non posso accedere ad un attributo/metodo della classe con la classe stessa A MENO CHE non 
si tratti di attributo/metodo STATICO. (vedi il pdf che sto scrivendo su overleaf (libro ecc...)


"""