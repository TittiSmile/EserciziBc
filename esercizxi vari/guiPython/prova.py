from breezypythongui import EasyFrame
import tkinter.filedialog

class File(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, "file ")
        self.addLabel(text="apri un file da leggere:", row=0, column=0)
        self.outputArea=self.addTextArea(" scegli un file... ",row=1,column=0)
        self.addButton(text="open",row=1, column=2,command=self.apriFile)
    def apriFile(self):
        file=tkinter.filedialog.askopenfilename(parent=self)
        if file!= "":
            fileApertura=open(file,"r")
            lettura=fileApertura.read()
            fileApertura.close()
            self.outputArea.setText(lettura)
            self.setTitle(file)



def main():
    File().mainloop()


if __name__ == "__main__":
    main()