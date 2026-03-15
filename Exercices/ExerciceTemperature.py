# Exercice : à partir de la température d'un patient, indiquer son état
# Si >= 40 le patient est en état de hyperthermie
# Si >= 37 et < 40 son état est en fièvre
# Si > 35 et < 37 son état est normal
# Si >= 37 le patient est en état de hypothermie

# on démarre par récupérer la température du patient
temp = float(input('Temperature ? '))       # attention à convertir en float le texte lu du clavier

# différentes formes d'organiser la séquence de tests est possible
# penser à tester toutes les possibilités
if temp >= 40 :
    etat = 'hyperthermie'
elif temp >= 37 :
    etat = 'fièvre'
elif temp > 35 :
    etat = 'normal'
else :
    etat = 'hyperthermie'

# on termine par afficher l'état du patient 
print ("L'état du patient est :" , etat)