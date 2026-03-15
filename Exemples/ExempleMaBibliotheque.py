# Exemple d'usage d'une bibliothèque qu'on a définit
#  
# on peut utiliser une bibliothèque qu'on a fait facilement
# juste en important les fonctions qui nous intéressent 
# (comme on fait avec n'importe quel bibliothèque)
#  

from MaBibli import surfaceRectangle

larg = float (input('Largeur ? '))
haut = float (input('Hauteur ? '))
print (larg, 'x', haut)

surface = surfaceRectangle(larg, haut)
print ('surface :', surface)
