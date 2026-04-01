import random


def even_game(game_starts: bool) -> tuple[str, str]:
    if game_starts:
        print('Answer "yes" if the number is even, otherwise answer "no".')

    number = random.randint(1, 100)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return str(number), correct_answer
