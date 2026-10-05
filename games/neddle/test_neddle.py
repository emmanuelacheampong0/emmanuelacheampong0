"""Tests for Neddle feedback and the playable game loop."""

import unittest

from neddle import ABSENT, CORRECT, PRESENT, play_game, score_guess


class FeedbackTests(unittest.TestCase):
    def test_exact_matches(self):
        self.assertEqual(score_guess("crane", "crane"), [CORRECT] * 5)

    def test_misplaced_and_absent_letters(self):
        self.assertEqual(
            score_guess("stare", "tears"),
            [PRESENT, PRESENT, CORRECT, CORRECT, PRESENT],
        )
        self.assertEqual(
            score_guess("crane", "slate"),
            [ABSENT, ABSENT, CORRECT, ABSENT, CORRECT],
        )

    def test_duplicate_guess_letters_are_not_overcounted(self):
        self.assertEqual(
            score_guess("allee", "apple"),
            [CORRECT, PRESENT, ABSENT, ABSENT, CORRECT],
        )

    def test_invalid_length_or_characters_raise(self):
        with self.assertRaises(ValueError):
            score_guess("four", "apple")
        with self.assertRaises(ValueError):
            score_guess("appl!", "apple")


class GameTests(unittest.TestCase):
    def test_player_can_win(self):
        guesses = iter(("no", "crane"))
        messages = []
        won = play_game("crane", lambda _prompt: next(guesses), messages.append)
        self.assertTrue(won)
        self.assertTrue(any("Enter exactly five letters" in line for line in messages))
        self.assertTrue(any("found it" in line for line in messages))

    def test_player_loses_after_six_guesses(self):
        guesses = iter(("slate",) * 6)
        messages = []
        won = play_game("crane", lambda _prompt: next(guesses), messages.append)
        self.assertFalse(won)
        self.assertTrue(any("CRANE" in line for line in messages))


if __name__ == "__main__":
    unittest.main()
