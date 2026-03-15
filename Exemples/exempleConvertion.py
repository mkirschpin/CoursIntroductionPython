#exemple des convertions de variables d'un type vers un autre

a = input('a ? ')   #on demande une valeur pour "a" et "b"
b = input('b ? ')

somme = a + b              # input lit des string, a et b contienent des string
print("a+b: ", somme)      # a + b fait donc une contatenation, pas la somme

inta = int(a)            #on convertit a et b de str à int
intb = int(b)

somme = inta + intb
print("a+b: ", somme) 

floata = float(a)        # on peut aussi convertir en float
floatb = float(b)   
somme = floata + floatb
print("a+b: ", somme) 

strsomme = str(somme)
print(type(strsomme))
