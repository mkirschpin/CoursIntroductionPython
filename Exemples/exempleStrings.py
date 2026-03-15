#exemple sur la manipulation des string

nom = 'Toto'
premier = nom[0]    #une string peut être vue comme un tableau de lettres
dernier = nom[3]

print(premier, dernier)

# par contre, une string ne peut pas être modifiée (elle est "immutable")
# la ligne ci-dessous genere une erreur " 'str' object does not support item assignment"
#nom[1]='a'

#on peut faire plein des choses avec les strings
nom = input("nom ? ")

taille = len(nom)   #on peut trouver sa taille (comme les tableau)
premier = nom[ 0 ]
milieu = nom[taille // 2]
dernier = nom[ -1 ]
print('taille :', taille )
print(premier, milieu, dernier)

#on peut convertir en majuscule ou minuscule 
print (nom.upper())
print (nom.lower())

#on peut chercher un 'patron' (une string dans une autre string)
pos = nom.find('ele')
print('il y a un "ele" à la position ? ', pos)
trouve = nom.endswith('ele')
print('ça termine par "ele" ? ', trouve)

#on peut comparer les strings avec les opérateurs logiques (==, !=, >, <, etc.)
print ('le nom est egale à "ele" ? ', (nom == 'ele')) 
print ('le nom est suppérieur à "Titi" ? ', (nom > 'Titi'))

#on peut aussi tester ces éléments (sont-ils des lettres, les chiffres... ?)
estUnEspace = dernier.isspace()
estLettre = dernier.isalpha()
estChiffre = dernier.isdigit()

print ('le dernier est un espace ? ', estUnEspace)
print ('le dernier est une lettre ?', estLettre)
print ('le dernier est un chiffre ?', estChiffre)

#on peut le faire aussi avec le string tout entier, pas que avec les lettres
print ('nom ne contient que des lettres ? ', nom.isalpha())
print ('nom est un numéro entier positif ? ', nom.isdigit())
print ('nom ne contient que des espaces vides ? ', nom.isspace())
