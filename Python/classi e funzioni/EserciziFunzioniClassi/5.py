"""
Scrivere una classe Docente che rappresenti le seguenti informazioni relative ad un docente:
nome, cognome, codice ed età
"""

class Docente():
    nome = "Anakin"
    cognome = "Skywalker"
    codice = "BB8"
    id = 51

doc = Docente()
print("nome docente: ", doc.nome,
      "\ncognome docente: ", doc. cognome,
      "\ncodice: ", doc.codice,
      " \nid: ", doc.id)