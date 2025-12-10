import math
from typing import Union, Dict

def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle.
    
    Parameters
    ----------
    radius : float
        The radius of the circle (must be positive).
    
    Returns
    -------
    float
        The area of the circle.
    
    Raises
    ------
    ValueError
        If radius is negative or zero.
    TypeError
        If radius is not a number.
    
    Examples
    --------
    >>> calculate_circle_area(5)
    78.54
    """
    # Validate input type
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    
    # Validate radius is positive
    if radius <= 0:
        raise ValueError("Radius must be positive")
    
    # Calculate area using formula: A = π * r²
    area = math.pi * radius ** 2
    
    # Return rounded area to 2 decimal places
    return round(area, 2)


def calculate_rectangle_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.
    
    Parameters
    ----------
    length : float
        The length of the rectangle (must be positive).
    width : float
        The width of the rectangle (must be positive).
    
    Returns
    -------
    float
        The area of the rectangle.
    
    Raises
    ------
    ValueError
        If length or width is negative or zero.
    TypeError
        If length or width is not a number.
    
    Examples
    --------
    >>> calculate_rectangle_area(5, 3)
    15
    """
    # Validate input types
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Length and width must be numbers")
    
    # Validate dimensions are positive
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive")
    
    # Calculate area using formula: A = length * width
    area = length * width
    
    # Return rounded area to 2 decimal places
    return round(area, 2)


def calculate_triangle_area(base: float, height: float) -> float:
    """
    Calculate the area of a triangle.
    
    Parameters
    ----------
    base : float
        The base of the triangle (must be positive).
    height : float
        The height of the triangle (must be positive).
    
    Returns
    -------
    float
        The area of the triangle.
    
    Raises
    ------
    ValueError
        If base or height is negative or zero.
    TypeError
        If base or height is not a number.
    
    Examples
    --------
    >>> calculate_triangle_area(5, 4)
    10.0
    """
    # Validate input types
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Base and height must be numbers")
    
    # Validate dimensions are positive
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive")
    
    # Calculate area using formula: A = (base * height) / 2
    area = (base * height) / 2
    
    # Return rounded area to 2 decimal places
    return round(area, 2)


def calculate_square_area(side: float) -> float:
    """
    Calculate the area of a square.
    
    Parameters
    ----------
    side : float
        The side length of the square (must be positive).
    
    Returns
    -------
    float
        The area of the square.
    
    Raises
    ------
    ValueError
        If side is negative or zero.
    TypeError
        If side is not a number.
    
    Examples
    --------
    >>> calculate_square_area(5)
    25
    """
    # Validate input type
    if not isinstance(side, (int, float)):
        raise TypeError("Side must be a number")
    
    # Validate side is positive
    if side <= 0:
        raise ValueError("Side must be positive")
    
    # Calculate area using formula: A = side²
    area = side ** 2
    
    # Return rounded area to 2 decimal places
    return round(area, 2)


def calculate_ellipse_area(major_axis: float, minor_axis: float) -> float:
    """
    Calculate the area of an ellipse.
    
    Parameters
    ----------
    major_axis : float
        The major axis (semi-major axis length, must be positive).
    minor_axis : float
        The minor axis (semi-minor axis length, must be positive).
    
    Returns
    -------
    float
        The area of the ellipse.
    
    Raises
    ------
    ValueError
        If major_axis or minor_axis is negative or zero.
    TypeError
        If major_axis or minor_axis is not a number.
    
    Examples
    --------
    >>> calculate_ellipse_area(5, 3)
    47.12
    """
    # Validate input types
    if not isinstance(major_axis, (int, float)) or not isinstance(minor_axis, (int, float)):
        raise TypeError("Major and minor axes must be numbers")
    
    # Validate axes are positive
    if major_axis <= 0 or minor_axis <= 0:
        raise ValueError("Major and minor axes must be positive")
    
    # Calculate area using formula: A = π * a * b
    area = math.pi * major_axis * minor_axis
    
    # Return rounded area to 2 decimal places
    return round(area, 2)


def get_positive_float(prompt: str) -> float:
    """
    Get a positive float input from the user with validation.
    
    Parameters
    ----------
    prompt : str
        The prompt message to display to the user.
    
    Returns
    -------
    float
        The positive float value entered by the user.
    
    Examples
    --------
    >>> radius = get_positive_float("Enter radius: ")
    Enter radius: 5
    """
    while True:
        try:
            # Prompt user for input
            value = input(prompt).strip()
            
            # Convert to float
            number = float(value)
            
            # Validate positive value
            if number <= 0:
                print("Error: Please enter a positive number.")
                continue
            
            # Return valid positive number
            return number
        except ValueError:
            # Handle invalid input
            print("Error: Please enter a valid number.")


def calculate_circle_interactive() -> float:
    """
    Interactive function to calculate circle area from user input.
    
    Returns
    -------
    float
        The calculated area of the circle.
    """
    # Prompt user for radius
    radius = get_positive_float("Enter the radius of the circle: ")
    
    # Calculate area
    area = calculate_circle_area(radius)
    
    # Return calculated area
    return area


