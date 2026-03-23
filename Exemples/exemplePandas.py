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


# on peut également faire des petites statistiques sur les données numériques du DataFrame
# comme ici la somme (sum) ou encore la moyenne (mean)
print ()
print ('Somme des valeurs numériques :',ventes.sum(numeric_only=True) )
print ('Moyenne de valeurs numériques :', ventes.mean(numeric_only=True) )

# on peut également compter le nombre de valeurs présentes dans chaque colonne
print ( ventes.count() )

# et si on veut faire ça sur une seule colonne, il suffit de la cibler
print ('Total de ventes:', ventes['MONTANT'].sum() )
print ('Nombre de vendeurs :', ventes['VENDEUR'].count() )

# on peut grouper les valeurs d'une colonne pour faire les statistiques
# par exemple, la somme des ventes par vendeur
# il s'agit d'une opération semblable à un "group by" en SQL$
print ('Moyenne des ventes par vendeur :')
print (ventes.groupby(by='VENDEUR').mean())

print ('Somme des ventes par secteur :')
print (ventes.groupby(by='SECTEUR').sum())
