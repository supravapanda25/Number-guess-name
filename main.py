from random import randint
EASY_LEVEL_TURNS = 12
MEDIUM_LEVEL_TURNS = 7
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"CONGRATULATIONS!! The answer was {answer}.")

def difficulty_level():
  level = input("Level of your game?You will get your turns likewise Type 'easy' or 'medium' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  elif level == "medium":
    return MEDIUM_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def Number_guessing_game():
  print("Number Guessing Game!")
  print("I have thought of a number between 1 and 100, try to guess it.")
  answer = randint(1, 100)

  turns = difficulty_level()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining.")

    guess = int(input("Make a guess: "))

    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("No more turns left, You lose.")
      return
    elif guess != answer:
      print("Try to Guess again.")


Number_guessing_game()
