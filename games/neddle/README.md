# Neddle

A complete terminal word-guessing game inspired by Wordle. Find the hidden five-letter word in six attempts. Green squares mark letters in the right place; yellow squares mark letters that belong elsewhere. Repeated letters are scored with a two-pass algorithm so the feedback does not overcount them.

The game currently accepts any five alphabetic characters as a guess; it does not require an external dictionary or package.

## Run

```bash
python3 neddle.py
```

## Test

```bash
python3 -m unittest -v
```

The tests cover exact, misplaced, absent, and repeated-letter feedback, input validation, winning, and exhausting all six attempts.
