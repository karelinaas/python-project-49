import random


def calc_game(game_starts: bool) -> tuple[str, int | None]:
    if game_starts:
        print("What is the result of the expression?")

    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)
    operation_symbol = random.choice(["+", "-", "*"])

    result = None
    match operation_symbol:
        case "+":
            result = number1 + number2
        case "-":
            result = number1 - number2
        case "*":
            result = number1 * number2
    
    return f"{number1} {operation_symbol} {number2}", result
