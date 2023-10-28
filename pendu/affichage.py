import os







# Fonction clear le terminal
os.system("clear")
# Fonction curseur (Code Dorian)
def setCursor(x,y):
    print("\033[%d;%dH" % (y,x), end='')
# Fonction clear une ligne
def clearLine(line):
    setCursor(0, line)
    x,y = os.get_terminal_size()
    for i in range(x):
        print(" ", end='')
    print("")



def EcrireCaractere(lettre_dite):
    NewLettre = False
    LettreOK= False
    clearLine(0)
    setCursor(0,0)
    print("Saisir une lettre en minuscule",end="")
    Lettre = input(" ? ").lower()  #.lower() convert A to a 
    while(not(LettreOK)):
        
        # Caractère valide
        if len(Lettre) != 1:
            clearLine(0)
            setCursor(0,0)
            print("Merci de taper qu'une seule lettre",end="")
            Lettre = input(" ? ") 
            LettreOK = False
            NewLettre=True
        elif Lettre >= 'a' and Lettre <= 'z':
            LettreOK = True
            NewLettre=True
        else :
            clearLine(0)
            setCursor(0,0)
            print("Saisir une lettre en minuscule",end="")
            Lettre = input(" ? ") 
            LettreOK = False
            NewLettre=True

        # Lettre pas dite
        if LettreOK :
            for case in range (0,len(lettre_dite)):
                if Lettre==lettre_dite[case]:
                    NewLettre=False
        if not(NewLettre):
            clearLine(0)
            setCursor(0,0)
            print("Lettre déjà utilisé, nouvelle lettre",end="")
            Lettre = input(" ? ")
            LettreOK= False
            NewLettre=True
    # Stocker la lettre utilisée    
    lettre_dite.append(Lettre)
    return Lettre

# Afficher le pendu 
def Afficher_Pendu(Ajout_Pendu):
    match Ajout_Pendu :
        case 1 :
            setCursor(3,8)
            print("━")
        case 2 :
            setCursor(4,8)
            print("┻")
        case 3 :
            setCursor(5,8)
            print("━")
        case 4 :
            setCursor(4,7)
            print("┃")
        case 5 :
            setCursor(4,6)
            print("┃")
        case 6 :
            setCursor(4,5)
            print("┏")
        case 7 :
            setCursor(5,5)
            print("━")
        case 8 :
            setCursor(6,5)
            print("┓")
        case 9 :
            setCursor(6,6)
            print("0")
        case 10 :
            setCursor(6,7)
            print("◊")