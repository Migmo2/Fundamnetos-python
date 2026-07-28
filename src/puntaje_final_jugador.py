# Programa para calcular puntaje final de un jugador

nombre = input("Ingrese el nombre del jugador: ")

goles = int(input("Ingrese cantidad de goles: "))
asistencias = int(input("Ingrese cantidad de asistencias: "))
tarjetas = int(input("Ingrese cantidad de tarjetas amarillas: "))

puntaje_final = (goles * 5) + (asistencias * 3) - tarjetas

print("\n----- RESULTADO -----")
print("Jugador:", nombre)
print("Goles:", goles)
print("Asistencias:", asistencias)
print("Tarjetas:", tarjetas)
print("Puntaje final:", puntaje_final)
