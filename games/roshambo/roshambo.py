"""A small, replayable Rock–Paper–Scissors game for the terminal."""

from __future__ import annotations

import random

CHOICES = ("r", "p", "s")
NAMES = {"r": "Rock", "p": "Paper", "s": "Scissors"}
BEATS = {"r": "s", "p": "r", "s": "p"}


def winner(hero: str, villain: str) -> str:
    """Return 'hero', 'villain', or 'tie' for two valid R/P/S choices."""
    hero, villain = hero.lower(), villain.lower()
    if hero not in CHOICES or villain not in CHOICES:
        raise ValueError("Choices must be 'r', 'p', or 's'.")
    if hero == villain:
        return "tie"
    return "hero" if BEATS[hero] == villain else "villain"


def computer_rps() -> str:
    """Choose a random rock, paper, or scissors throw."""
    return random.choice(CHOICES)


def play_round(hero: str, villain: str | None = None) -> tuple[str, str, str]:
    """Resolve one round and return (player throw, computer throw, result)."""
    hero = hero.lower()
    villain = computer_rps() if villain is None else villain.lower()
    return hero, villain, winner(hero, villain)


def main() -> None:
    """Play repeated rounds until the player quits."""
    score = {"hero": 0, "villain": 0, "tie": 0}
    print("\n  ROSHAMBO  /  Rock · Paper · Scissors")
    print("  Choose r, p, or s. Type q whenever you want to leave.\n")

    while True:
        raw = input("  Your throw [r/p/s/q]: ").strip().lower()
        if raw in ("q", "quit", "exit"):
            break
        if raw not in CHOICES:
            print("  Please enter r, p, s, or q.\n")
            continue

        hero, villain, result = play_round(raw)
        score[result] += 1
        outcome = {"hero": "You win this round!", "villain": "Computer wins this round.", "tie": "It’s a tie."}[result]
        print(f"  You: {NAMES[hero]}   ·   Computer: {NAMES[villain]}")
        print(f"  {outcome}  Score: {score['hero']}–{score['villain']}  (ties {score['tie']})\n")

    print(f"\n  Final score: {score['hero']}–{score['villain']}  ·  {score['tie']} ties")
    print("  Thanks for playing.\n")


if __name__ == "__main__":
    main()
