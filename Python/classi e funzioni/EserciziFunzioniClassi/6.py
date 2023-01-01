"""
L’inizializzatore deve ricevere e settare Nome Cognome ID ed età
"""
class Persona():
    def __init__(self, nome, cognome, id, anni):
        self.nome=nome
        self.cognome=cognome
        self.id=id
        self.anni=anni

    def stampa(self):
        print(self.nome, self.cognome, self.id, self.anni)


p = Persona("harry", "potter", "777", 11)
p.stampa()


"""
                in JAVA
public class myClass{
    private String nome;
    myClass(String nome){
        this.nome=nome
    }
}
"""