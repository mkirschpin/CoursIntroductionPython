# exemple discutant certaines curiosités sur les collections 

# commençons par les indices (positions) dans les collections 
# une collection est un ensemble ordonné d'éléments, comme une liste (tableau) ou une string
# chaque valeur est accessible par sa position, indiquée par l'indice
#  
tab = ['a','b','c','d']
milieu = len(tab)//2    # division entière // car les indices doivent tjs être des entiers
print (tab, 'milieu est à la position', milieu)

# on peut récupérer des "tranches" (slices) de collection avec en indiquant [début : fin]
# attention, le contenu de la position "fin" n'est jamais inclus
debut = tab[:milieu]                # tranche de la position 0 à 2 (valeur de milieu) 
fin = tab[milieu:]                  # tranche de la position milieu jusqu'à la dernière
coeur = tab[milieu-1 : milieu+1]    # tranche de la position 1 (milieu-1) à 3, sans inclure celle-ci
print(debut, coeur, fin, sep='**')  # l'option sep='**' fait qu'on remplace les espaces entre les var par des * 

# avec le [:] (de 0 à la dernière position), on fait une copie de la collection
copie = tab[:]               
copie[-1] = 'fin'
print(tab)
print(copie)

print('originel', tab, 'copie', copie)   # on a pu changer la copie sans toucher l'originel

# On peut faire la même choise avec les string, qui sont des collections de lettres 
nom = 'Toto et Titi'
print(nom[:4])
print(nom[4:8])
print(nom[8:])

# par contre, les string sont non-modifiables, ellent ne peuvent pas être modifiées
# par exemple, la ligne ci-dessous causerait une erreur (si on lui enlève le #)
# nom[-1] = 'fin'

# enfin, on peut avoir des index negatifs 
# c.a.d. des positions a partir de la fin
print(nom[-4:])         # ça donnera juste Titi
print(copie[-1])        # ça nous donnera la dernière valeur de copie, qui est 'fin'


# maintenant on regarde l'appartenance d'un élément à une collection 
element = 'b'
print (element, 'in', tab, ( element in tab ) )             # True si l'élément y est
print (element, 'not in', nom, ( element not in nom ) )     # True si l'élément n'y est pas

# on peut trouver la première position où apparaît l'élément et le nb de fois où il apparaît  
indice = tab.index('c')
nbfois = nom.count('t')
print ('indice "a"', indice)
print ('nb fois "t"', nbfois)
