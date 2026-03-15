# Exercice : calcul impots à la République des Bananes 
# Nous avons trois tranches d’impôts : 
#   < 9 000,00 ne sont pas imposables  
#   entre 9 000,00 et 15 000,00 paient 15% d’impôt 
#   >  15 000,00 doivent payer 20% d’impôts sur leurs revenus. 
# Trois types de revenus sont imposables : 
#   les salaires, les primes et les heures complémentaires, 
#   mais uniquement si on a reçu des aides à la formation . 
# Notre programme devra comptabiliser l’ensemble de revenus reçus par un citoyen, 
# avant d'identifier sa catégorie d’imposition et calculer le montant d’impôts à payer. 
# Les revenus seront stockés dans un tableau contenant 4 positions : 
#   le montant de salaire ; le montant des primes ; 
#   le montant des heures complémentaires ; et le montant d’aides à la formation . 
# 

# on demarre par créer un tableau vide pour acceuillir les valeurs
revenus = [ 0 , 0 , 0 , 0]          

# puis on demande à l'utilisateur les valeurs pour le tableau
revenus[0] = float(input('Montant salaire : '))
revenus[1] = float(input('Montant primes : '))
revenus[2] = float(input('Montant heures complémentaires :'))
revenus[3] = float(input('Montant aides formation : '))

# on fait la somme des revenus 
somme = revenus[0] + revenus[1]
# les heures comp ne se comptabilisent que s'il y a une aide à la formation
if revenus[3] > 0 :
    somme += revenus[2]

# maintenant on essaie de trouver la bonne categorie
if somme < 9000.00 :
    taux = 0
elif somme > 15000.00 :
    taux = 0.20
else :
    taux = 0.15

# et on calcule l'impot
impot = somme * taux

print ('Total des revenus imposables :', somme)
print ('Impot à payer : ', impot)

