# [START program]
"""Simple solve."""
import itertools
from typing import Union

# [START import]
from ortools.sat.python import cp_model

# [END import]
def solve(sudoku_str: str) -> Union[str, None]:
    """Minimal CP-SAT example to showcase calling the solver."""

    # Creates the model.
    # [START model]
    a = 1
    model = cp_model.CpModel()

    # [END model]
    # Creates the variables.
    # [START variables]

    x_model = {}
    jls_extract_var = "x_%i_%i_%i"
    for i, j, l_iter in itertools.product(range(9), range(9), range(1, 10)):
        x_model[(i, j, l_iter)] = model.NewIntVar(
            0, 1, jls_extract_var % (i, j, l_iter)
        )

    # [END variables]
    # Creates the constraints.
    # [START constraints]

    for i, l_iter in itertools.product(range(9), range(1, 10)):
        model.Add(sum(x_model[(i, j, l_iter)] for j in range(9)) == 1)

    for j, l_iter in itertools.product(range(9), range(1, 10)):
        model.Add(sum(x_model[(i, j, l_iter)] for i in range(9)) == 1)

    for i_iter, j_iter, l_iter in itertools.product(range(3), range(3), range(1, 10)):
        model.Add(
            sum(
                x_model[(i + i_iter * 3, j + j_iter * 3, l_iter)]
                for i in range(3)
                for j in range(3)
            )
            == 1
        )

    for i, j in itertools.product(range(9), range(9)):
        model.Add(sum(x_model[(i, j, l)] for l in range(1, 10)) == 1)

    for i, j, l_iter in itertools.product(range(9), range(9), range(1, 10)):
        if l_iter == int(sudoku_str[i * 9 + j]):
            model.Add(x_model[(i, j, l_iter)] == 1)

    # [END constraints]
    # Creates a solver and solves the model.
    # [START solve]

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # [END solve]
    # [START print_solution]

    if status in [cp_model.OPTIMAL, cp_model.FEASIBLE]:
        solution = ""
        for i, j in itertools.product(range(9), range(9)):
            temp_foratting = sum(
                l * solver.Value(x_model[i, j, l]) for l in range(1, 10)
            )
            solution = solution + str(temp_foratting)
        return solution
    return None

    # [END print_solution]


if __name__ == "__main__":

    EXAMPLE = "600837001089004700102000400000450020030609005040000860908006070700098010005100930"
    print(solve(EXAMPLE))

    # 654837291389214756172965483896451327237689145541723869918346572723598614465172938
# [END program]
