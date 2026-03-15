#Exemple usage bibliothèque NumPy

# on va commencer par importer la bibliothèque
# l'alias avec "as" permet de faire np.opération au lieu de numpy.opération
import numpy as np

# une fois importer, on peut definir une matrice (tableau) 3 x 2 rempli des 0
nbLignes = 2
nbColonnes = 3

# attention c'est X, Y (les dimensions), donc COLONNE x LIGNE
matrice = np.zeros( ( nbColonnes, nbLignes) )

# on l'imprime et on vérifie son type
print(matrice)
print('matrice est un objet de la classe :', type(matrice))

# on peut manipuler (modifier ou consulter) les positions par leurs coordonnées
matrice[0][0] = 1
matrice[1][0] = 2
matrice[2][0] = 3

# on peut même attribuer une même valeur à toutes une ligne
matrice[2] = 3

print(matrice)
print('La valeur de la postion [1][1] est ', matrice[1][1])

# on peut utiliser les nombreuses opérations de la classe ndarray
# transpositon
mI = matrice.transpose()

print('La matrice transposée : \n', mI)

# on peut lui demander sa forme (shape est une propiété de la classe ndarray)
forme = mI.shape
lignes = forme[0]           # la première dimension correspond aux nb de lignes
colonnes = forme[1]         # la 2ème dimension correspond au nb de colonnes 

print('la matrice transposée a ', lignes, 'lignes et', colonnes, 'colones', forme)

print('La matrice originnele :\n', matrice)

# on peut obtenir la diagonal de la matrice
diagonal = matrice.diagonal()
print('diagonal', diagonal, 'type', type(diagonal))


# quelques functions statistiques : somme, moyenne, écart-type, max
sommeM = matrice.sum()
sommeLigne = matrice.sum(axis=1)
sommeColonne = matrice.sum(axis=0)
print ('somme par ligne', sommeLigne, 'somme par colonne', sommeColonne, \
    'somme de la matrice',  sommeM)

moyenne = matrice.mean()
ecart = matrice.std()
valMax = matrice.max()

print("Moy:",moyenne,'ecart type:', ecart, 'valMax:', valMax)

# on peut également rechercher facilement des éléments dans la matrice
sup2 = matrice[matrice >= 2]
inf1 = matrice[matrice <= 1]
print('Elements supérieurs ou égales à 2:',sup2)
print('Elements inférieurs ou égales à 1:',inf1)

# enfin, on peut aussi manipuler des matrices d'objets, quelque soit leur classe
matriceObjets = np.empty( (nbLignes, nbColonnes) , dtype='object')
matriceObjets[1][1] = 'Toto'
print("matrice d'objets: \n", matriceObjets)

# attention au moment de créer des matrices "vides" avec d'autres types de données
# elle va contenir alors des valeurs aléatoires
matriceInt = np.empty( (nbLignes, nbColonnes) , dtype='int32')
print(matriceInt)
matriceFloat = np.empty ( (nbLignes, nbColonnes) , dtype='float64')
print(matriceFloat)