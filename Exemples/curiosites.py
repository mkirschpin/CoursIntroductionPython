#quelques curiosités en Python

temp = float(input('Temperature ? '))

#expression logiques du type val < var < val sont acceptées
if 35 < temp < 37 :
    print ('Etat normal')

#ça équivaut à dire 
if temp > 35 and temp < 37 :
    print ('Etat vraiment normal')

##################

prix = 1000.00
nbPart = int(input("Nb participants ? "))

#l'analyse d'une expression logique s'arrête dès qu'on a une réponse sûre
#si nbPart=0, on s'arrêtera sans évaluer la 2è partie, car on aura FAUX forcément

if nbPart > 0 and prix/nbPart > 10 :
    contribMin = prix/nbPart
else :
    contribMin = 10

print ('Pour %d participants, et un cadeau à %.2f, chacun doit donner %.2f ' \
    % (nbPart, prix, contribMin)) 
