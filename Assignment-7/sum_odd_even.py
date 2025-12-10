"""
Python program to calculate the sum of odd and even numbers using user input.
This program takes numbers from the user and calculates the sum of odd numbers
and the sum of even numbers separately.
"""

def get_numbers_from_user():
    """
    Get numbers from user input.
    
    Returns:
        list: List of numbers entered by the user
    """
    numbers = []
    print("Enter numbers to calculate sum of odd and even numbers.")
    print("Enter 'done' or press Enter with no input when finished.\n")
    
    while True:
        try:
            user_input = input("Enter a number (or 'done' to finish): ").strip()
            
            # Check if user wants to finish
            if user_input.lower() == 'done' or user_input == '':
                break
            
            # Convert to integer and add to list
            number = int(user_input)
            numbers.append(number)
            print(f"Added {number} to the list.")
            
        except ValueError:
            print("Invalid input! Please enter a valid integer or 'done' to finish.")
    
    return numbers


def calculate_sums(numbers):
    """
    Calculate the sum of odd numbers and sum of even numbers.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        tuple: (sum_of_odd, sum_of_even, odd_numbers, even_numbers)
    """
    sum_of_odd = 0
    sum_of_even = 0
    odd_numbers = []
    even_numbers = []
    
    for num in numbers:
        if num % 2 == 0:  # Even number
            sum_of_even += num
            even_numbers.append(num)
        else:  # Odd number
            sum_of_odd += num
            odd_numbers.append(num)
    
    return sum_of_odd, sum_of_even, odd_numbers, even_numbers


def display_results(numbers, sum_of_odd, sum_of_even, odd_numbers, even_numbers):
    """
    Display the input numbers, odd/even classification, and their sums.
    
    Args:
        numbers (list): List of input numbers
        sum_of_odd (int): Sum of odd numbers
        sum_of_even (int): Sum of even numbers
        odd_numbers (list): List of odd numbers
        even_numbers (list): List of even numbers
    """
    print("\n" + "="*50)
    print("RESULTS")
    print("="*50)
    
    if not numbers:
        print("No numbers were entered.")
        return
    
    print(f"\nNumbers entered: {numbers}")
    
    # Display odd numbers
    if odd_numbers:
        print(f"\nOdd numbers: {odd_numbers}")
        print(f"Sum of odd numbers: {sum_of_odd}")
    else:
        print("\nNo odd numbers found.")
        print("Sum of odd numbers: 0")
    
    # Display even numbers
    if even_numbers:
        print(f"\nEven numbers: {even_numbers}")
        print(f"Sum of even numbers: {sum_of_even}")
    else:
        print("\nNo even numbers found.")
        print("Sum of even numbers: 0")
    
    print("\n" + "="*50)


def main():
    """
    Main function to run the odd/even sum calculator.
    """
    print("="*50)
    print("SUM OF ODD AND EVEN NUMBERS CALCULATOR")
    print("="*50)
    print()
    
    # Get numbers from user
    numbers = get_numbers_from_user()
    
    # Check if any numbers were entered
    if not numbers:
        print("\nNo numbers entered. Exiting...")
        return
    
    # Calculate sums of odd and even numbers
    sum_of_odd, sum_of_even, odd_numbers, even_numbers = calculate_sums(numbers)
    
    # Display results
    display_results(numbers, sum_of_odd, sum_of_even, odd_numbers, even_numbers)


if __name__ == "__main__":
    main()






