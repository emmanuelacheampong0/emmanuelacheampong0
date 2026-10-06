# Games Lab

Two beginner-friendly games, built in both Python and the browser.

## Play

- [Roshambo browser edition](roshambo/index.html)
- [Neddle browser edition](neddle/index.html)
- [Games gallery](index.html)

The browser pages are self-contained and use no packages or external images. To play locally, download the repository and open `games/index.html` in a browser.

## Development note

These portfolio editions were prepared with AI coding assistance from Emmanuel’s course-project descriptions. They are learning prototypes; review the code and compare it with the original assignment before presenting or submitting it as independent work.

## Run the Python versions

```bash
python3 games/roshambo/roshambo.py
python3 games/neddle/neddle.py
```

## Run all Python tests

```bash
python3 -m unittest discover -s games/roshambo -p 'test_*.py'
python3 -m unittest discover -s games/neddle -p 'test_*.py'
```

The Python versions require Python 3.10 or newer and no third-party packages.
# Play the games

The browser versions are published with the profile site:

- [Play Roshambo](https://emmanuelacheampong0.github.io/emmanuelacheampong0/games/roshambo/)
- [Play Neddle](https://emmanuelacheampong0.github.io/emmanuelacheampong0/games/neddle/)

Each folder also includes the Python source, tests, and instructions to run locally.
