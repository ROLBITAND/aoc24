from typing import List

import pytest

from day2 import _is_report_safe


@pytest.mark.parametrize(
        "report",
        [
            # ASC
            [1, 2],                     # just pair
            [1, 2, 3, 4, 5],            # increase by 1
            [1, 3, 5, 7, 9],            # increase by 2
            [1, 4, 7, 10, 13],          # increase by 3
            [1, 3, 5, 6, 9, 12, 13],    # mixed increase
            # DESC
            [2, 1],
            [5, 4, 3, 2, 1],
            [9, 7, 5, 3, 1],
            [13, 10, 7, 4, 1],
            [13, 12, 9, 6, 5, 3, 1],
        ]
)
def test_safe_reports(report: List[int]):
    assert _is_report_safe(report)


@pytest.mark.parametrize(
        "report",
        [
            # ASC
            [1, 2, 2, 4, 5],            # not at least one diff
            [1, 3, 5, 7, 11],           # more than 3
            [1, 4, 7, 6, 13],           # change in order
            [1, 3, 7, 6, 9, 12, 13],    # more than 3 + change in order
            # DESC
            [5, 4, 2, 2, 1],
            [11, 7, 5, 3, 1],
            [13, 6, 7, 4, 1],
            [13, 12, 9, 6, 7, 3, 1],
        ]
)
def test_unsafe_reports(report: List[int]):
    assert not _is_report_safe(report)