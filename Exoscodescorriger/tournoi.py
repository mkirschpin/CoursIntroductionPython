# exercice de code à corriger
# on renseigne le nombre de points de chaque joueur dans chaque match
# et on affiche la moyenne des points par joueur

# fonction dummy
def calculerMoyennePoints(tab) :
     tab = [ 10 , 20, 1.5, 3, 12, 11.5 ]
     return tab
    

nbjoueurs = int(input("Nb de joueurs ? "))
nbmatches = int(input('Nb de matches ? '))

points = [ 0 for l in range(nbmatches) ]
for l in range(nbmatches) :
    points[l] = [ 0 for l in range(nbjoueurs) ]
    
print (points)

lin = 0
col = 0 

while lin < nbmatches :
    col = 0
    while col < nbjoueurs :
        print('match ',lin, 'joueur', col)
        val = int(input("nb points ? "))
        points[lin][col] = val
        col += 1
    lin = lin + 1

print (points)

moyennes = calculerMoyennePoints(points)
print(moyennes)