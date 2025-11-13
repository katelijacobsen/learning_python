            # 0, 1, 2, 3, 4, 5
toppings = ["Pepperoni", "Skinke", "Ost", "Oliven", "Ananas"]

print(toppings)

#Print et enkelt element ud fra listen
print(toppings[2])

#Ændre et element fra listen
toppings[2] = "Bacon"
print(toppings)

# Printe et sektion ud fra listen (slice)
print("De midterste toppings:   ", toppings[2:5])

# Erstatter elementer i listen f.eks. fra 1 til 3
toppings[1:3] = ["Salat", "Kartofler", "Løg"]
print(toppings)

# Erstatter 2 elementer med 1 element
toppings[1:3] = ["Extra ost"]
print(toppings)

# Fjerne et element
del toppings[0:2]
print(toppings)

# Eksempel på brug at matematisk operator. 
# Måde man kan tilføje elementer til listen
toppings += ["Skine", "Kebab", "Kylling"]
print(toppings)

# Kompakt metode i Python. Printer de 3 første elementer.
print(toppings[:3])

# Anden vej rundt. Printer resten af listen efter de 3 elementer.
print(toppings[3:])

# Printe hver andet element ud fra listen.
print(toppings[::2])

# Ønsker at gennemgå listen og gøre noget specifikt for hver element.
for slags in toppings:
    print("Du kan få " + slags + " på din pizza")


# Egne eksempeler

topping1 = [1,2,3,4,5] * 3
topping2 = [6,7,8,9,10]

print(topping1 + topping2)

print(2 in topping1)
print(2 in topping2)