"""
Creare una funzione che calcoli quanti giorni mancano a Natale dopo aver inserito il
numero da tastiera del giorno e mese corrente
"""
def calcolaGiorni (giorno, mese):
    giornoNatale = 25
    meseNatale = 12
    differenzaGiorni = 0
    differenzaMesi = 0

# se siamo prima del 25 e nei mesi disponibili
    if giorno <= giornoNatale and mese <= meseNatale:
        differenzaGiorni = giornoNatale - giorno
        differenzaMesi = meseNatale - mese
        print("la tua data: ", giorno, "/", mese,
              "\nmancano ", differenzaGiorni, " giorni  e ", differenzaMesi, " mesi a Natale")
# se siamo dopo il 25 nei mesi disponibili
    elif giorno >= giornoNatale and mese <= meseNatale :
        differenzaGiorni = giornoNatale + (31 - giorno)
        differenzaMesi = meseNatale - mese - 1
        # casistica dal 26 al 31 dicembre
        if giorno > giornoNatale and mese == 12:
            differenzaGiorni =  (31-giorno) + giornoNatale
            differenzaMesi = 11
            print("la tua data: ", giorno, "/", mese,
                  "\nmancano ", differenzaGiorni, " giorni  e ", differenzaMesi, " mesi a Natale")
        else:
            print("la tua data: ", giorno, "/", mese,
                  "\nmancano ", differenzaGiorni, " giorni  e ", differenzaMesi, " mesi a Natale")



giorno = int(input("inserire giorno: "))
mese = int(input("inserire mese: "))
calcolaGiorni(giorno, mese)


# vedi come fare while finchè non è un intero...








# piccola postilla. in altri linguaggi di programmazione, la dichiarazione va fatta al di fuori dell'if.
# la dichiarazione di questa variabile è visibile solo nell'if
"""
                                            ESEMPIO IN JAVA!!!!!!!!!!!!!!!!!!!!!!!
public class Main
{
    int foo(){
        int x = 10;
        int val = 0; /* val lo dichiaro fuori dall'if. questo perchè, se lo avessi dichiarato dentro,
                        il return val non mi andava :D val non era visibile fuori dall'if*/
        if (x>=10){
           val = 2;
        }
        else{
             val = 44;
        }
        return val;
    }
    
    public static void main(String[] args) {
        System.out.println("Welcome to Online IDE!! Happy Coding :)");
        Main m = new Main();
        System.out.println(m.foo());
    }
}




            *************************IN MANIERA ALTERNATIVA A SOPRA****************************
            
            
            
public class Main
{
    int foo(){
        int x = 5;
        if (x>=10){
          int val = 2;
          return val;
        }
        else{
           int  val = 44;
           return val;
        }
    }
    
    public static void main(String[] args) {
        System.out.println("Welcome to Online IDE!! Happy Coding :)");
        Main m = new Main();
        System.out.println(m.foo());
    }
}


"""


