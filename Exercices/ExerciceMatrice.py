# Exercice transpotion d'une matrice
# créer un programme permettant d'inverser (transposer) une matrice M de taille L x C 

# d'abord on va permettre à l'utilisateur de nous renseigner la matrice M
nbLignes = int(input('Nb de lignes : '))
nbColonnes = int(input('Nb de colonnes : '))

m = [ 0 for lin in range(nbLignes) ]

# on peut utiliser un while ou un for en guise de boucle
for lin in range(nbLignes) :
    # chaque ligne va avoir NbColonnes éléments 
    m[lin] = [ 0 for col in range(nbColonnes) ]

    for col in range(nbColonnes) :
        m[lin][col] = int(input("valeur [%d][%d] :" % (lin,col) ) )

print('matrice M :', m)

# on va créer maintenant la nouvelle matrice qu'on remplira
mInv = [ [ 0 ] * nbLignes for l in range(nbColonnes) ]

# on a une matrice de 2 dimensions, donc 2 boucles (while ou for)
# avec for
#for lin in range(nbLignes) :
#    for col in range(nbColonnes) :
#        mInv[col][lin] = m [lin][col]

# avec while
lin = 0                              
while lin < nbLignes :
    col = 0                          
    while col < nbColonnes :
        mInv[col][lin] = m [lin][col]
        col += 1                     
    lin += 1

print ('matrice transposée : ', mInv)
