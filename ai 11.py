class MapColoring:
    def __init__(self, variables, domains, constraints):
        self.variables = variables  # List of variable names (regions)
        self.domains = domains  # Dictionary mapping variables to their possible colors
        self.constraints = constraints  # List of constraints (pairs of adjacent regions)

    def is_valid(self, variable, assignment, neighbor, neighbor_color):
        # Check if neighbor has the same color as assigned to it
        return assignment.get(neighbor) != neighbor_color

    def backtracking_search(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment  # Solution found

        unassigned = [var for var in self.variables if var not in assignment]
        current_var = unassigned[0]  # Choose an unassigned variable

        for color in self.domains[current_var]:
            if all(self.is_valid(current_var, assignment, neighbor, color) for neighbor in self.constraints[current_var]):
                assignment[current_var] = color
                result = self.backtracking_search(assignment)
                if result is not None:
                    return result
                del assignment[current_var]

        return None  # No solution found

# Example usage:
if __name__ == '__main__':
    # Example map coloring problem
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    domains = {
        'WA': ['red', 'green', 'blue'],
        'NT': ['red', 'green', 'blue'],
        'SA': ['red', 'green', 'blue'],
        'Q': ['red', 'green', 'blue'],
        'NSW': ['red', 'green', 'blue'],
        'V': ['red', 'green', 'blue'],
        'T': ['red', 'green', 'blue']
    }
    constraints = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['SA', 'Q', 'V'],
        'V': ['SA', 'NSW', 'T'],
        'T': ['V']
    }

    map_coloring_problem = MapColoring(variables, domains, constraints)
    solution = map_coloring_problem.backtracking_search()

    if solution:
        print("Solution found:")
        for var in variables:
            print(f"{var}: {solution[var]}")
    else:
        print("No solution found")
