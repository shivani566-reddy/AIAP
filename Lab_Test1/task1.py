def reverse_list_builtin(lst):
    """Reverse a list using the built-in reverse() method."""
    lst_copy = lst.copy()
    lst_copy.reverse()
    return lst_copy

def reverse_list_slicing(lst):
    """Reverse a list using slicing."""
    return lst[::-1]

def reverse_list_loop(lst):
    """Reverse a list using a manual loop."""
    reversed_lst = []
    for item in lst:
        reversed_lst = [item] + reversed_lst
    return reversed_lst

def reverse_list_recursion(lst):
    """Reverse a list using recursion."""
    if len(lst) == 0:
        return []
    else:
        return [lst[-1]] + reverse_list_recursion(lst[:-1])

# Alternative AI-suggested implementations
def reverse_list_reversed(lst):
    """Reverse a list using the reversed() iterator."""
    return list(reversed(lst))

# Performance testing
import time

def test_performance():
    import random

    test_lists = [
        [1, 2, 3, 4, 5],
        list(range(100)),
        [random.randint(0, 1000) for _ in range(10000)]
    ]

    implementations = [
        ("Built-in reverse()", reverse_list_builtin),
        ("Slicing", reverse_list_slicing),
        ("Loop", reverse_list_loop),
        ("Recursion", reverse_list_recursion),
        ("reversed() function", reverse_list_reversed),
    ]

    for idx, test_lst in enumerate(test_lists):
        print(f"\nTesting on list of length {len(test_lst)}:")
        for name, func in implementations:
            start = time.time()
            # for recursion, skip very large lists to avoid recursion limit
            if name == "Recursion" and len(test_lst) > 1000:
                print(f"{name:20}: Skipped (list too large for recursion)")
                continue
            result = func(test_lst)
            end = time.time()
            print(f"{name:20}: {end - start:.6f} sec")

if __name__ == "__main__":
    test_performance()
    # Example: Reverse a given list and print the result
    given_list = [1, 2, 3, 4, 5]
    reversed_given_list = reverse_list_slicing(given_list)
    print("Reversed list:", reversed_given_list)
