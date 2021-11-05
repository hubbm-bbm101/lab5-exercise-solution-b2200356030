# guessing game
import random

guessed_number = random.randint( 0 , 10)

number = int(input("guess the random number: "))

while number != guessed_number:
    
    if number > guessed_number:
        print("decrease your number")
        number = int(input("guess the new number: "))
    
    elif guessed_number > number:
        print("increase your number")
        number = int(input("guess the new number: "))
else:
    print("you found the random number") 
    
