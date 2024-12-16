import random

#Create a function to guess the game
def age_guess():
    print("\n++++++ WELCOME TO THE AGE GUESSING GAME ++++++")
    print("Guess the age of a person between 18 and 25 years")
    print("You have Only 3 guesses, GOODLUCK!!\n")

    #Randomly generate game
    age = random.randint(18,25)

    #Give player 3 attempts
    attempts = 3

    for attempt in range(1, attempts+1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter you age_guess: "))
            if guess < 18 or guess > 25:
                print("Your age_guess is out of the range! Please guess the age between 18 and 25")
                print()
                continue

            if guess == age:
                print(f"Congartulation! You guessed the correct Age: {age}")
                print()
                break
            elif guess < age:
                print("Age guess Too low! Try again.")
                print()
            else:
                print("Age guess Too high! Try again")
                print()
        except ValueError:
            print("Invalid Input! Please enter a number between 18 and 25 years")
            print()
    else:
        print(f"Sorry! you have used all your guesses: The  correct age was {age}")
        print()

#Run the game

if __name__ == "__main__":
    age_guess()




