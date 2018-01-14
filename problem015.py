from math import factorial

def possiblePaths(down, right):
    """Finds the number of paths for going down and right some number of times."""
    return factorial(down+right)//factorial(down)//factorial(right)

print(possiblePaths(20,20)) # 137846528820
