# Exemple Fonctions
# l'usage de fonctions implique faire attention à quelques points
# notamment par rapport aux paramètres 

# imaginons une fonctin qui calcule une remise 
def calculerRemise(montant) :       # la variable montant sera déclarée automatiquement
    if 100 <= montant < 150 :       # avec une "copie" de valeur qu'on aurait donnée en
        remise = montant * 0.10     # appellant la fonction 
    elif montant >= 150 :
        remise = montant * 0.20
    else :
        remise = 0
    montant -= remise                         # ça change la variable "local" (ici)
    print ('dans la fonction :',montant)      # mais pas celle dans le code principal

    return remise                

# maintenant, on considère une fonction qui modifie un tableau bidimensionnel
# produits avec les noms des produits dans la 1er dimension [0], et les prix en 2ème [1]   
def ajouterProduit (produits, nomprod, prixprod) :
    produits[0].append(nomprod)         # on modifie ici le tableau
    produits[1].append(prixprod)        # la modification sera sentie dans l'originel  

    print ('dans fonction :', produits)
    # la fonction se termine avec le bloc, pas de retour ici

# même chose pour un tableau d'une seule dimension
# le tableau "pointe" vers les valeurs, c'est cette indication (comme une adresse)
# vers les valeurs qui est "copiée" dans la variable tableau, 
# ce qui fait que si on change tableau, l'originel va se change, puisqu'on va 
#  directement dans "l'adresse" où se trouvent les vraies valeurs les modifier
# ce ne sera pas le cas de la variable "val", puisqu'il s'agit d'une valeur "simple"
# Python se contente de recopier la valeur qu'il y a dedans. 
def changeTableau (tableau, val) :
    tableau.append(val)
    print('dans fonction: ',tableau)
    
# et si on déclare un tableau dans la fonction et qu'on le retourne ? que se passe-t-il ?
def lectureValeur (message, nbValeurs) :
    tableau = [ None ] * nbValeurs       # on va creer un tableau vide

    for i in range(nbValeurs) :
        tableau[i] = input(message)

    print (tableau)
    return tableau

# ########################################### #
# code principal -> qui utilise les fonctions 

# on va tester la fonction calculerRemise et voir ce qui se passe avec le montant 
montant = float(input('montant ? '))
print ('avant la fonction :', montant)

remise = calculerRemise(montant)
print('après fonction :', montant)  # la variable ici reste inchangée

print('remise :', remise)

# maintant on teste la fonction avec le tableau
produits = [ ['Raclette', 'Comte'] , [ 9.50 , 12.50  ] ]
print ('avant fonction :', produits)

ajouterProduit(produits, 'Emental', 8.50)
print ('après fonction :', produits)        # le tableau produit sera changé !

tab = [ 0, 2, 15 ]
print ('avant fonction :', tab)
changeTableau (tab, 35)                     # même chose pour le tableau "tab"
print('après fonction :', tab)

lecture = lectureValeur('une lettre ? ', 3) # on peut même récupérer un tableau créé dans la fonciton 
print (lecture)                             

