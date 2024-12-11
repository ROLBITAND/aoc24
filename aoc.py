import argparse

import day1


IMPLEMENTATIONS = {
    (1, 1): day1.part1,
    (1, 2): day1.part2,
}


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    
    parser.add_argument("day", type=int)
    parser.add_argument("part", type=int)

    return parser.parse_args()


def main(day: int, part: int):
    if part not in [1, 2]:
        raise ValueError("Part can only be 1 or 2.")
    if day < 1 or day > 31:
        raise ValueError("Day can only be between 1 and 31.")

    with open(f"inputs/{day}_{part}.txt", "r") as input_f:
        IMPLEMENTATIONS[(day, part)](input_f)


if __name__ == "__main__":
    args = parse_arguments()
    main(args.day, args.part)