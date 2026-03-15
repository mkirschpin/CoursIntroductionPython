#exemple usage Si

# on lit une valeur 
x = int(input('x ? '))

if x < 0 :                      # si la condition est vraie, on entre dans le bloc
    print (x, 'est négatif')    # attention au nb d'espaces avant le print
else :                          # si la condition est fausse, on vient ici
    print (x, 'est positif')    # le nb d'espaces avant le print indique le bloc
                                # dès que le nb d'espaces sera différent, on "sort" du bloc
print('suite...')

# on peut avoir une structure qui enchaine les if : if cond - elif cond - else 
if x < 0 :
    print (x, '< à 0')
elif x > 0 : 
    print (x, '> à 0')
else :
    print ('zéro')
print('suite...')
  
# et on peut avoir un if sans else 
if x >= 0 :
    print (x, 'positif ou 0')
print('suite...')

# on peut enchainer autant de "elif" qu'il nous faudra
temp = float(input('Température ? '))
etat = ''

#si on renseigne une temperature positive, la variable état n'aurait pas 
#été définie et on aura une erreur. Pour éviter cela, il faut décommenter
#la ligne n° 4, où on definit la variable etat. 

if temp >= 40 :
    etat = 'hyperthermie'
elif temp >= 37 :
    etat = 'fièvre'
elif temp > 35 :
    etat = 'normal'
else :
    etat = 'hypothermie'

print ('Etat : ', etat)
