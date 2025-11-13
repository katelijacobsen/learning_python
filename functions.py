# Opgave 1
# Lav en funktion, der finder det største af to tal og returnerer det. 
def big_number(no_1, no_2):
    if no_1 > no_2:
        return no_1
    else:
        return no_2
    
number_1 = 5
number_2 = 10 
print('%d og %d det største er %d' % (number_1, number_2, big_number(number_1, number_2)))

# Opgave 2 
# Lav en funktion, der udskriver teksten "Hej" foran et navn, der gives
# som parameter til funktionen.

def greetings(name):
    print("Hej" + name)

introducing = " Jakob"

greetings(introducing)

# Opgave 3
# Lav en funktion, som udskriver hver andet bogstav i en tekst
# Tip: Udnyt at en streng i virkeligheden er en liste af bogstaver.
def each_second_string():
    print(letter[::2])

letter = ["a", "b", "c", "d", "e", "f", "g", "h"]
each_second_string()