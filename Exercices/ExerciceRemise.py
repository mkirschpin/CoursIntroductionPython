# Exercice Remise
# Dans une boutique de vêtements, on souhaite appliquer une remise de prix en fonction
# de la valeur total des achats. 
# Pour plus de 50€ en achat, on souhaite offrir aux clients une remise de 10%. 
# Pour plus de 100€ d’achat, on lui offrira une remise de 20%, alors que pour 
# plus de 150€ d’achats, on offrira 25%.
# Proposez un programme permettant à l'utilisateur de renseigner le montant d'achat
# et calculer la valeur de la remise à partir d’un montant renseigné.

# en entrée, on a besoin du montant total d'achat. On la demande à l'utilisateur
montant = float (input ("montant ? "))

if montant >= 150 :
    remise = montant * 0.25
elif montant >= 100 :
    remise = montant * 0.20
elif montant >= 50 :
    remise = montant * 0.10
else :
    remise = 0

montant = montant - remise

print ('remise : ', remise)
print ('montant mis à jour :' , montant)