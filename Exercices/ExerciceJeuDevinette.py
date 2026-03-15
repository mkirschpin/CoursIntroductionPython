# Exercice jeu de devinette. 
# L’utilisateur renseigne un chiffre, l’ordinateur tire au sort un numéro entre 0 et ce chiffre,
# l’utilisateur doit ensuite essayer de découvrir quel numéro l’ordinateur a tiré au sort.
#  L’utilisateur a droit à 3 essais. 

# on commence par demander la limite max
limiteMax = int (input('Limite max ? '))

# on tire au sort 
from random import randint 
numero = randint(0,limiteMax)

# on définit nos variables de contrôle pour la boucle
nbEssai = 3                             # 3 essais autorisés
trouve = False                          # si on a trouvé ou pas

# tant qu'on n'a pas trouvé et qu'il nous reste des essais à faire
while trouve == False and nbEssai > 0 :
    pari = int(input('Votre pari ? '))
    if pari == numero :
        trouve = True       # ça y est, on a trouvé

    nbEssai = nbEssai - 1   # on a fait un essai, un essai de moins disponible

if trouve :                 # trouve est vraie, on a gagné
    print('Vous avez gagné !!') 
else :                      # sinon, on a fait tous les essais et on a perdu
    print('Vous avez perdu ! Le numéro était ', numero)    
