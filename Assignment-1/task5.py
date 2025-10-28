def find_largest():
    """Ask the user to input numbers and find the largest among them."""
    numbers = []
    
    # Get the number of elements
    while True:
        try:
            n = int(input("How many numbers do you want to enter? ").strip())
            if n <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Get the numbers from user
    for i in range(n):
        while True:
            try:
                num = float(input(f"Enter number {i+1}: ").strip())
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    if not numbers:
        print("No numbers were entered.")
        return None
    
    largest = max(numbers)
    print(f"\nThe largest number in the list is: {largest}")
    print(f"The complete list is: {numbers}")
    
    return largest

if __name__ == "__main__":
    find_largest()