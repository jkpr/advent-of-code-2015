# Advent of Code 2015

These are my solutions to Advent of Code 2015. The solutions are in the `__init__.py` files for each day's package. Sometimes, there is an `alternate` subpackage that has an alternate solution in its own `__init__.py`.

Try the problems yourself at [https://adventofcode.com/2015/](https://adventofcode.com/2015/).

Feel free to create a Github issue if you want to discuss anything!

# Usage

1. Clone this repo: `git clone https://github.com/jkpr/advent-of-code-2015`
2. Change into the new directory: `cd advent-of-code-2015`
3. Run `make env` to build the environment.
4. Activate the environment with `source env/bin/activate`
5. Run a CLI for day `N`'s code with `python3 -m aoc2015.dayN`, e.g. `python3 -m aoc2015.day1`.

The CLI is common for each day. The main patterns for options are:

- `-t` to run part 1 with `test_input.txt`
- `-2` to run part 2
- `-t -2` to run part 2 with `test_input.txt`
- `-t 1` to run part 1 with `test_input1.txt`
- `-t 1 -2` to run part 2 with `test_input1.txt`

# Helpful imports and documentation

- [collections](https://docs.python.org/3/library/collections.html)
- [itertools](https://docs.python.org/3/library/itertools.html)
