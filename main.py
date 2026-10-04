# Number Guessing Game
import random
while True:
    print("==========NUMBER GUESSING GAME==========")
    print("Choose Your Difficulty ")
    print("1. Easy  (1,100)")
    print("2. Medium  (1,500)")
    print("3. Hard  (1,1000)")


    choice=int(input("Enter Your choice : "))
    if choice==1:
        max_number=100
        Level = "Easy"
        print(f"You choosed {Level} level So guess the number between (1,100)")

    elif choice==2:
        max_number=500
        Level = "Medium"
        print(f"You choosed {Level} level So guess the number between (1,500)")

    elif choice==3:
        max_number=1000
        Level = "Hard"
        print(f"You choosed {Level} level So guess the number between (1,1000)")

    else:
        print("Invalid choice !! ")
        exit()

    number = random.randint(1,max_number)

    maximum_attempts=10
    attempts=0

    while True:
        remaining_attempt=maximum_attempts-attempts
        print(f"{remaining_attempt} attempts left !! ")
        guess = int(input("Enter your guess : "))
        attempts+=1

        if guess==number:
            print("Condratulation !! You Won the Game .")
            print(f"You guessed the number in {attempts} attempt ")
            break
        elif guess > number:
            print("Too Big ")

        else:
            print("Too Small ")

        if attempts==maximum_attempts:
            print("Game Over ")
            print(f"The number was {number}")
            break

    play_again = input("\n Do you want to play again : ").lower()

    if play_again!="yes":
        print("Thanks! for playing !! ")
        break



