# exemple tuple
# une tuple est un ensemble ordonné des valeurs (comme les listes)
# mais contrairement à la liste, on ne peut plus les modifier

# création d'une tuple avec le () et pas les []
annees = ( 'L1', 'L2', 'L3' )
print(annees)

# on peut accéder à chaque élément grâce à sa position (comme les listes)
print ('1er année :', annees[0] )

# on peut créer un tuple à partir d'un tableau 
tab = [ 10 , 12 , 14, 16 ]
mention = tuple(tab)
print (mention)

# ou d'une string
valeurs = input('un message ?')
tup = tuple(valeurs)
for val in tup :
    print (val, end='...')
print()

# on peut lui demander sa taille, tester des valeurs avec in (comme les listes)
print ('années en licence :', len(annees))
print ('M1 inclus ?', ( 'M1' in annees ) )
print ('position L3 :', annees.index('L3'))

# mais si on essaie de modifier une tuple, on aura une erreur
#tup[0] = 'a'
