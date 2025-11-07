name = input('Hvad er dit navn?     ')

if name == "John":
    print('Kæft det grimt...')
else:
    print("Ejjj det et pændt navn")

tal = int(input('Indtast et tal:    '))

if (tal >= 100): 
    print("Nøj, et stort tal du fandt der")
elif tal < 20:
    print('Godt nok et lille tal')
elif 20 < tal and tal < 80:
    print('mellemstort tal')
else:
    print('hvAbehar')