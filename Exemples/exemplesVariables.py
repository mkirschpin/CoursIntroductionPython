#exemple sur les variables
nom = 'Toto'    # on définit une variable à son premier usage
print('Hello ! Je suis', nom)

nom = input('votre nom ?')  # on peut lire facilement une valeur du clavier avec input
print('Hello, ', nom)       # et afficher la valeur d'une variable avec print

a = 15
print (a)
print (type(a))  #on voit ici q "a" est "class: int", donc un entier

a = 'Hello '
print (a)
print (type(a)) #mais ici on le voit "class: str", a est désormais une string

b = 'World '
print (a + b)   #en tant que string, le "+" fait une concatenation 
print (a * 2)   #en tant que string, le "*" répète n-fois la string

b = 2
a = 15  #on remet une valeur int dans la variable "a"
print ( a + b ) #en tant que int, le "+" et le "*" correspondent
print ( a * b ) #aux opérateurs mathématique (adition et multiplication)