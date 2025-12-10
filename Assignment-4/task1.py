def is_leap_year(year):
    """
    Check if a given year is a leap year.
    
    Args:
        year (int): The year to check
    
    Returns:
        bool: True if the year is a leap year, False otherwise
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_user_input():
    """
    Get year input from user with validation.
    
    Returns:
        int: Valid year input from user
    """
    while True:
        try:
            year = int(input("Enter a year to check if it's a leap year: "))
            if year > 0:
                return year
            else:
                print("Please enter a positive year.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    year = get_user_input()
    result = "is" if is_leap_year(year) else "is not"
    print(f"{year} {result} a leap year")