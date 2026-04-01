import random


def gcd_game(game_starts: bool) -> tuple[str, int]:
    if game_starts:
        print("Find the greatest common divisor of given numbers.")

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    return f"{num1} {num2}", gcd(num1, num2)
