# [START program]
"""Simple solve."""
# [START import]
from ortools.sat.python import cp_model

# [END import]


def SimpleSatProgram(example):
    """Minimal CP-SAT example to showcase calling the solver."""
    # Creates the model.
    # [START model]
    model = cp_model.CpModel()
    # [END model]

    # Creates the variables.
    # [START variables]
    num_vals = 10
    x = {}
    for i in range(9):
        for j in range(9):
            for l in range(1,10):
                x[(i, j, l)] = model.NewIntVar(0, 1, "x_%i_%i_%i" % (i, j, l))

    # [END variables]

    # Creates the constraints.
    # [START constraints]
    for i in range(9):
        for l in range(1, 10):
            model.Add(sum([x[(i, j, l)] for j in range(9)]) == 1)

    for j in range(9):
        for l in range(1, 10):
            model.Add(sum([x[(i, j, l)] for i in range(9)]) == 1)

    for ii in range(3):
        for jj in range(3):
            for l in range(1, 10):
                model.Add(
                    sum([x[(i + ii*3, j + jj*3, l)] for i in range(3) for j in range(3)]) == 1
                )
    
    for i in range(9):
        for j in range(9):
            model.Add(sum([x[(i, j, l)] for l in range(1, 10)]) == 1)

    for i in range(9):
        for j in range(9):
            for l in range(1, 10):
                if l == int(example[i * 9 + j]):
                    model.Add(x[(i, j, l)] == 1)

    # [END constraints]

    # Creates a solver and solves the model.
    # [START solve]
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    # [END solve]

    # [START print_solution]
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print("Solution :")
        s = ""
        for i in range(9):
            for j in range(9):
                a = 0
                for l in range(1, 10):
                    a+=l*solver.Value(x[i, j, l])
                s = s + str(a)
        print(s)
    else:
        print("No solution found.")
    # [END print_solution]


if __name__ == "__main__":
    example = "600837001089004700102000400000450020030609005040000860908006070700098010005100930"
    SimpleSatProgram(example)

     # 654837291389214756172965483896451327237689145541723869918346572723598614465172938
# [END program]
