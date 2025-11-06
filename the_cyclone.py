

height = int(input('What is your height fella?:     '))
credits = int(input('How many credits do you have left?:    '))

if height >= 137 and credits >= 10:
    print('Enjoy the ride!! :D')
elif height < 137 and credits >= 10:
    print('You are too short :(')
elif height >= 137 and credits < 10:
    print('You are too short on credits :(')
else:
    print('You do not have met either the requirements') 
