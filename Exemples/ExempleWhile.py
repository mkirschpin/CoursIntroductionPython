#exemple While

#entree
salaire = float(input('Salaire initial ? '))

#etat initial
somme = 0 

      # condition  
while salaire > 0.0 :
    somme = somme + salaire
    # mise à jour variable de controle
    salaire = float(input('Nouveau salaire ? (-1 pour sortir) '))
 
# print('Total reçu : %.2f euros ' % somme)   # alternative
print('Total reçu : {:.2f} euros '.format(somme))


# on remplit un tableau avec 4 revenus (comme dans l'exo "republique des bananes")
revenus = [ 0, 0, 0 , 0 ]

taille = len(revenus)
compteur = 0

while compteur < taille :
    revenus[compteur] = float(input('Revenu : '))
    compteur += 1   # équivaut à compteur = compteur + 1

print(revenus)


