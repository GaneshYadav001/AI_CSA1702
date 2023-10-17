class MapColoringCSP:
    def __init__(self, variables, domains, neighbors):
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
    def is_consistent(self, variable, color, assignment):
        for neighbor in self.neighbors[variable]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True
    def backtracking_search(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment  # All variables are assigned
        unassigned_variable = [var for var in self.variables if var not in assignment][0]
        for color in self.domains[unassigned_variable]:
            if self.is_consistent(unassigned_variable, color, assignment):
                assignment[unassigned_variable] = color
                result = self.backtracking_search(assignment)
                if result:
                    return result
                del assignment[unassigned_variable]  # Remove the assignment if it doesn't lead to a solution
        return None
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V']
domains = {var: ['Red', 'Green', 'Blue'] for var in variables}
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW']
}
csp = MapColoringCSP(variables, domains, neighbors)
assignment = csp.backtracking_search({})
if assignment:
    print("Solution found:")
    print(assignment)
else:
    print("No solution exists.")
