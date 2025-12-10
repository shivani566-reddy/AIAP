def format_name(first_name, last_name):
    """
    Format first and last names as 'Last, First'
    
    Args:
        first_name (str): First name
        last_name (str): Last name
    
    Returns:
        str: Formatted name as 'Last, First'
    """
    return f"{last_name.title()}, {first_name.title()}"

def get_user_input():
    """
    Get first and last name input from user with validation
    
    Returns:
        tuple: (first_name, last_name)
    """
    while True:
        first_name = input("Enter first name: ").strip()
        if first_name and first_name.isalpha():
            break
        print("Please enter a valid first name (letters only).")
    
    while True:
        last_name = input("Enter last name: ").strip()
        if last_name and last_name.isalpha():
            break
        print("Please enter a valid last name (letters only).")
    
    return first_name, last_name

if __name__ == "__main__":
    first_name, last_name = get_user_input()
    formatted_name = format_name(first_name, last_name)
    print(f"Formatted name: {formatted_name}")