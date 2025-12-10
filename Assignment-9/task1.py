def sum_even_odd(numbers: list[int]) -> tuple[int, int]:
   
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list of integers")
    even_sum = 0
    odd_sum = 0
    for n in numbers:
        if not isinstance(n, int):
            raise TypeError("all elements in numbers must be integers")
        if n % 2 == 0:
            even_sum += n
        else:
            odd_sum += n
    return even_sum, odd_sum


# --- AI-assisted generated docstring (simulated output from an AI tool) ---
ai_docstring = """Summarize even and odd numbers in a list.

Args:
    numbers: list of integers

Returns:
    (even_sum, odd_sum) where even_sum is the total of even numbers and odd_sum total of odd numbers.

Notes:
    Raises a TypeError if non-integer elements are present.
"""

def compare_docstrings(manual: str, ai: str) -> None:
    """Simple comparison that prints presence of common doc sections."""
    sections = ["Args", "Returns", "Raises", "Examples", "Notes"]
    print("Manual docstring:")
    print(manual.strip(), end="\n\n")
    print("AI-generated docstring:")
    print(ai.strip(), end="\n\n")

    print("Section presence comparison:")
    for sec in sections:
        m_has = sec in manual
        ai_has = sec in ai
        print(f"  {sec:8}: manual={'Yes' if m_has else 'No '}, ai={'Yes' if ai_has else 'No '}")

# Example usage
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6]
    ev, od = sum_even_odd(data)
    print(f"Even sum: {ev}, Odd sum: {od}\n")
    compare_docstrings(sum_even_odd.__doc__ or "", ai_docstring)