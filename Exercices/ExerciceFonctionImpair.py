# Exercice : compter le nombre de n°s impair existent dans un tableau
# en utilisant la fonction "estPair" (ou estImpair, au choix) qu'on vient de créer

# d'abord on va importer la fonction qu'on vient de créer
from FonctionEstPair import estPair

# on va créer un tableau vide, où on gardera les numeros lus
tableau = []

# on lit un premier numéro
numero = int(input('Entrer un numéro (entrer un numéro négatif pour arrêter) : '))

# numero devient notre variable de contrôle 
while numero >= 0 :
    tableau.append (numero)
    
    # on met à jour la variable de contrôle
    numero = int(input('Entrer un numéro (entrer un numéro négatif pour arrêter) : '))

print(tableau)

# on parcours le tableau pour compter le nombre d'impairs
nbImpairs = 0 

# pour parcourir plus facilement le tableau, on peut utiliser une boucle for
for numero in tableau :
    # si est impair on ajoute 1 à nbImpair
    if (not estPair(numero)) :
        nbImpairs += 1

print ('Nombre de numéros impairs :', nbImpairs)