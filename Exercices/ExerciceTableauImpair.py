# Exercice : compter le nombre de n°s impair existent dans un tableau
# Demander à l'utilisateur de renseigner un tableau (on s'arrete dès que  
# l'utilisateur renseigne un numéro < 0), 
# puis parcourrir le tableau et compter le nombre de valeurs impairs

# on commence par créer un tableau vide, où on gardera les numeros lus
tableau = []

# on lit un premier numéro
numero = int(input('Entrer un numéro (entrer un numéro négatif pour arrêter) : '))

# numero devient notre variable de contrôle 
while numero >= 0 :
    tableau.append (numero)
    
    # on met à jour la variable de contrôle
    numero = int(input('Entrer un numéro (entrer un numéro négatif pour arrêter) : '))


# on parcours le tableau pour compter le nombre d'impairs
nbImpairs = 0 

# pour parcourir plus facilement le tableau, on peut utiliser une boucle for
for numero in tableau :
    #on vérifie si c'est par ou impair
    reste = numero % 2 

    if reste == 0 :
        estPair = True
    else :
        estPair = False
        nbImpairs += 1

    # on affiche ce qu'on a trouvé
    print(numero, 'est pair ?', estPair)

print ('On a trouve %d numeros impairs ' % nbImpairs)