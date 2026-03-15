# Exercice transpotion d'une matrice
# programme permettant d'inverser (transposer) une matrice M de taille L x C 
# à l'aide de la bibliothèque NumPy

# on importe la bibliothèque 
import numpy as np

# on va demander à l'utilisateur combien de lignes et de colonnes 
nbLignes = int(input('Nb de lignes : '))
nbColonnes = int(input('Nb de colonnes : '))

# maintenant on peut créer une matrice taille nbLignes x nbColonnes remplie de zéros 
m = np.zeros( (nbLignes, nbColonnes) )

# on aurait aussi pu créer une matrice vide (avec 'None') avec
#m = np.empty( (nbLignes,nbColonnes), dtype='object' )

#on va maintenant demander à l'utilisateur les valeurs pour y coller
#attention, la matrice créée avec m = np.zeros contient des numéros float
# on peut utiliser un while ou un for en guise de boucle
for lin in range(nbLignes) :
    for col in range(nbColonnes) :
        m[lin][col] = float(input("valeur [%d][%d] :" % (lin,col) ) )

print('Matrice :\n', m)

# on transpose la matrice dans une nouvelle matrice
mInv = m.transpose()

print('Matrice transposée :\n', mInv)




