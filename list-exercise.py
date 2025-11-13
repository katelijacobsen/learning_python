# Opave 1
# Lav et program som udskriver de 10 største byer i rækkefølge
cities = [ "København", "Aarhus", "Odense", "Aalborg", "Esbjerg", "Randers", "Horsens", "Kolding", "Vejle", "Roskilde"]
print(cities)

#Opave 2
# Lav et program, som udskriver de 5 største byer
print(cities[:5])

#Opave 3
# Lav et program, som udskriver de sidste 5 byer på listen
print(cities[5:])

#Opave 4
# Lav et program, som udskriver hver tredje by på listen
print(cities[::3])

#Opave 5
# Lav et program, som udskriver hver by på listen og dens position.
position = 1

for city in cities:
    print(f"{position}. {city}")
    position += 1

#Opave 6
# Erstat København med Hovedstadsområdet
cities[0] = "Hovedstadsområdet"
print(cities)

#Opave 7
#Fjern Randers fra listen
del cities[5]
print(cities)

#Opave 8
# Tilføj Herning og Silkeborg til listen

cities += ["Herning", "Silkeborg"]

print(cities)
