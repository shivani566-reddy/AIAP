"""
Calculator Module

This module provides basic arithmetic operations including addition, 
subtraction, multiplication, and division.

Functions:
- add(a, b): Returns the sum of two numbers.
- subtract(a, b): Returns the difference of two numbers.
- multiply(a, b): Returns the product of two numbers.
- divide(a, b): Returns the quotient of two numbers.
"""

def add(a: float, b: float) -> float:
    """
    Add two numbers.

    Parameters
    ----------
    a : float
        The first number.
    b : float
        The second number.

    Returns
    -------
    float
        The sum of `a` and `b`.
    """
    return a + b  # Return the sum of a and b


def subtract(a: float, b: float) -> float:
    """
    Subtract two numbers.

    Parameters
    ----------
    a : float
        The number from which to subtract.
    b : float
        The number to subtract.

    Returns
    -------
    float
        The difference of `a` and `b`.
    """
    return a - b  # Return the difference of a and b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    Parameters
    ----------
    a : float
        The first number.
    b : float
        The second number.

    Returns
    -------
    float
        The product of `a` and `b`.
    """
    return a * b  # Return the product of a and b


def divide(a: float, b: float) -> float:
    """
    Divide two numbers.

    Parameters
    ----------
    a : float
        The numerator.
    b : float
        The denominator.

    Returns
    -------
    float
        The quotient of `a` divided by `b`.

    Raises
    ------
    ValueError
        If `b` is zero, a ValueError is raised.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")  # Raise an error if dividing by zero
    return a / b  # Return the quotient of a and b


# Example usage
if __name__ == "__main__":
    print("Addition:", add(5, 3))  # Example of addition
    print("Subtraction:", subtract(5, 3))  # Example of subtraction
    print("Multiplication:", multiply(5, 3))  # Example of multiplication
    print("Division:", divide(5, 3))  # Example of division