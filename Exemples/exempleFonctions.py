# Exemples Fonctions
# exemples de création et usage des fonctions

# un fonction doit être définie avant d'être utilisée
# soit on va la définir dans le même fichier (comme ici)
# soit on la définit dans un autre fichier et on fait alors un import
# from NomFichierSansExtentionPy import NomDeLaFonction

# pour définir une fonction, on va faire utiliser "def"
# def NomDeLaFonction (paramètres) :

# exemple fonction qui calcule le volume d'un cube
# les paramètres reprèsentent des variables qui sont être utilisées dans la fonction
def volumeCube (cote) :
    """ Documentation : fonction calculant le volume d'un cube """
    volume = cote ** 3
    return volume


# exemple fonction avec plusieurs valeurs retournées
# dans ce cas, c'est comme si on retournait un tuple
def swap (x, y) :
    return y, x


# les 1ers paramètres sont obligatoires, puis on peut indiquer les paramètres optionnels
# les paramètres optionnels sont une valeur par défaut, les variables auront la 
# valeur par défaut si aucune valeur n'est indiquée lors de l'appel de la fonction 
#
# Exemple : cette fonction doit valider si un mot de passe suit les règles
# longueur min, nb de chiffre min, nb de majuscules min, nb caractères spéciaux min 
def validerMdP (mdp, longueur = 8, chiffres = 1, maj = 1, speciaux = 1 ) :
    # message de documentation entre """ """ (3 " de chaque côté)
    """ Fonction permettant de vérifier si un mot de passe suit les règles :
        Il doit avoir une longueur d'au moins 8 caractères, dont au moins 
        1 majuscule, 1 caractère spécial et au moins 1 chiffre. 
    """
    nbChiffres = 0
    nbMaj = 0
    nbSpec = 0

    for lettre in mdp :
        if lettre.isupper() :       # c'est une majuscule
            nbMaj += 1
        elif lettre.isdigit() :     # c'est un chiffre
            nbChiffres += 1
        elif not lettre.isalpha() : # ce n'est pas une lettre 
            nbSpec += 1
    
    taille = len(mdp)
    if ( taille >= longueur and nbMaj >= maj and \
         nbChiffres >= chiffres and nbSpec >= speciaux ) :
        estValide = True
    else :
        estValide = False
    
    #print ('chffres', nbChiffres, 'maj', nbMaj, 'speciaux', nbSpec, 'longueur', taille, ':', estValide)
    return estValide


# usage des fonctions 
cot = float(input('cote ? '))
vol = volumeCube(cot)
print ('volume :', vol)

# appel fonction avec paramètres par defaut
motdepasse = input('Mot de passe : ')
valide = validerMdP(motdepasse)
print ('valide ?', valide)

# et maintenant avec autres paramètres 
valide = validerMdP(motdepasse, longueur=10, maj=2, chiffres=2)
print ('valide ?', valide)

# appel fonction qui retourne plusieurs valeurs de retour
a = 3
b = 2
print (a,b)
a,b = swap (a,b)    # les variables recoivent les valeurs retournées dans l'ordre
print (a,b)
tup = swap(a,b)     # on peut également affecter les valeurs à un tuple
print (tup)
print (type(tup))
