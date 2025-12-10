# ...existing code...
import os

def count_lines_few_shot(file_path):
    """
    Count lines in a .txt file (few-shot style: demonstrate small examples then apply same rule).
    Returns:
        int: number of lines in the file
    """
    # Few-shot illustrative examples (not used for prediction, only demonstration)
    examples = {
        "example_one.txt": 1,
        "example_two.txt": 2
    }
    # Real counting rule learned from examples: open file and count newline-separated lines
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return sum(1 for _ in f)
    except OSError:
        raise

def get_user_input_file():
    """Prompt user for a valid existing .txt file path and return it."""
    while True:
        path = input("Enter path to a .txt file: ").strip()
        if not path:
            print("Please enter a file path.")
            continue
        if not os.path.isfile(path):
            print("File does not exist. Try again.")
            continue
        if not path.lower().endswith(".txt"):
            print("Please provide a .txt file.")
            continue
        return path

if __name__ == "__main__":
    file_path = get_user_input_file()
    try:
        lines = count_lines_few_shot(file_path)
        print(f"{file_path} contains {lines} lines.")
    except Exception as e:
        print(f"Error reading file: {e}")
# ...existing code...