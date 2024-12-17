from day4 import _get_diagonals, _get_other_diagonals


def test_get_diagonals():
    input = "ABCDEF" "GHIJKL" "MNOPQR" "STUVWX" "YZ1234" "567890"

    expected = [
        "A",
        "GB",
        "MHC",
        "SNID",
        "YTOJE",
        "5ZUPKF",
        "61VQL",
        "72WR",
        "83X",
        "94",
        "0",
    ]

    assert _get_diagonals(input, 6) == expected


def test_get_other_diagonals():
    input = "ABCDEF" "GHIJKL" "MNOPQR" "STUVWX" "YZ1234" "567890"

    expected = [
        "F",
        "EL",
        "DKR",
        "CJQX",
        "BIPW4",
        "AHOV30",
        "GNU29",
        "MT18",
        "SZ7",
        "Y6",
        "5",
    ]

    assert _get_other_diagonals(input, 6) == expected
