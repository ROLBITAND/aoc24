from io import TextIOWrapper
import re


def part1(input: TextIOWrapper):
    program = input.read()

    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")

    multi: int = 0
    for match in mul_pattern.finditer(program):
        multi = multi + (int(match.group(1)) * int(match.group(2)))

    print(f"{multi=}")


def part2(input: TextIOWrapper):
    pass
