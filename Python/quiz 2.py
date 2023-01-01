"""
Stai scrivendo un programma Python per convalidare i
numeri dei dipendenti. Il numero del dipendente deve avere il formato ddd-dd-dddd
e consiste solo di numeri e trattini. Il programma
deve stampare True se il formato è corretto e stampare se
il formato non è corretto, Falso
"""

employee_number=""
parts=""
while employee_number!="":
    valid = True
    employee_number = input("insert employee number: ")
    parts = employee_number.split('-')
    if len(parts) == 3:
        if  len(parts[0])==3 and len(parts[1])==2 and len(parts[2]) == 4:
            if parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
                valid = False
    print(valid)