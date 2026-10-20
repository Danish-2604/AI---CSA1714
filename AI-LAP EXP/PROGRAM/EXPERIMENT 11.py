
regions = ["A", "B", "C", "D"]
colors = ["Red", "Green", "Blue"]

neighbors = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

assignment = {}

def is_valid(region, color):
    for neighbor in neighbors[region]:
        if assignment.get(neighbor) == color:
            return False
    return True

def solve(index=0):
    if index == len(regions):
        return True

    region = regions[index]
    for color in colors:
        if is_valid(region, color):
            assignment[region] = color
            if solve(index + 1):
                return True
            del assignment[region]
    return False

if solve():
    print("Map Coloring Solution:")
    for region, color in assignment.items():
        print(region, ":", color)
else:
    print("No solution found")
