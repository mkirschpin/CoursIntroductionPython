#exemple boucle infinie

#entree
salaire = float(input('Salaire initial ? '))
somme = 0 

while salaire > 0.0 :
    somme = somme + salaire
    print(somme)
    
# mise à jour variable de controle a été mise à l'extérieur de la boucle
#(en reduisant le nombre d'espaces)
salaire = float(input('Nouveau salaire ? (-1 pour sortir) '))
 
print('Total reçu : %.2f euros ' % somme)
