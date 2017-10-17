import random
random_number = int(input("Enter a number between 1 and 100: "))
for guess_number in random_number:
if guess_number == random_number:
print ("You are right!")
if guess_number <= random_number:
print ("Too low!")
if guess_number >= random_number:
print ("Too high!")





