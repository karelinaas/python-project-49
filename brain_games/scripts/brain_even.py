import random

from prompt import string


def is_even(number):
    return number % 2 == 0


def brain_even():
    print("Welcome to the Brain Games!")
    name = string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    correct_answers = 0
    rounds_to_win = 3
    
    while correct_answers < rounds_to_win:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        
        correct_answer = "yes" if is_even(number) else "no"
        user_answer = string("Your answer: ").lower()
        
        if user_answer == correct_answer:
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


def main():
    brain_even()


if __name__ == "__main__":
    main()
