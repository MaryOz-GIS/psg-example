#Comparar los números 44 y 98 , 111 y 333 , comprobar si tienen la misma paridad ambos pares o ambos impares
#Paridad en matemáticas y programación significa si un número es par o impar.
#Entonces:
#Dos números tienen la misma paridad si ambos son pares o ambos son impares.
#Tienen distinta paridad si uno es par y el otro es impar.

#primer par
a=44
b=98

modulo_a = a % 2
# Si el resto es 0 → el número es par → par = True
# Si el resto es 1 → el número es impar → par = False
a_es_par = (modulo_a == 0)
print("¿A es par?", a_es_par)

modulo_b = b % 2
# Si el resto es 0 → el número es par → par = True
# Si el resto es 1 → el número es impar → par = False
b_es_par = (modulo_b == 0)
print("¿B es par?", b_es_par)

primera_paridad = (a_es_par and a_es_par)
print("Tienen paridad?",primera_paridad)

#segundo par
c=111
d=333
modulo_c = c % 2
# Si el resto es 0 → el número es par → par = True
# Si el resto es 1 → el número es impar → par = False
c_es_par = (modulo_c == 0)
print("¿C es par?", c_es_par)

modulo_d = d % 2
# Si el resto es 0 → el número es par → par = True
# Si el resto es 1 → el número es impar → par = False
d_es_par = (modulo_d == 0)
print("¿D es par?", d_es_par)

segunda_paridad = (c_es_par and d_es_par)
print("Tienen paridad?",segunda_paridad)