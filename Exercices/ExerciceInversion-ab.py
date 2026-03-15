# Exercice Inersion tableau
# A partir d'un tableau donné par l'utilisateur (p.ex. [a, b, c]),  
# produire un nouveau tableau avec les mêmes éléments mais en ordre inverse ([c, b, a])

 
# d'abord, on demande à l'utisateur combien des valeurs il souhaite pour son tableau
# puis on lui demandera autant de valeurs.   
taille = int(input('Taille du tableau ? '))

# on va créer un tableau de cette taille
liste = [ None for col in range(taille) ]


# on va lire autant d'éléments. 
# on peut faire avec un for compteur in range(taille) ou avec un while
compteur = 0
while compteur < taille :
    valeur = input('Valeur ? ')
    liste[compteur] = valeur
    compteur = compteur + 1     # pas nécessaire si on fait un for

#for compteur in range(taille) :
#    valeur = input('Valeur ? ')
#    liste[compteur] = valeur

print('valeurs renseignées :', liste)


# Créer un 2ème tableau listeInv, qui aura les mêmes valeurs de liste en ordre inverse
listeInv = [ None for col in range(taille) ]

# différentes manières de faire, 
# pour rester proche à l'algo fait en TD, on va utiliser 2 compteurs, un qui avance et l'autre qui recule
compteur = 0                    # première position
compteurInv = taille - 1        # dernière position

# double check au cas où (un seul suffisait en fait)
while compteur < taille and compteurInv >=0 :
    listeInv[compteurInv] = liste[compteur] 
    compteur += 1               # équivaut à compteur = compteur + 1
    compteurInv -= 1            # équivaut à compteurInv = compteurInv - 1 

print(liste)
print(listeInv)
