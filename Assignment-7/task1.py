

# FIXED - Correct syntax with colon
def add(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Sum of a and b
    """
    return a + b

def subtract(a, b):
    """Subtract two numbers."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide two numbers with zero check."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def get_user_input():
    """Get two numbers from user with validation."""
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("Please enter valid numbers.")

def main():
    print("Calculator Application")
    print("----------------------")
    a, b = get_user_input()
    
    result = add(a, b)
    print(f"{a} + {b} = {result}")

if __name__ == "__main__":
    main()