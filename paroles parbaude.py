parole = input("Ievadi savu paroli: ")
mazie = 0
lielie = 0
cipari = 0
simboli = 0
for el in parole:
    if el.islower():
        mazie = 1
    elif el.isupper():
        lielie = 1
    elif el.isdigit():
        cipari = 1
    elif not el.isalpha() and not el.iadigit():
        simboli = 1
kriteriji = mazie + lielie + cipari + simboli                       
if len(parole) >= 9:
    if kriteriji >= 3:
        print("Parole ir droša!") 
    elif kriteriji == 2:
        print("Parole ir videji droša!")
    else:
        print("Parole nav droša!!!")
else:
    print("Parole nav droša!!!")             