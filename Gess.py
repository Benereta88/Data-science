import random

def guess_the_number():
    print("Welcome to guess the number! :")
    secret, attempts = random.randint(1, 100), 0

    while(attempts := attempts + 1):
        if(guess := int(input("Enter your Guess(1 - 100):"))) == secret:
            print(f"Congrats! You guess the number {secret} in {attempts}")
            break
        print("Too low, Try again. " if guess < secret else " Too hight, Try again.")

    
if __name__ == "_main_":
    guess_the_number()