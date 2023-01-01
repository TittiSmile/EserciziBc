"""Si utilizzi il modulo breezypythongui per creare una GUI che consente all’utente di
profilarsi inserendo nome, cognome, scelta del colore, username, password e caricamento
di un file. Una volta cliccato su invia deve comparire un popup che visualizzi: Iscrizione
creata correttamente."""

from breezypythongui import EasyFrame
import tkinter.filedialog


class profiloUtente(EasyFrame):
    def __init__(self):
        # EasyFrame.__init__(self, width=500, height=500, title="ProfiloUtente")
        EasyFrame.__init__(self, title="ProfiloUtente")
        self.setResizable(False)
        self.setBackground("#4682B4")
        self.addLabel(text="Inserisci dati:", row=0, column=0)

        self.addLabel(text="nome:", row=1, column=0)
        self.inputField=self.addTextField(text=" ", row=1, column=1 )

        self.addLabel(text="cognome:", row=2, column=0)
        self.inputField=self.addTextField(text=" ", row=2, column=1)

        self.addLabel(text="username:", row=3, column=0)
        self.inputField=self.addTextField(text=" ", row=3, column=1)

        self.addLabel(text="password:", row=4, column=0)
        self.inputField=self.addTextField(text=" ", row=4, column=1)

        self.outputArea = self.addTextArea("scegli un file da leggere...", width=30, height=1,row=5, column=0)
        self.addButton(text="open", row=5, column=1, command=self.apriFile)


        self.outputField= self.addTextField(text="  ", row=10, column=1, state="readonly")
        self.button=self.addButton(text="invia",row=10,column=0, command=self.popUpMessage)
    def popUpMessage(self):
        msg="Iscrizione effettuata"
        self.outputField.setText(msg)
    def apriFile(self):
        file=tkinter.filedialog.askopenfilename(parent=self)
        if file!= "":
            fileApertura=open(file,"r")
            lettura=fileApertura.read()
            fileApertura.close()
            self.outputArea.setText(lettura)
            self.setTitle(file)



def main():
    profiloUtente().mainloop()


if __name__ == "__main__":
    main()