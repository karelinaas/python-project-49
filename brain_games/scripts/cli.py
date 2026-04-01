import argparse
import sys

from prompt import string


def welcome_user() -> str:
    print("Welcome to the Brain Games!")
    name = string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def get_game_name() -> str:
    if len(sys.argv) == 1:
        game = sys.argv[0].split("/")[-1].replace("brain-", "")
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument("--game", help="Название игры")
        args = parser.parse_args()
        game = args.game
    return game
