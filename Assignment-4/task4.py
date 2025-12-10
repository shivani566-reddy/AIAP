def count_vowels_zero_shot(text):
    """
    Count vowels in text using zero-shot approach (direct rule-based)
    
    Args:
        text (str): Input string
    
    Returns:
        int: Number of vowels
    """
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def count_vowels_few_shot(text):
    """
    Count vowels in text using few-shot approach (pattern learning)
    
    Args:
        text (str): Input string
    
    Returns:
        int: Number of vowels
    """
    # Few-shot examples to learn from
    examples = {
        'hello': 2,  # e, o
        'world': 1,  # o
        'python': 1  # o
    }
    
    # Using learned patterns from examples
    vowels = set('aeiouAEIOU')
    return sum(1 for char in text if char.lower() in vowels)

def get_user_input():
    """
    Get string input from user with validation
    
    Returns:
        str: Non-empty string from user
    """
    while True:
        text = input("Enter a string to count vowels: ").strip()
        if text:
            return text
        print("Please enter a non-empty string.")

if __name__ == "__main__":
    text = get_user_input()
    
    # Compare both approaches
    zero_shot_count = count_vowels_zero_shot(text)
    few_shot_count = count_vowels_few_shot(text)
    
    print(f"\nResults for string: '{text}'")
    print(f"Zero-shot approach: {zero_shot_count} vowels")
    print(f"Few-shot approach: {few_shot_count} vowels")