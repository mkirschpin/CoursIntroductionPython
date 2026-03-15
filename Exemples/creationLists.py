# Exemples de création de lists
# les variables ne sont créées en Python que lorsqu'on lui attribue une valeur
# ça peut poser quelques difficultés lorsqu'on parle des lists (tableaux)

# Si on sait exactement la taille de la liste
# None veut dire une valeur inconnue (NULL), bref, une case vide
liste = [ None, None, None, None ]                         # liste de 4 position 
tab2dim = [ [ None, None, None ], [ None, None, None ] ]   # tableau 2 lignes et 3 colonnes 

# on recupère leur taille 
taille = len(liste)
nbLignes = len(tab2dim) 
nbColonnes = len(tab2dim[0])

print(liste, 'taille', taille)
print(tab2dim, nbLignes, 'x', nbColonnes)

# maintenant si on ne sait pas la taille 
# (par exemple, si on l'obtient d'une variable en entrée ou qu'on demande à l'utilisateur)
taille = int(input('taille souhaitée ? '))

# c'est là où sa coince : on va devoir utiliser notre créativité
# on peut utiliser l'opérateur * pour "multiplier" les None autant de fois qui nécessaire
liste = [ None ] * taille 
print (liste, 'taille', len(liste))


#  on peut aussi se servir directement d'un range, qu'on utilisera comme démarrage
liste = list(range(taille))
print (liste, 'taille', len(liste))

# ou encore on peut se servir d'une boucle for qui va faire "répeter" le Node n fois
liste = [ None for c in range(taille) ]
print (liste, 'taille', len(liste))


# pour les tableaux multi-dimensionnel, on va aussi avoir plusieurs solutions
# on rappelle qu'un tableau multi-dimensionnel est un tableau de tableaux
# autrement dit, une liste dont chaque postion est une autre liste
# il faut donc créer chacune de ces listes... 
nbLignes = int(input('Nb de lignes ? '))
nbColonnes = int(input('Nb de colonnes ? '))

# méthode 1 : si [ None ] * n permet de créer une liste de taille n (ça sera notre ligne)
# on va devoir répéter cette opération, autant de lignes qu'on veut, à l'aide d'un for 
liste = [ [ None ] * nbColonnes for l in range(nbLignes) ]
print(liste, len(liste), 'x', len(liste[0]))

# on peut alors accéder et manipuler ensuite chaque valeur
liste[0][0] = 'a'
print(liste)

# méthode 2 : même idée que le précédent 
# si [ None for c in range(n) ] permet de créer une liste avec n positions, 
# on va répeter cette création à l'aide d'un for autant de lignes qu'on veut
liste = [ [ None for c in range(nbColonnes) ] \
                        for l in range(nbLignes) ]
print(liste, len(liste), 'x', len(liste[0]))

# on peut alors accéder et manipuler ensuite chaque valeur
liste[0][0] = 'a'
print(liste)

# méthode 3 : pareil q le premier, mais la ligne on va la créer directement avec range
liste = [ list(range(nbColonnes)) for l in range(nbLignes) ]
print(liste, len(liste), 'x', len(liste[0]))

# on peut tjs accéder et manipuler ensuite chaque valeur
liste[0][0] = 'a'
print(liste)



