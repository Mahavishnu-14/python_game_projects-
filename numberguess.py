import random

mi = 1
ma = 100
att = 10

rand = random.randint(mi, ma)

attempts = 0

print(f"Guess the number {mi} and {ma}. You have {att} attempts.")

while attempts < att:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < mi or guess > ma:
            print(f"Please enter a number between {mi} and {ma}.")
        elif guess < rand:
            print("Too low!")
        elif guess > rand:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if attempts == att and guess != rand:
    print(f"Sorry, you've used all your attempts. The number was {rand}.")

