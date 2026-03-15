# les tableaux dans Python sont en fait des lists
# une liste est une suite ordonnée d'éléments 
# chaque élément a donc une position (tab[position]) comme les tableaux
# et on peut changer le contenu de ces positions (c'est "mutable")

tab = [ 10 , -20, 1.5, 3 ]
taille = len(tab)
premier = tab[0]
dernier = tab[-1]
print ('taille', taille, 'premier', premier, 'dernier', dernier)
print (tab)

tab[1] = 2
tab.append(40) 
print(tab)

somme = sum(tab)
maxi = max(tab)
print (somme, maxi)

tab.insert(4, 5)    # on insère une nouvelle valeur 5 qui occupera la position 4
print(tab)        
tab.remove(2)       # on supprime la valeur 2 (une exception est lancée si valeur pas dans la liste)
print(tab)
tab.pop(1)          # on supprime la valeur à la position 1 
print(tab)
tab.sort()          # on ordonne les éléments sur le tableau
print(tab)

# un tableau multidimensionnel est un "tableau des tableaux" 
# une liste dont les valeurs sont d'autres listes
tab2dim = [ ['a' , 'b' ], [ 'c', 'd'] ]
print(tab2dim)

# un tableau contient des objets, peu importe leur classe
tab2dim[1][1] = 0       # on peut ajouter un int à notre tableau de string
print(tab2dim)

# chaque élément dans une liste est un objet, et on n'est pas obligé d'avoir
# tous les objets de même "type" (classe). 
# on peut donc avoir qqch comme ça
produits = ['raclette', 'compté']
prix = [ 5.0 , 7.0 ]
qtes = [ 2, 1]
panier = [ 'Toto', produits, prix, qtes, 17.0]
print(panier)
print('client:',panier[0])
print('1er prod:',panier[1][0])

# on peut à tout moment ajouter des nouvels éléments à un tableau 
# la méthode "append" ajouter un nouvel élément à la fin du tableau
produits.append('maroille')
prix.append(6.0)
qtes.append(2)

print('Produits :',produits)
print('Prix :', prix)
print('Quantités :',qtes)

# l'indice -1 permet d'accéder à la dernière position d'une liste
#  voir exemple "collections" 
panier[4] = panier[-1] + prix[-1]*qtes[-1]

# le tableau panier contient les tableaux produits, prix et qtes 
# si on met à jour ces derniers,  le tableau panier le sera aussi, puisqu'il les contient
print(panier)

