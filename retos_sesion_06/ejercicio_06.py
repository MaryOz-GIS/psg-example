#¿El cubo de 300 se encuentra en el siguiente rango? [N > 0 & N < 27_000_000] = rango 1 a 27000000
numero = 300
cubo = numero ** 3
print("el cubo del numero es:",cubo)

en_rango = (cubo >0 and cubo < 27000000)
print ("el cubo del numero esta en el rango?", en_rango)