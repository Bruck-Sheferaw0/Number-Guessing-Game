from processor_num import NumGuesser

print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty. 'easy' or 'hard': ").lower()
prompt = NumGuesser()
if difficulty_level == 'easy':
    prompt.difficulty_easy()
else:
    prompt.difficulty_hard()