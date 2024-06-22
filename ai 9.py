import itertools

def calculate_total_distance(path, distances):
    total_distance = 0
    num_cities = len(path)
    for i in range(num_cities):
        total_distance += distances[path[i % num_cities]][path[(i + 1) % num_cities]]
    return total_distance

def tsp_brute_force(distances):
    num_cities = len(distances)
    all_cities = list(range(num_cities))
    min_distance = float('inf')
    best_path = None
    
    for path in itertools.permutations(all_cities):
        current_distance = calculate_total_distance(path, distances)
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = path
    
    return best_path, min_distance

# Example usage:
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

best_path, min_distance = tsp_brute_force(distances)

print("Best Path:", best_path)
print("Minimum Distance:", min_distance)
