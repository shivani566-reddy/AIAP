def cm_to_inches(centimeters):
    """
    Convert centimeters to inches
    
    Args:
        centimeters (float): Length in centimeters
    
    Returns:
        float: Length in inches
    """
    # 1 inch = 2.54 centimeters
    return centimeters / 2.54

def get_user_input():
    """
    Get centimeter input from user with validation
    
    Returns:
        float: Valid centimeter value from user
    """
    while True:
        try:
            cm = float(input("Enter length in centimeters: "))
            if cm >= 0:
                return cm
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    centimeters = get_user_input()
    inches = cm_to_inches(centimeters)
    print(f"{centimeters:.2f} centimeters = {inches:.2f} inches")