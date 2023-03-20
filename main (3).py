'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
import random

def guess_number():
    secret_number = random.randint(1, 100)
    guess = None
    attempts = 0
    
    while guess != secret_number:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low, try again.")
        elif guess > secret_number:
            print("Too high, try again.")
    
    print(f"Congratulations, you guessed the number in {attempts} attempts!")

guess_number()
