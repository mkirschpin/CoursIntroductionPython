# petit exemple pour bien penser à toutes les situations
# scenario : entreprise de formation continue, on s'inscrit et on peut suivre
# à autant de matières qu'on le souhaite. Mais on n'aura l'attestation de
# réussite que si on réussit plus de matières qu'on en échoue.
# L'appli doit permettre un candidat de renseigner ses notes pour savoir
# sa moyenne et s'il aura droit à l'attestation de réussite ou pas. 

# état initial
somme = 0
nbReussi = 0
nbEchec = 0 

note = float(input('Entrer une note (-1 pour sortir) : '))
      #conditon 
while note > 0 : 
    somme += note 

    #on comptabilise la note en tant que réussite ou échec 
    if note >= 10.0 :
        nbReussi += 1
    else :
        nbEchec += 1

    note = float(input('Entrer une note (-1 pour sortir) : '))

# moyenne = somme / nb de notes (qui est le nb d'échecs + ceux de réussites)
# la ligne ci-dessous pourrait être source de bug
# moy = somme / (nbEchec + nbReussi)

#que se passe-t-il si on n'a rentré aucune note ? (i.e. renseigné -1 à l'input) ?
#nbReussi et nbEchec resteront à 0
#le calcul de moyenne risque alors une division par zéro.  
# 
if nbReussi > 0 or nbEchec > 0 :
    moy = somme / (nbEchec + nbReussi) 
else :
    moy = 0  #ça veut dire qu'on n'a pas eu des notes renseignées

print('Moyenne : ', moy)

if nbReussi > nbEchec :
    print("Formation validée !")
else :
    print('Formation non-validée.')

