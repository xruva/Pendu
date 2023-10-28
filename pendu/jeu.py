import random
import os
from data import list_mot
import affichage

#############################################
##                                         ##
##              Jeu du pendu               ##
##                                         ##
#############################################

#Variables
nb_mot = len(list_mot)
mot_alea = random.randint(0,nb_mot-1)
lettre_dite =[]
mot = list_mot[mot_alea]

Lettre_trouvee = 0
nb_lettre = len(mot)
Ajout_Pendu = 0
LettreOK = False
NewLettre = False
Gagne=False
Perdu=False


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


# Afficher les "-" correspondant au nombre de lettre
setCursor(0,10)
for i in range (0,nb_lettre):
    print("_",end="")

# Afficher l'alphabet
setCursor(0,12)
print('abcdefghijklmnopqrstuvwxyz')

while(not(Gagne)and not(Perdu)):

    #Ecriture lettre
    Lettre=affichage.EcrireCaractere(lettre_dite)

    #Rayer la lettre dans l'alphabet
    posi = ord(Lettre)-96
    setCursor(posi,12)
    print("-",end="")

    #Check Lettre dans le mot
    Post_lettre_trouvee = Lettre_trouvee
    for i in range (0,len(mot)) :
        if Lettre==mot[i] :
            setCursor(i+1,10)
            print(Lettre)
            Lettre_trouvee +=1

    #Si il n'y avait pas de lettre dans le mot, ajout d'un baton        
    if Post_lettre_trouvee == Lettre_trouvee:
        Ajout_Pendu+=1
 
    # Afficher le pendu 
    affichage.Afficher_Pendu(Ajout_Pendu)

    #Fin du jeu
    if nb_lettre==Lettre_trouvee:
        Gagne=True
        setCursor(3,3)
        print("Gagné ! Le mot était :",mot)
    if Ajout_Pendu==10:
        Perdu=True
        setCursor(3,3)
        print("Perdu... Le mot était :",mot)
    

    #   FIN !