# ...existing code...

def is_reverse():
    """Ask the user for a string, print whether it's the same when reversed (palindrome), and return True/False."""
    s = input("Enter a string to check if it's the same when reversed: ").strip()
    if s == s[::-1]:
        print(f"'{s}' is reversed (palindrome).")
        return True
    else:
        print(f"'{s}' is not reversed.")
        return False

if __name__ == "__main__":
    is_reverse()

# ...existing code...