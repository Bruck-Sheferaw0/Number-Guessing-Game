import random


class NumGuesser:  # take 2 levels of difficulty, get random number, and check user answer.
    def __init__(self):
        self.number = random.randint(1, 100)

    def difficulty_easy(self):
        lives = 10
        print(f"You have {lives} attempts remaining to guess the number.")
        while lives > 0:
            user_input = int(input("Guess a number: "))
            if user_input == self.number:
                print(f"You win! the number is {self.number}")
                lives = -1
            elif user_input < self.number:
                print("Too Low")
                lives -= 1
                print(f"You have {lives} attempts remaining to guess the number.")
            elif user_input > self.number:
                print("Too High")
                lives -= 1
                print(f"You have {lives} attempts remaining to guess the number.")
            elif lives < 1:
                print(f"You have no more tries. The number was {self.number}. You Lost")
                break

    def difficulty_hard(self):
        lives = 5
        print(f"You have {lives} attempts remaining to guess the number.")
        while lives > 0:
            user_input = int(input("Guess a number: "))
            if user_input == self.number:
                print(f"You win! the number is {self.number}")
                lives = -1
            elif user_input < self.number:
                print("Too Low")
                lives -= 1
                print(f"You have {lives} attempts remaining to guess the number.")
            elif lives < 1:
                print(f"You have no more tries. The number was {self.number}. You Lost")
                break
