# un range est une séquence de numéros entiers, qu'on va utiliser surtout pour les for 
# on peut faire un range(debut, fin, step) qui va de début jusqu'à la fin (sans l'inclure)
# en avaçant pas à pas (step)

r1 = range(5)               #range allant de 0 à 5 (sans l'inclure), de un à un
print(r1)                   
print(type(r1))             # range est un classe, r1 est un object contenant la sequence de numéros 

print('range(5)')
for i in r1 :               # si on utilise notre range dans un for, on voit apparaitre les numéros 
  print(i, end=' ')         # ici l'option end=' ' remplace la nouvelle ligne par un espace
                            # on voit donc apparaitre 0 1 2 3 4

print('\n range(1,5)')      # range allant de 1 à 5 (sans l'inclure), un par un
for i in range(1,5) :       # on voit donc apparaitre 1 2 3 4 
  print(i, end=' ')

print('\n range(0,5,2)')    # range de 0 à 5 (sans celui-ci), avançant 2 par 2
for i in range(0,5,2) :     # on voit donc apparaitre 0 2 4
  print(i, end=' ')

print()