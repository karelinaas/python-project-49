import random


def prime_game(game_starts: bool) -> tuple[str, str]:
    if game_starts:
        print('Answer "yes" if given number is prime. Otherwise answer "no".')

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    number = random.randint(1, 100)
    correct_answer = "yes" if is_prime(number) else "no"
    
    return str(number), correct_answer
