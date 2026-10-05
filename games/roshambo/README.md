# Roshambo

A complete, replayable terminal version of Rock–Paper–Scissors, built in Python. The project keeps the rules in small reusable functions, chooses the computer throw at random, validates input, and tracks wins, losses, and ties until the player quits.

## Run

```bash
python3 roshambo.py
```

Enter `r`, `p`, or `s` for a throw. Enter `q` to finish and see the final score.

## Test

```bash
python3 -m unittest -v
```

The tests cover every outcome, case normalization, invalid choices, the computer's choice, and the round helper.
