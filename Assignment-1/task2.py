# ...existing code...

import math

def is_prime():
    """Ask the user for an integer, print whether it's prime, and return True/False."""
    while True:
        s = input("Enter an integer to check for primality: ").strip()
        try:
            n = int(s)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if n <= 1:
        print(f"{n} is not prime.")
        return False
    if n <= 3:
        print(f"{n} is prime.")
        return True
    if n % 2 == 0:
        print(f"{n} is not prime.")
        return False

    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            print(f"{n} is not prime.")
            return False

    print(f"{n} is prime.")
    return True

if __name__ == "__main__":
    is_prime()

# ...existing code...