import random


def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = None

    print("I have generated a random number between 1 and 100. Can you guess what it is?")

    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")

    print(f"Congratulations! You've guessed the number correctly. It took you {attempts} attempts.")


if __name__ == "__main__":
    guess_the_number()