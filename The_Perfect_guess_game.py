import random

def greet_user():
    name=input("Please enter your name: ")
    print(f"Hello!{name}👋 Welcome to the Perfect Guess Game.🤔❓")
    print("In this game, you will try to guess a number that I have selected.")
    print("Let's see how many attempts it takes you to guess the correct number!")
    print("Good luck!\n")

def perfect_guess_game():
    
    #Different levels of difficulty
    print("Choose a difficulty level:")
    print("1. Easy😄: The number is chosen b/w 1 to 50")
    print("2. Medium😁: The number is chosen b/w 1 to 100")
    print("3. Hard😏: The number is chosen b/w 1 to 500")
    difficulty = input("Enter the number corresponding to your choice (1, 2, or 3): ")
    if difficulty == '1':
        # random number b/w 1 to 50
        secret_number = random.randint(1, 50)
    elif difficulty == '2':
        #random number b/w 1 to 100
        secret_number = random.randint(1, 100)      
    elif difficulty == '3':
        # random number b/w 1 to 500
        secret_number = random.randint(1, 500)
    else:
        print("Invalid choice. Please restart the game and choose a valid difficulty level.")
        return 
    
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            diff = abs(secret_number - guess)
            if diff <= 5:
                print("🔥 Super close!")
            elif diff <= 10:
                print("🌡️ Getting warmer.")
            else:
                print("❄️ Cold guess.")


            if guess < secret_number:
                print("High! Please.🥵")
            elif guess > secret_number:
                print("Low! Please.🥶")
            else:
                print(f"Congratulations!🤩🥳🎉 You've guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

def play_again():
    while True:
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again == 'yes':
            perfect_guess_game()
        elif play_again == 'no':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

#start the game
greet_user()    
perfect_guess_game()
play_again()            

