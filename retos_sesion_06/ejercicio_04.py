#La resta de los números 17 y 9 es un número par?
a=17
b=9

diferencia = a-b
resto = diferencia % 2
# Si el resto es 0 → el número es par → par = True
# Si el resto es 1 → el número es impar → par = False
par = (resto == 0)
print("¿La diferencia es par?", par)