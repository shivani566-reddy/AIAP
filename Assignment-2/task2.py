def is_palindrome(number: int) -> bool:
    """
    Check if a number is a palindrome.
    
    A palindrome number reads the same forwards and backwards.
    
    Parameters
    ----------
    number : int
        The number to check. Can be positive or negative.
    
    Returns
    -------
    bool
        True if the number is a palindrome, False otherwise.
    
    Raises
    ------
    TypeError
        If the input is not an integer.
    
    Examples
    --------
    >>> is_palindrome(121)
    True
    >>> is_palindrome(123)
    False
    >>> is_palindrome(0)
    True
    >>> is_palindrome(-121)
    False
    """
    # Check if input is an integer
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Convert to string to check palindrome (ignore negative sign)
    num_str = str(abs(number))
    
    # Compare string with its reverse
    return num_str == num_str[::-1]


def get_user_input() -> int:
    """
    Get a valid integer input from the user.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    int
        The integer provided by the user.
    
    Examples
    --------
    >>> number = get_user_input()
    Enter a number to check if it's a palindrome: 121
    """
    while True:
        try:
            # Prompt user for input
            user_input = input("Enter a number to check if it's a palindrome: ").strip()
            
            # Convert input to integer
            number = int(user_input)
            
            # Return the valid integer
            return number
        except ValueError:
            # Handle invalid input
            print("Invalid input! Please enter a valid integer.")


def display_result(number: int, is_pal: bool) -> None:
    """
    Display the palindrome check result in a formatted manner.
    
    Parameters
    ----------
    number : int
        The number that was checked.
    is_pal : bool
        Whether the number is a palindrome or not.
    
    Returns
    -------
    None
    
    Examples
    --------
    >>> display_result(121, True)
    """
    # Create formatted output message
    result_text = "is a palindrome" if is_pal else "is NOT a palindrome"
    
    # Print result with formatting
    print("\n" + "="*50)
    print(f"Number: {number}")
    print(f"Result: {number} {result_text}")
    print("="*50 + "\n")


def check_multiple_numbers(numbers: list[int]) -> dict:
    """
    Check multiple numbers for palindrome property.
    
    Parameters
    ----------
    numbers : list[int]
        A list of integers to check.
    
    Returns
    -------
    dict
        A dictionary with numbers as keys and palindrome status as values.
    
    Examples
    --------
    >>> check_multiple_numbers([121, 123, 0, -121])
    {121: True, 123: False, 0: True, -121: False}
    """
    # Initialize empty dictionary
    results = {}
    
    # Iterate through each number in the list
    for number in numbers:
        # Check if each number is a palindrome
        results[number] = is_palindrome(number)
    
    # Return results dictionary
    return results


def display_multiple_results(results: dict) -> None:
    """
    Display multiple palindrome check results in a formatted manner.
    
    Parameters
    ----------
    results : dict
        Dictionary containing numbers and their palindrome status.
    
    Returns
    -------
    None
    """
    # Print header
    print("\n" + "="*60)
    print("Palindrome Check Results for Multiple Numbers")
    print("="*60)
    
    # Iterate through results and display each one
    for number, is_pal in results.items():
        status = "✓ Palindrome" if is_pal else "✗ Not Palindrome"
        print(f"{number:>10} : {status}")
    
    # Print footer
    print("="*60 + "\n")


def main():
    """
    Main function to run the palindrome checker application.
    
    Returns
    -------
    None
    """
    # Print welcome message
    print("\n" + "="*60)
    print("Welcome to Palindrome Checker")
    print("="*60)
    
    while True:
        # Display menu options
        print("\nOptions:")
        print("1. Check a single number")
        print("2. Check multiple numbers")
        print("3. Exit")
        
        # Get user choice
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == '1':
            # Single number palindrome check
            try:
                number = get_user_input()
                is_pal = is_palindrome(number)
                display_result(number, is_pal)
            except TypeError as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            # Multiple numbers palindrome check
            try:
                # Get comma-separated numbers from user
                numbers_input = input("Enter numbers separated by commas: ").strip()
                
                # Parse the input and convert to list of integers
                numbers = [int(n.strip()) for n in numbers_input.split(',')]
                
                # Check all numbers
                results = check_multiple_numbers(numbers)
                
                # Display results
                display_multiple_results(results)
            except ValueError:
                print("Error: Please enter valid integers separated by commas.")
        
        elif choice == '3':
            # Exit the program
            print("Thank you for using Palindrome Checker. Goodbye!")
            break
        
        else:
            # Handle invalid choice
            print("Invalid choice. Please enter 1, 2, or 3.")


# Demonstration with test cases
def run_test_cases():
    """
    Run predefined test cases to demonstrate palindrome checking.
    
    Returns
    -------
    None
    """
    # Define test cases
    test_numbers = [0, 1, 11, 121, 123, 1221, 12321, 9009, 10001, -121, 1000]
    
    # Print header
    print("\n" + "="*60)
    print("Palindrome Checker - Test Cases")
    print("="*60)
    
    # Iterate through test cases
    for num in test_numbers:
        try:
            # Check if number is palindrome
            result = is_palindrome(num)
            status = "✓ Palindrome" if result else "✗ Not Palindrome"
            print(f"{num:>10} : {status}")
        except TypeError as e:
            print(f"Error with {num}: {e}")
    
    # Print footer
    print("="*60 + "\n")


if __name__ == "__main__":
    # Ask user if they want to see test cases first
    show_tests = input("Do you want to see test cases? (yes/no): ").strip().lower()
    
    if show_tests == 'yes':
        # Run and display test cases
        run_test_cases()
    
    # Run main application
    main()