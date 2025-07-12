#Crea un diccionario de alimentos y que animales domésticos lo consumen
alimentos_animal = {"carne" : ["gato", "perro"], "zanahoria" : ["conejo"] }

#Añade al diccionario 4 alimentos más, usando update(clave=valor)
alimentos_animal.update({"maiz":"gallina", "zanahoria":"conejo","afrecho":["conejo","chancho"],"choclo":["conejo","cuy"]})
print(alimentos_animal)

#Existe en el diccionario de alimentos la comida 'trigo'?
valor_trigo = alimentos_animal["trigo"]
print("Valor de trigo':", valor_trigo)

#Elimina la comida 'zanahoria' del diccionario de alimentos
zanahoria = alimentos_animal.pop('zanahoria')
print(zanahoria ,type(zanahoria))
print(dalimentos_animal)