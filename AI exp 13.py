import random

def objective_function(x):
    # Replace this function with your own objective function to be optimized
    return -(x ** 2)

def hill_climbing(initial_solution, step_size, max_iterations):
    current_solution = initial_solution
    current_value = objective_function(current_solution)

    for _ in range(max_iterations):
        # Generate a neighboring solution
        neighbor_solution = current_solution + random.uniform(-step_size, step_size)
        neighbor_value = objective_function(neighbor_solution)

        # Move to the neighbor if it's better
        if neighbor_value > current_value:
            current_solution = neighbor_solution
            current_value = neighbor_value

    return current_solution, current_value

if __name__ == "__main__":
    # Set the initial parameters
    initial_solution = random.uniform(-10, 10)
    step_size = 0.1
    max_iterations = 100

    # Run the hill climbing algorithm
    final_solution, final_value = hill_climbing(initial_solution, step_size, max_iterations)

    # Print the results
    print("Optimal Solution:", final_solution)
    print("Optimal Value:", final_value)
