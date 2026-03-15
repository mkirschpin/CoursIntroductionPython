# Exercice : identifier si un numéro est pair ou impair
# Concevoir un programme capable demander à son utilisateur un numéro, 
# puis de lui indiquer à l’écran si un numéro est pair ou impair.

# on commence par lire le numéro
numero = int(input('Entrer un numéro : '))

#on vérifie si c'est par ou impair
reste = numero % 2 

if reste == 0 :
    estPair = True
else :
    estPair = False

# on affiche ce qu'on a trouvé
print(numero, 'est pair ?', estPair)