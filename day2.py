from io import TextIOWrapper
from itertools import pairwise
from typing import List, Literal


def _is_report_safe(report: List[int]) -> bool:
    # Assume ascending to start
    order: Literal["ASC", "DESC"] = "ASC"

    for i, level_pair in enumerate(pairwise(report)):
        # Test difference
        difference = abs(level_pair[0] - level_pair[1])
        if difference > 3 or difference < 1:
            return False

        # First pair might update order
        if i == 0:
            if level_pair[0] > level_pair[1]:
                order = "DESC"

        # Check order
        if order == "ASC" and level_pair[0] > level_pair[1]:
            return False
        if order == "DESC" and level_pair[0] < level_pair[1]:
            return False

    return True



def part1(input: TextIOWrapper):
    safe_reports: int = 0
    
    for report in input.readlines():
        report = report.strip()
        report = [int(level) for level in report.split(" ")]
        if _is_report_safe(report):
            safe_reports = safe_reports + 1

    print(f"{safe_reports=}")



def part2(input: TextIOWrapper):
    pass