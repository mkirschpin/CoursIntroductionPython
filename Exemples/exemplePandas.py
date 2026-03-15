# d'abord on importe la bibliothèque pandas
# comme ça on peut l'utiliser dans notre code

import pandas as pnd

# on va créer notre premier DataFrame
monDF = pnd.DataFrame ( 
  { 'Habitants' : [ 8, 70, 320, 1200 ],
		'Capital': ['Geneve', 'Paris', 
                'Washington', 'Pequin'] },
		index=['Suisse', 'France', 'USA', 
           'Chine'] )

print (monDF)

print ('Les capitals :')
# avec monDF['Capital'] on récupère 
# toute la colonne nommée Capital et 
# avec print, on les affiche
print ( monDF['Capital'] )

# on peut aussi chercher une valeur parmi
# celles utilisées comme "index" du DF
# pour cela, nous utilisons loc

infoFR = monDF.loc['France']
print ('Infos France :')
print (infoFR)

print ()
print ( monDF.info() )  # on affiche les informations sur le DataFrame
print ()
print ( monDF.describe() )  # analyse rapide sur les données numériques
print ()
print ( monDF.sample(1) )  # on affiche un échantillon aléatoire
print ()

# on peut également récupérer des infos à partir d'un fichier

ventes = pnd.read_csv('http://www.kirschpm.fr/cours/PythonDataScience/files/VentesPropre.csv', 
                     delimiter=';',
                     header=[0],
                     index_col=[0])

print ("Données de ventes : ")
print ( ventes.info() )      # on affiche les informations sur le DataFrame

print ( ventes.head() )       # on affiche les premières lignes
print ( ventes.describe() )   # analyse rapide sur les données numériques (ici le montant)

print ()
print (ventes.sum(numeric_only=True) )
print (ventes.mean(numeric_only=True) )

print ( ventes.count() )