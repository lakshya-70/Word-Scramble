# 38th github project --> Word Scramble
print('---------Word Scramble----------')
import random


WORDS = ["python", "guitar", "planet", "chocolate", "butterfly",
         "volcano", "library", "elephant", "diamond", "pizza"]


def scramble(word):
    letters = list(word)
    while True:
        random.shuffle(letters)
        scrambled = "".join(letters)
        if scrambled != word:
            return scrambled


def main():
    print("WORD SCRAMBLE")
    score = 0

    while True:
        word = random.choice(WORDS)
        scrambled = scramble(word)

        print(f"\nScrambled: {scrambled}")
        guess = input("Your guess: ").strip().lower()

        if guess == word:
            score += 1
            print(f"Correct! Score: {score}")
        else:
            print(f"Wrong. The word was '{word}'.")

        again = input("Play again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print(f"Final score: {score}")
            break



main()