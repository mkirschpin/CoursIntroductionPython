# Exercice : calculer  le montant total des commissions pour un ensemble de conseillers
# On va utiliser pour cela la fonction calculCommission qu'on a construit

# on va donc importer la fonction dont on aura besoin
from FonctionsCommission import calculCommission 

# tout d'abord il faut demander combien de conseillers nous avons
# puis créer et remplir le tableau des devis en conséquence

nbConseil = int(input("Nb de conseillers ? "))

devis = [ 0 for lin in range(nbConseil) ]

# on peut utiliser un while ou un for en guise de boucle
for compteur in range(nbConseil) :
    # on va créer le tableau contenant le devis de ce conseiller
    devis[compteur] = [ 0 , 0 , 0 , 0 ]         # ou [ 0 for col in range(4) ]

    print ("conseiller n° ", compteur)

    for sem in range(4) :
        devis[compteur][sem] = int(input("Nb de devis de la semaine : "))

print('Devis des conseillers :', devis)

# maintenant pour calculer les commissions, avec la fonction calculCommission
commissions = calculCommission(devis)

print('commissions à payer : ', commissions)


