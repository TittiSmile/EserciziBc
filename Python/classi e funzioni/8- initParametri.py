# è possibile passare parametri ad init, come se fosse una funzione normale
class myClass():
    def __init__(self, a, b):
        print("sono nel metodo magico init")
        self.a = a
        print(a)


obj = myClass("ciao",1)
"""
init funge un po' da costruttore... quindi ogni volta che andrò a creare un oggetto di tipo myClass, 
devo passargli 1 parametro (o più...)
con la scrittura a riga 5, sto assegnando al valore a (di init) il valore a passato come parametro quando creo obj 
(cioè "ciao"). 
ovviamente la print, mi stamperà a. 
CHIARAMENTE, con l'aggiunta di b come parametro, vado ad aggiungere un parametro anche nella creazione di obj. 
se non faccio self.b=*qualcosa* non mi risulterà da nessuna parte... glielo passerò come parametro ma sarà a tutti gli 
effetti inutile. 

"""



"""
                    ESEMPIO DI JAVA 

public class Main{
    private String nome;
    Main(String nome){
        this.nome=nome;
    }
    public static void main(){
        String nome = "ciao";
        Main m = new Main(nome);
        system...(m.nome);      //stamperà "ciao"
    }

}


"""
