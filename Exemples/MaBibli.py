# Exemple de définition d'une bibliothèque
#
# on peut facilement créer sa propre bibliothèque en réunissant plusieurs de nos fonction
# on réunit dans un même fichier des fonctions sur un même sujet
# on peut alors réutiliser plus facilement ces fonctions, en important la bibliothèqe

# une première fonction sur le 
def volumeCube (cote) :
    """ Documentation : fonction calculant le volume d'un cube """
    volume = cote ** 3
    return volume

def translatRectangle (largeur, hauteur) :
    """ fonction qui fait le translade d'un rectangle 
    (hauteur devient largueur et vice-versa) """
    return hauteur, largeur 


def surfaceRectangle (largeur, hauteur) :
    """ calcul de la surface d'un rectangle (hauter x largeur) """
    return (largeur * hauteur)


