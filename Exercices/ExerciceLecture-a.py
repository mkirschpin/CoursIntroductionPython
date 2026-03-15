# Exercice : 
# a) Le programme doit permettre à un utilisateur de rentrer plusieurs valeurs. 
#    et indiquer si la valeur renseignée ne contient que des lettres ou 
#    s’il s’agit d’un numéro entier positif . 
#    Le programme doit s’arrêter si l’utilisateur entre la valeur « fin ». 
# b) Le programme doit enregistrer dans un tableau les valeurs qui correspondraient à
#    des numéros entiers. 
#    Il faut Aaficher le tableau avant de terminer le programme. 
# c)  Trouver des fonctions permettant de calculer la moyenne, le min et le max du tableau. 
#     Afficher ces valeurs avant de terminer le programme. 


# premier partie : boucle de lecture
# on fait une boucle pour demander à l'utilisateur de renseigner une valeur
# on ne sortira que lorsqu'il aura renseigner "fin"

valeur = input ('Entrer une valeur : ')

while (valeur.lower() != 'fin') :           # lower pour éviter des soucis si l'user entre Fin 
    if (valeur.isalpha()) :
        print ('La valeur ne contient que des lettres')
    elif (valeur.isdigit()) :
        print ('La valeur est un entier positif')
    else :
        print ('La valeur contient des lettres et des chiffres')

    # on demande une nouvelle valeur (mise à jour variable de contrôle)
    valeur = input("entrer une nouvelle valeur : ")


