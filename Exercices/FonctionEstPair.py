# Exercice : Pair ou Impair
# créer une fonction pour savoir si un numéro est pair ou impair

# fonction pour savoir si un numéro est pair
def estPair(numero) :
    # on calcule le reste
    reste = numero % 2 

    # on vérifie si c'est par ou impair
    if reste == 0 :
        estPair = True
    else :
        estPair = False

    # on retourne une réponse
    return estPair


# on peut faire la même chose avec impair
def estImair(numero) :
    # on calcule le reste
    reste = numero % 2 

    # on vérifie si c'est par ou impair
    if reste == 0 :
        estImpair = False
    else :
        estImpair = True

    # on retourne une réponse
    return estImpair
