# ...existing code...

def is_recursive():
    """Ask the user for a non-negative integer, compute factorial using both
    a recursive and an iterative implementation (both shown below), print the
    results and return the factorial value.

    Recursive implementation:
        def fact_recursive(n):
            if n <= 1:
                return 1
            return n * fact_recursive(n - 1)

    Iterative implementation:
        def fact_iterative(n):
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result
    """
    # Recursive factorial
    def fact_recursive(n):
        if n <= 1:
            return 1
        return n * fact_recursive(n - 1)

    # Iterative factorial
    def fact_iterative(n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    while True:
        s = input("Enter a non-negative integer to compute its factorial: ").strip()
        try:
            n = int(s)
            if n < 0:
                print("Please enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    rec = fact_recursive(n)
    itr = fact_iterative(n)

    print(f"Recursive factorial of {n} is: {rec}")
    print(f"Iterative factorial of {n} is: {itr}")

    if rec != itr:
        print("Warning: recursive and iterative results differ.")
    return rec

if __name__ == "__main__":
    is_recursive()

# ...existing code...