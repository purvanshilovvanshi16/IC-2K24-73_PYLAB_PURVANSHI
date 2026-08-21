import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

max_attempts = 7
attempts = 0

print("Guess the Number Game!")
print("I have chosen a number between 1 and 100.")
print("You have 7 attempts to guess it.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")

    elif guess > number:
        print("Too high! Try again.")

    else:
        print("Correct! 🎉")
        print("You guessed the number in", attempts, "attempt(s).")
        break

else:
    print("\nSorry! You have used all 7 attempts.")
    print("The correct number was:", number)