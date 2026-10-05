"""Neddle: a Wordle-style five-letter guessing game for the terminal."""

from __future__ import annotations

import random

WORD_LENGTH = 5
MAX_ATTEMPTS = 6
WORDS = (
    "apple", "bloom", "brick", "cheer", "crane", "dream", "fresh", "grape",
    "light", "ocean", "plant", "quiet", "slate", "smile", "toast", "train",
)
CORRECT = "correct"
PRESENT = "present"
ABSENT = "absent"
MARKS = {CORRECT: "🟩", PRESENT: "🟨", ABSENT: "⬜"}


def score_guess(guess: str, answer: str) -> list[str]:
    """Score a guess, using Wordle's two-pass rule for repeated letters."""
    guess, answer = guess.lower(), answer.lower()
    if len(guess) != WORD_LENGTH or len(answer) != WORD_LENGTH:
        raise ValueError("Both guess and answer must be five letters long.")
    if not guess.isalpha() or not answer.isalpha():
        raise ValueError("Guess and answer must contain letters only.")

    feedback = [ABSENT] * WORD_LENGTH
    remaining: dict[str, int] = {}

    # Mark exact matches first, then count only answer letters still available.
    for index, letter in enumerate(answer):
        if guess[index] == letter:
            feedback[index] = CORRECT
        else:
            remaining[letter] = remaining.get(letter, 0) + 1

    # Allocate misplaced-letter matches without counting duplicates twice.
    for index, letter in enumerate(guess):
        if feedback[index] == CORRECT:
            continue
        if remaining.get(letter, 0) > 0:
            feedback[index] = PRESENT
            remaining[letter] -= 1

    return feedback


def render_feedback(guess: str, feedback: list[str]) -> str:
    """Render a guess and its feedback as compact colored-square markers."""
    return " ".join(MARKS[mark] for mark in feedback) + f"  {guess.upper()}"


def play_game(answer: str | None = None, input_fn=input, print_fn=print) -> bool:
    """Play one game. Return True for a win and False for a loss."""
    answer = random.choice(WORDS) if answer is None else answer.lower()
    if len(answer) != WORD_LENGTH or not answer.isalpha():
        raise ValueError("The answer must be a five-letter word.")

    print_fn("\n  N E D D L E  /  a five-letter word game")
    print_fn(f"  Guess the word in {MAX_ATTEMPTS} tries. Green = right spot; yellow = elsewhere.")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        while True:
            guess = input_fn(f"\n  Guess {attempt}/{MAX_ATTEMPTS}: ").strip().lower()
            if len(guess) == WORD_LENGTH and guess.isalpha():
                break
            print_fn("  Enter exactly five letters.")

        feedback = score_guess(guess, answer)
        print_fn("  " + render_feedback(guess, feedback))

        if guess == answer:
            print_fn(f"  Nice solve — you found it in {attempt} {'guess' if attempt == 1 else 'guesses'}! ✨")
            return True

    print_fn(f"\n  Out of guesses. The word was {answer.upper()}.")
    return False


def main() -> None:
    """Run games until the player opts out of replaying."""
    print("\n  A small daily-puzzle mood, made for the terminal.\n")
    while True:
        play_game()
        again = input("\n  Play again? [y/n]: ").strip().lower()
        if again not in ("y", "yes"):
            print("\n  Thanks for playing Neddle. Keep noticing the details.\n")
            break


if __name__ == "__main__":
    main()
