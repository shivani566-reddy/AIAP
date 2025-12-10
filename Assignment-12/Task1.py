def linear_search(lst, target):
    """
    Search for target in lst and return its index.
    Returns -1 if target is not found.
    """
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1


# Example usage
numbers = [10, 25, 30, 45, 50]
x = 30

idx = linear_search(numbers, x)
if idx != -1:
    print(f"Value {x} found at index {idx}")
else:
    print(f"Value {x} not found in the list")