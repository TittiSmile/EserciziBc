"""
(pag31) le funzioni le abbiamo viste anche prima nella lezione 5.
 qui però stiamo avendo a che fare con metodi definiti in una classe
 (funzione -> fuori da una classe. metodo -> in classe). un metodo in una classe è considerato come attributo
"""

class myClass():    # è buona norma mettere le parentesi vuote
    def metodo(self):  # a differenza delle funzioni già introdotte, un metodo di una classe prende come parametro self
        print("sono nel metodo della classe")
    def metodo2(self,a):    # chiaramente, posso passargli anche un argomento (o più) generici...
        print(a)
        self.a = a
        #self.a="aaa"   #non funge


c = myClass()
c.metodo()
c.metodo2(1)        #...ricordando che nella chiamata al metodo, devo passare l'argomento
c.metodo2("ciao")   # chiaramente può essere anche una stringa
c.metodo2(14)





"""
                    in JAVA

public class Main
{
    int x;
    int foo(int x){         //gli passo questo parametro quando chiamo foo con m 
        this.x=x;           //con this imposto la x dichiarata nel main = alla x del parametro di foo (un po' come col costruttore)
        return x;
    }
	public static void main(String[] args) {
		System.out.println("Hello World");
		Main m = new Main();
		System.out.println(m.foo(10));
		
	}
}


"""