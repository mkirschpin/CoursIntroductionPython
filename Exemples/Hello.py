val = input ('entrer un n° : ')
print (val)
print ( type (val) )

nb = float(val)

reste = nb % 2
print (reste)

if reste == 0 :
  print (nb , ' est pair')

print ('bonne journée')