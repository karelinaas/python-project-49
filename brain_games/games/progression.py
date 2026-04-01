import random


def progression_game(game_starts: bool) -> tuple[str, str]:
    if game_starts:
        print("What number is missing in the progression?")
    
    length = random.randint(5, 10)
    start = random.randint(1, 50)
    step = random.randint(1, 10)

    def generate_progression(start: int, step: int, length: int) -> list[int]:
        return [start + i * step for i in range(length)]
    
    progression: list[int | str] = generate_progression(start, step, length)
    
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    
    progression[hidden_index] = ".."
    
    return " ".join(str(num) for num in progression), str(correct_answer)
