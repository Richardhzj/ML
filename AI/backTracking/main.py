import time

from problem import Problem
from solvers import MinConflictsSolver, RecursiveBacktrackingSolver

regions = ["North Carolina",  # 0
           "South Carolina",  # 1
           "Virginia",  # 2
           "Tennessee",  # 3
           "Kentucky",  # 4
           "West Virginia",  # 5
           "Georgia",  # 6
           "Alabama",  # 7
           "Mississippi",  # 8
           "Florida"]  # 9
borders = [("North Carolina", "South Carolina"),
           ("North Carolina", "Virginia"),
           ("North Carolina", "Tennessee"),
           ("North Carolina", "Georgia"),
           ("South Carolina", "Georgia"),
           ("Virginia", "Tennessee"),
           ("Virginia", "Kentucky"),
           ("Virginia", "West Virginia"),
           ("Tennessee", "Kentucky"),
           ("Tennessee", "Georgia"),
           ("Tennessee", "Alabama"),
           ("Tennessee", "Mississippi"),
           ("Kentucky", "West Virginia"),
           ("Georgia", "Alabama"),
           ("Georgia", "Florida"),
           ("Alabama", "Mississippi"),
           ("Alabama", "Florida")]

colors = ["red", "blue", "green", "yellow"]


def check_border(variables, *args):
    zipped = list(zip(variables, args))
    return zipped[0][1] != zipped[1][1]


def solve_csp(solver):
    problem = Problem(solver)
    problem.add_variables(regions, colors)
    for node in regions:
        borders_per_node = [borders[index] for (index, a_tuple) in enumerate(borders) if a_tuple[0] == node]
        if borders_per_node:
            for border in borders_per_node:
                problem.add_constraint(check_border, list(border))

    start_time = time.time()
    problem.get_solution()
    end_time = (time.time() - start_time)
    print(f"Solution with {solver.get_description()} took {end_time} sec and {solver.counter} checks")
    problem.plot_map(borders)


if __name__ == "__main__":
    solvers = [RecursiveBacktrackingSolver(forwardcheck=False), RecursiveBacktrackingSolver(forwardcheck=True),
               MinConflictsSolver()]
    for solver in solvers:
        solve_csp(solver)
