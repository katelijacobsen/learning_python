# For Loop
# This type of loop decides how many times it should repeat.
# By adding a variant and using a function called range(), we can decide
# how many times it repeats.

for i in range(5):
    print(i)
print('this line is not looping')


for i in range(5):
    print(i)
    print('this line is looping')

# While Loop (+ if statement)
# A while loop is like keep on doing a task until it is done.
# Compare it when watering plants: you're watering until you have no water left
password = ""

while password != "chicken":
    password = input("Enter password:   ")
    if password != "chicken":
        print("wrong")
print("Login successful")