# Escribe un programa en Python que convierta 1000000 de segundos en semanas, días, horas, minutos y segundos

total_segundossegundos= 1000000

# Total de segundos a convertir
total_segundos = 1_000_000

# Constantes de conversión
segundos_por_minuto = 60
segundos_por_hora = 60 * 60
segundos_por_dia = 24 * segundos_por_hora
segundos_por_semana = 7 * segundos_por_dia

# Cálculo de semanas
semanas = total_segundos // segundos_por_semana
resto = total_segundos % segundos_por_semana

# Cálculo de días
dias = resto // segundos_por_dia
resto %= segundos_por_dia

# Cálculo de horas
horas = resto // segundos_por_hora
resto %= segundos_por_hora

# Cálculo de minutos
minutos = resto // segundos_por_minuto
segundos = resto % segundos_por_minuto

# Mostrar resultados
print(f"{total_segundos} segundos son:")
print(f"{semanas} semanas")
print(f"{dias} días")
print(f"{horas} horas")
print(f"{minutos} minutos")
print(f"{segundos} segundos")
