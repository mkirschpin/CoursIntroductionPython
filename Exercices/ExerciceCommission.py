# Exercice : calculer  le montant total des commissions pour un ensemble de conseillers
# On considère un tableau avec le nombre de devis analysés par conseiller par semaine 
# On doit remplir ce tableau et calculer la valeur des commissions pour chaque conseiller,  
# On gardera ces valeurs dans un autre tableau qu'on affichera
# 

# tout d'abord il faut demander combien de conseillers nous avons
# puis créer et remplir le tableau des devis en conséquence

nbConseil = int(input("Nb de conseillers ? "))

devis = [ 0 for lin in range(nbConseil) ]

# on peut utiliser un while ou un for en guise de boucle
for compteur in range(nbConseil) :
    # on va créer le tableau contenant le devis de ce conseiller
    devis[compteur] = [ 0 , 0 , 0 , 0 ]         # ou [ 0 for col in range(4) ]

    print ("conseiller n° ", compteur)

    for sem in range(4) :
        devis[compteur][sem] = int(input("Nb de devis de la semaine : "))

print('Devis des conseillers :', devis)

# maintenant pour calculer les commissions, 
# on va devoir d'abord créer un tableau pour enregistrer la valeur de chaque conseiller
commission = [ 0 for col in range(nbConseil)]

# puis on aura besoin d'une boucle pour parcourir ligne par ligne (conseiller par conseiller)
# pour chaque conseiller, on peut faire une 2ème pour parcourir toutes les semaines de ce conseiller
# (ou utiliser simplement l'appel sum() avec la ligne correspondant au conseiller)
for conseiller in range(nbConseil) :
    print('Conseiller ', conseiller)

    # on peut utiliser la fonction sum pour faire la somme de la ligne du conseiller
    somme = sum(devis[conseiller])
    print("devis réalisés dans la semaine ", somme)

    # ou on peut faire avec une boucle comme ici 
    # (décommenter en supprimant les """ si vous voulez ça)
    """somme = 0
    nbSemaines = len(devis[conseiller])    # taille de la ligne
    for sem in range(nbSemaines) :
        somme += devis[conseiller][sem]
    """    
    commission[conseiller] = somme * 100

print('commissions à payer : ', commission)


