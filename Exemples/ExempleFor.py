#exemple boucle for

#la boucle for ("for each") permet de parcourir tous les éléments d'une collection 
#une collection ça peut être un tableau, une string, une liste... 

texte = input('Entrer un message : ')

voyel = 0

#pour chaque lettre c dans la varible texte
for c in texte :
    #print(c)
    #l'opérateur in vérifie si un élément c fait partie d'une collection
    if c.lower() in 'aeiou' :
        voyel += 1   #ça équivaut à dire voyel = voyel + 1

print('{} a {} voyelles'.format(texte, voyel))


# la classe range permet de créer une liste de numéros entiers
# qui va être fort utile pour les boucles for 
# par exemple, ici, on va générer une liste de numéros entiers
# avec autant de numéros que de voyels de mon texte, en commeçant par 0
for i in range(voyel) :
    print('.'*i, i)
print("Booooommmm !! :-)")


# on peut contrôler le range pour faire un range allant d'une valeur x
# à une valeur y (sans l'inclure) avec un certain pas (step)
x = int(input("debut : "))
y = int(input("fin :"))
step = int(input("step :")) 
for i in range(x,y,step) :
    print('.'*i, i)
print('Booommm.... :-)')
