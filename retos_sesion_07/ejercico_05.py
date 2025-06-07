#Escribe un programa que reciba una cadena y retorna verdadero o falso 
#si es palindrome sin importar los espacios, mayúsculas o minúsculas

# escribir una palabra o frase
texto = input("Escribe una palabra o frase: ")

# Quitamos espacios 
texto_limpio = texto.replace(" ", "")
# Convertimos todo a minúsculas
texto_limpio  = texto_limpio.lower() 
# Invertimos el texto sin espacios
texto_invertido = texto_limpio[::-1]

# Comparamos y mostramos 
print("la palabra es palindrome? :")
print(texto_limpio == texto_invertido)