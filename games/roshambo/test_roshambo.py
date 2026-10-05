"""Focused tests for Roshambo game rules and random computer throws."""

import unittest
from unittest.mock import patch

from roshambo import computer_rps, play_round, winner


class WinnerTests(unittest.TestCase):
    def test_all_ties(self):
        for choice in ("r", "p", "s"):
            with self.subTest(choice=choice):
                self.assertEqual(winner(choice, choice), "tie")

    def test_each_winning_pair(self):
        self.assertEqual(winner("r", "s"), "hero")
        self.assertEqual(winner("p", "r"), "hero")
        self.assertEqual(winner("s", "p"), "hero")

    def test_each_losing_pair(self):
        self.assertEqual(winner("s", "r"), "villain")
        self.assertEqual(winner("r", "p"), "villain")
        self.assertEqual(winner("p", "s"), "villain")

    def test_choice_is_case_insensitive(self):
        self.assertEqual(winner("R", "s"), "hero")

    def test_invalid_choice_raises(self):
        with self.assertRaises(ValueError):
            winner("x", "s")

    def test_computer_choice_is_valid(self):
        self.assertIn(computer_rps(), ("r", "p", "s"))

    def test_play_round_accepts_injected_computer_choice(self):
        self.assertEqual(play_round("r", "s"), ("r", "s", "hero"))

    @patch("roshambo.computer_rps", return_value="p")
    def test_play_round_uses_computer(self, _mock):
        self.assertEqual(play_round("r"), ("r", "p", "villain"))


if __name__ == "__main__":
    unittest.main()
