# Exercice Fleuriste : calculer le prix du bouquet 
# Le prix du bouquets est calculé en fonction du nombre de fleurs et du message 
# Chaque fleur est facturée 4€. 
# Si le message contient + de 10 mots, on facture 0,10€ par mot, 
# sinon on facture 0,05€ par lettre. 
# On demande à l'user le nbr de fleurs et le message, et à la fin on affiche le prix calculé.


# on commence par demander le nombre de fleurs et le message
nbFleurs = int(input('Nombre de fleurs au bouquet ? '))
message = input('Message ? ')               

# pour aller plus loin : 
# on peut garder les valeurs des prix (par fleur, par lettre, par mot)
# sur des contantes, pour pouvoir les changer (si nécessaire) plus facilement
PRIX_FLEUR = 4
PRIX_MOT = 0.10
PRIX_LETTRE = 0.05  
NB_MOTS = 10            # idem pour la limite de nb mots (pour changer le mode de facturation)

# on calcule d'abord le prix des fleurs 
prixFleurs = nbFleurs * PRIX_FLEUR

# on va parcourir le message pour savoir le nb de mots et de lettres
# attention le message peut être vide
nbMots = 0
nbLettres = 0

# la boucle for permet de parcourir la totalité d'un string (vu comme un tableau)
for lettre in message :
    if lettre.isspace() :
        nbMots += 1
    else :
        nbLettres += 1

print ('Nb de mots :',nbMots, 'Nb de lettres :',nbLettres)

# on peut aussi faire comme dans les algos qu'on a fait en TD.
#taille = len(message)
#compteur = 0
#while compteur < taille :
#  if message[compteur].isspace() :
#    nbMots = nbMots +1
#  else :
#    nbLettres = nbLettres + 1
#  compteur = compteur + 1  

# est-ce qu'on a compté le dernier mot ? :D
# soit on fait cadeau au client, soit on corrige cela
if len(message) > 0 : 
    nbMots += 1 # si on ne veut pas faire cadeau ;-)  

print ('Nb de mots :',nbMots, 'Nb de lettres :',nbLettres)


if nbMots >= NB_MOTS :
    prixMessage = nbMots * PRIX_MOT
else :
    prixMessage = nbLettres * PRIX_LETTRE 

prixBouquet = prixFleurs + prixMessage

print('Prix bouquet : %.2f (dont %.f pour les fleurs et %.2f pour le message).' \
    % (prixBouquet, prixFleurs, prixMessage) )  # attention à ne pas oublier les () ici


