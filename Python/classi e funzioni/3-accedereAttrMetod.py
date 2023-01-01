# per accedere ad attributi (ma anche metodi) di una classe, si usa la dot notation.
class myClass:
    x = 10      # attributo della classe
    y=4



var = myClass()
print(var.x)
print(myClass.y)    # se non voglio creare un oggetto di quella classe, posso accedere ad y attraverso la classe stessa




"""
discorso un po' diverso da java... 
con java si può usare la classe per accedere ad un attributo solo se l'attributo (ma anche metodo) è statico.


public class Main
{
    int x = 10;
	public static void main(String[] args) {
		System.out.println("Hello World");
		System.out.println(Main.x);                 // ERRORE perchè x non è statico.
	}
}

"""

