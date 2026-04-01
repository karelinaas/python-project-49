import random


def even_game(game_starts: bool) -> tuple[int, str]:
    if game_starts:
        print('Answer "yes" if the number is even, otherwise answer "no".')

    number = random.randint(1, 100)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return number, correct_answer