def calculate_rectangle_interactive() -> float:
    """
    Interactive function to calculate rectangle area from user input.
    
    Returns
    -------
    float
        The calculated area of the rectangle.
    """
    # Prompt user for length
    length = get_positive_float("Enter the length of the rectangle: ")
    
    # Prompt user for width
    width = get_positive_float("Enter the width of the rectangle: ")
    
    # Calculate area
    area = calculate_rectangle_area(length, width)
    
    # Return calculated area
    return area


def calculate_triangle_interactive() -> float:
    """
    Interactive function to calculate triangle area from user input.
    
    Returns
    -------
    float
        The calculated area of the triangle.
    """
    # Prompt user for base
    base = get_positive_float("Enter the base of the triangle: ")
    
    # Prompt user for height
    height = get_positive_float("Enter the height of the triangle: ")
    
    # Calculate area
    area = calculate_triangle_area(base, height)
    
    # Return calculated area
    return area


def calculate_square_interactive() -> float:
    """
    Interactive function to calculate square area from user input.
    
    Returns
    -------
    float
        The calculated area of the square.
    """
    # Prompt user for side length
    side = get_positive_float("Enter the side length of the square: ")
    
    # Calculate area
    area = calculate_square_area(side)
    
    # Return calculated area
    return area


def calculate_ellipse_interactive() -> float:
    """
    Interactive function to calculate ellipse area from user input.
    
    Returns
    -------
    float
        The calculated area of the ellipse.
    """
    # Prompt user for major axis
    major_axis = get_positive_float("Enter the major axis of the ellipse: ")
    
    # Prompt user for minor axis
    minor_axis = get_positive_float("Enter the minor axis of the ellipse: ")
    
    # Calculate area
    area = calculate_ellipse_area(major_axis, minor_axis)
    
    # Return calculated area
    return area


def display_menu() -> None:
    """
    Display the main menu for shape selection.
    
    Returns
    -------
    None
    """
    # Print menu header
    print("\n" + "="*60)
    print("Shape Area Calculator")
    print("="*60)
    
    # Print menu options
    print("\nSelect a shape to calculate area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Square")
    print("5. Ellipse")
    print("6. Exit")
    
    # Print menu footer
    print("="*60)


def main():
    """
    Main function to run the shape area calculator application.
    
    Returns
    -------
    None
    """
    while True:
        # Display menu
        display_menu()
        
        # Get user choice
        choice = input("Enter your choice (1-6): ").strip()
        
        # Process user choice
        if choice == '1':
            try:
                # Calculate circle area
                area = calculate_circle_interactive()
                print(f"\n✓ Circle area: {area} square units")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            try:
                # Calculate rectangle area
                area = calculate_rectangle_interactive()
                print(f"\n✓ Rectangle area: {area} square units")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '3':
            try:
                # Calculate triangle area
                area = calculate_triangle_interactive()
                print(f"\n✓ Triangle area: {area} square units")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '4':
            try:
                # Calculate square area
                area = calculate_square_interactive()
                print(f"\n✓ Square area: {area} square units")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '5':
            try:
                # Calculate ellipse area
                area = calculate_ellipse_interactive()
                print(f"\n✓ Ellipse area: {area} square units")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '6':
            # Exit program
            print("\nThank you for using Shape Area Calculator. Goodbye!")
            break
        
        else:
            # Handle invalid choice
            print("Invalid choice. Please enter a number between 1 and 6.")


def run_test_cases():
    """
    Run predefined test cases to demonstrate all shape calculations.
    
    Returns
    -------
    None
    """
    # Print test header
    print("\n" + "="*60)
    print("Shape Area Calculator - Test Cases")
    print("="*60)
    
    # Test circle
    print("\n1. Circle Tests:")
    print(f"   Circle (r=5): {calculate_circle_area(5)} sq units")
    print(f"   Circle (r=10): {calculate_circle_area(10)} sq units")
    
    # Test rectangle
    print("\n2. Rectangle Tests:")
    print(f"   Rectangle (l=5, w=3): {calculate_rectangle_area(5, 3)} sq units")
    print(f"   Rectangle (l=10, w=7): {calculate_rectangle_area(10, 7)} sq units")
    
    # Test triangle
    print("\n3. Triangle Tests:")
    print(f"   Triangle (b=5, h=4): {calculate_triangle_area(5, 4)} sq units")
    print(f"   Triangle (b=10, h=8): {calculate_triangle_area(10, 8)} sq units")
    
    # Test square
    print("\n4. Square Tests:")
    print(f"   Square (s=5): {calculate_square_area(5)} sq units")
    print(f"   Square (s=10): {calculate_square_area(10)} sq units")
    
    # Test ellipse
    print("\n5. Ellipse Tests:")
    print(f"   Ellipse (a=5, b=3): {calculate_ellipse_area(5, 3)} sq units")
    print(f"   Ellipse (a=10, b=6): {calculate_ellipse_area(10, 6)} sq units")
    
    # Print test footer
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    # Ask user if they want to see test cases first
    show_tests = input("Do you want to see test cases? (yes/no): ").strip().lower()
    
    if show_tests == 'yes':
        # Run and display test cases
        run_test_cases()
    
    # Run main application
    main()