#exemple avec boucle et bibliothèque random

#les bibliothèques contiennent plusieurs fonctions déjà prêtes 
#qu'on peut s'en servir dans nous codes. Mais pour cela, il faut
#les "importer", indiquer qu'on va utiliser tel fonction de tel bibliothèque 
from random import randint 

print('On roule le dès... ')

#la fonction randint permet de tirer au sort un chiffre entre les 
#limites données en paramètres (ici 1 et 6)
des = randint(1,6)

#etat initial
nbEssai = 0
pari = 0 

while pari != des and nbEssai < 3 :
    pari = int (input('Votre pari ? '))
    nbEssai += 1    #mise à jour variables de contrôle

if pari == des : 
    print("Vous avez gagné !")
else :
    print("Vous avez perdu ! Le dès vaut ", des)
