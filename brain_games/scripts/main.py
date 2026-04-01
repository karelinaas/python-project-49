import importlib

from prompt import string

from brain_games.scripts.cli import get_game_name, welcome_user


def main():
    if not (game := get_game_name()):
        print("Wrong command configuration!")
        return

    name = welcome_user()
    module = importlib.import_module("brain_games.games")
    game_func = getattr(module, f"{game}_game")

    correct_answers = 0

    while correct_answers < 3:
        question, correct_answer = game_func(correct_answers == 0)
        if correct_answer is None:
            return

        print(f"Question: {question}")
        user_answer = string("Your answer: ")

        if user_answer.lower() == str(correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
