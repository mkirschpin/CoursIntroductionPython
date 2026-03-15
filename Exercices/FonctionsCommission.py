# Exercice Commissions - avec fonctions
# fonctions pour le calcul de commissions

def calculCommission(devis) :
    # on decouvre d'abord combien de conseillers on a
    nbConseil = len(devis)

    # on va devoir d'abord créer un tableau pour enregistrer la valeur calculée  
    # pour la commission de chaque conseiller
    commission = [ 0 for col in range(nbConseil)]

    # puis on aura besoin d'une boucle pour parcourir ligne par ligne (conseiller par conseiller)
    # pour chaque conseiller, on récupère sa ligne et on fait la somme des devis 
    # (à l'aide de la fonction sum())
    for conseiller in range(nbConseil) :
        somme = sum(devis[conseiller])
        commission[conseiller] = somme * 100
    
    return commission
