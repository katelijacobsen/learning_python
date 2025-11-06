# We just got home from a fun trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:
# 🇨🇴 Colombian pesos
# 🇵🇪 Peruvian soles
# 🇧🇷 Brazilian reais
# Create a currency.py program that asks the user for the amount they have in 
# pesos, soles, and reais and calculates the total in USD.

pesos = int(input("What do you have left in pesos?"))
soles = int(input("What do you have left in soles?"))
reais = int(input("What do you have left in reais?"))

total = pesos * 0.00025 + soles * 0.28 + reais * 0.21

print("Your total is: ", total)