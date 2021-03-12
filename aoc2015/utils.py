import argparse
import functools
from pathlib import Path
import timeit
from typing import Callable, List


def read_lines(input_file: Path) -> List[str]:
    """Read lines from the input file as string."""
    with open(input_file) as f:
        return f.read().splitlines()


def lines_to_int(func):
    """A decorator to change input from string to int."""

    @functools.wraps(func)
    def wrapper(lines):
        int_lines = [int(line) for line in lines]
        return func(int_lines)

    return wrapper


def get_input_file(
    puzzle_data: str = None, module_path: str = None, test_input: str = None
) -> Path:
    """Get the puzzle input file."""
    if puzzle_data:
        return Path(puzzle_data)
    source = "input.txt" if test_input is None else f"test_input{test_input}.txt"
    if module_path:
        return Path(module_path).parent.joinpath(source)
    return Path(source)


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Advent of Code parser")
    parser.add_argument(
        "-i",
        "--puzzle_data",
        help="Puzzle input file. Uses 'input.txt' if nothing is supplied here or for test_input.",
    )
    parser.add_argument(
        "-2", "--second_part", help="Run the second part.", action="store_true"
    )
    parser.add_argument(
        "-t",
        "--test_input",
        metavar="N",
        nargs="?",
        const="",
        help="Use the file 'test_inputN.txt' as the puzzle input file. Note: N can be blank.",
    )
    args = parser.parse_args()
    return args


def main(
    module_path: str,
    part1: Callable,
    part2: Callable,
):
    """
    Run the common main method.

    Args:
        module_path: __file__ from the calling module. This helps find the input text file.
        part1: A callable taking a list (lines of the input file)
        part2: A callable taking a list (lines of the input file)
    """
    args = cli()
    source = get_input_file(
        puzzle_data=args.puzzle_data,
        module_path=module_path,
        test_input=args.test_input,
    )
    start = timeit.default_timer()
    lines = read_lines(source)
    if not args.second_part:
        result = part1(lines)
    else:
        result = part2(lines)
    end = timeit.default_timer()
    print(f"Elapsed time: {end-start:,.4f} seconds")
    print("Returned result:", result)
