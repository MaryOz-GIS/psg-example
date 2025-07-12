# crea un diccionario con la siguiente tupla de especies animales
animales = {('canino', '🐶') , ('felino','🐱') , ('aves',['🐦','🦅'])}
print("diccionario de animales:")
print(animales)

# del diccionario obtén y elimina el valor de la clave 'aves'
del animales['aves']
print("diccionario de animales modificado:")
print(animales)

# modifica el valor de la clave 'felino' por '🐈'

print ("diccionario: ")
print(animales)
animales['felino'] = '🐈'
print ("nuevo diccionario: ")
print(animales)


# cambia la clave canino por caninos y su valor por ['🐶','🐕']
print ("Modificar la clave canino por caninos")
print(animales)
animales['caninos'] = animales['canino']
del animales['canino']
print(animales)

animales['caninos'] =  ['🐶','🐕']
print("modificando valores de caninos")
print("animales")