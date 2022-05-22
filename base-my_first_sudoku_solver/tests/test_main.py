"""Module Test solve Sudoku"""
from my_first_sudoku_solver import solve

collect_ignore = ["setup.py"]


def test_solve_sudoku() -> None:
    """Test sudoku"""
    assert (
        solve(
            "600837001089004700102000400000450020030609005040000860908006070700098010005100930"
        )
        == "654837291389214756172965483896451327237689145541723869918346572723598614465172938"
    )


def test_solve_sudoku_no_result() -> None:
    """Test sudoku no result"""
    assert (
        solve(
            "660837001089004700102000400000450020030609005040000860908006070700098010005100930"
        )
        is None
    )
