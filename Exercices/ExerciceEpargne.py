# Exercice épargne
# Une banque veut offrir à ces clients la possibilité de simuler un investissement de
# type épargne. Celui-ci offre pendant les 3 premières années un taux de 2% à l’an et
#  de 1,5% pour les années suivantes. 
# Le programme devra, à partir d’un montant initial renseigné par le client, 
# afficher une prévision des gains pour les 8 prochaines années.

# nous avons besoin de connaitre le montant initial. On le demande au client
montant = float (input("Montant initial ? "))

# pour aller plus loin : on peut garder les valeurs des taux dans des "constantes"
# (variables dont la valeur ne change pas) 
# ainsi, on pourra les changer plus facilement
TAUX_DEBUT = 0.02
TAUX_FIN = 0.015
DUREE = 8                       # même chose pour la durée 

# on simule les gains pendant 8 ans 
# on a besoin alors d'une boucle : chaque tour de boucle nous représente une année

# checklist boucle : état initial
gains = 0                           # au début, aucun gains
compteur = 1                        # compteur se place à la première année

# checklist boucle : la condition 
while compteur <= DUREE :
    # on trouve le bon taux à appliquer
    if compteur <= 3 :
        taux = TAUX_DEBUT
    else :
        taux = TAUX_FIN

    gains = gains + (montant * taux)        # on applique le taux
    montant = montant + gains               # on met à jour le montant

    print('Année ', compteur)
    print('gains : ', gains)                # on affiche les gains 

    # checklist boucle : mise à jour variable de contrôle
    compteur = compteur + 1

# on termine par afficher le montant final
print('montant final : ', montant) 