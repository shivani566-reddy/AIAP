"""
Python program to calculate the sum of squares using user input.
This program takes numbers from the user and calculates the sum of their squares.
"""

def get_numbers_from_user():
    """
    Get numbers from user input.
    
    Returns:
        list: List of numbers entered by the user
    """
    numbers = []
    print("Enter numbers to calculate sum of squares.")
    print("Enter 'done' or press Enter with no input when finished.\n")
    
    while True:
        try:
            user_input = input("Enter a number (or 'done' to finish): ").strip()
            
            # Check if user wants to finish
            if user_input.lower() == 'done' or user_input == '':
                break
            
            # Convert to float and add to list
            number = float(user_input)
            numbers.append(number)
            print(f"Added {number} to the list.")
            
        except ValueError:
            print("Invalid input! Please enter a valid number or 'done' to finish.")
    
    return numbers


def calculate_sum_of_squares(numbers):
    """
    Calculate the sum of squares for a list of numbers.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        float: Sum of squares of all numbers
    """
    sum_of_squares = 0
    for num in numbers:
        sum_of_squares += num ** 2
    return sum_of_squares


def display_results(numbers, sum_of_squares):
    """
    Display the input numbers, their squares, and the sum.
    
    Args:
        numbers (list): List of input numbers
        sum_of_squares (float): Sum of squares
    """
    print("\n" + "="*50)
    print("RESULTS")
    print("="*50)
    
    if not numbers:
        print("No numbers were entered.")
        return
    
    print(f"\nNumbers entered: {numbers}")
    print("\nSquares:")
    for i, num in enumerate(numbers, 1):
        print(f"  {i}. {num}² = {num ** 2}")
    
    print(f"\nSum of squares: {sum_of_squares}")
    print("="*50)


def main():
    """
    Main function to run the sum of squares calculator.
    """
    print("="*50)
    print("SUM OF SQUARES CALCULATOR")
    print("="*50)
    print()
    
    # Get numbers from user
    numbers = get_numbers_from_user()
    
    # Check if any numbers were entered
    if not numbers:
        print("\nNo numbers entered. Exiting...")
        return
    
    # Calculate sum of squares
    sum_of_squares = calculate_sum_of_squares(numbers)
    2
    # Display results
    display_results(numbers, sum_of_squares)


if __name__ == "__main__":
    main()

