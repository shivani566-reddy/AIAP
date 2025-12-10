def sum_to_n(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    return n * (n + 1) // 2
n = int(input("Enter n to sum 1..n: ").strip())
print(sum_to_n(n))