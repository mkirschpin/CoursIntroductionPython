# Exemples usage de certaines bibliothèques standards

# d'abord, on importe les fonctions qui nous intéressent
from math import sqrt, pi
from datetime import datetime as dt     # as permet de faire un alias, plus court
                                        # très utile pour importer une classe
                                        # au lieu de parler datetime, on dit dt         

# on récupère la valeur de la constante pi
print ('pi = ',pi)

# on peut calculer une racide carrée avec sqrt
numero = float(input('numéro ? '))
racine = sqrt(numero)
print('racine :',racine)

# l'opération .today() de la classe datetime donne la date d'aujourdh'ui 
auj = dt.today()
print('auj :', auj.date())

# on peut aussi convertir des texte en dates 
unjour = input('un jour (JJ/MM/AAAA) ? ')
jour = dt.strptime( unjour ,'%d/%m/%Y') 
print('format ISO:', jour.date())

# et des dates en texte
unjour = auj.strftime('%d/%m/%Y')
print('auj :', unjour)
