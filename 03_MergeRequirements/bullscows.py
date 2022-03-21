from textdistance import hamming, sorensen
def bullscows(guess: str, secret: str):
    bulls = hamming.similarity(guess, secret)
    cows = int((hamming(guess, "") + hamming(secret, "")) * sorensen(guess, secret) / 2)
    return bulls, cows


def ask(prompt: str, valid: list[str] = None) -> str:
    print(prompt)
    guess = input()
    if valid == None:
        return guess 
    else:
        return guess if guess in valid else ask(prompt, valid)


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))

def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    import random
    secret = random.choice(words)
    num_of_attempts = 0
    guess = ""
    while (guess != secret):
        num_of_attempts += 1
        guess = ask("Введите слово: ", words)
        bulls, cows  = bullscows(guess, secret)
        inform("Быки: {}, Коровы: {}", bulls, cows)
    return num_of_attempts
