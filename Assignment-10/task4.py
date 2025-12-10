def process_scores(scores: list) -> None:
    """
    Process and display statistics for a list of scores.
    
    Parameters
    ----------
    scores : list
        A list of numeric scores.
    
    Returns
    -------
    None
    
    Examples
    --------
    >>> process_scores([85, 90, 78, 92, 88])
    Average: 86.6
    Highest: 92
    Lowest: 78
    """
    # Validate input
    if not scores:
        print("Error: Scores list is empty")
        return
    
    # Calculate total using sum()
    total = sum(scores)
    # Calculate average
    avg = total / len(scores)
    
    # Find highest and lowest using built-in functions
    highest = max(scores)
    lowest = min(scores)
    
    # Display results
    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)


# Alternative Implementation v2: Using Statistics Module (OPTIMIZED)
def process_scores_v2(scores: list) -> None:
    """
    Process scores using statistics module (OPTIMIZED).
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Parameters
    ----------
    scores : list
        A list of numeric scores.
    
    Returns
    -------
    None
    """
    import statistics
    
    # Validate input
    if not scores:
        print("Error: Scores list is empty")
        return
    
    # Use statistics module for mean
    avg = statistics.mean(scores)
    highest = max(scores)
    lowest = min(scores)
    
    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)


# Alternative Implementation v3: Using NumPy (OPTIMIZED for Large Data)
def process_scores_v3(scores: list) -> None:
    """
    Process scores using NumPy (OPTIMIZED for large datasets).
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Parameters
    ----------
    scores : list
        A list of numeric scores.
    
    Returns
    -------
    None
    """
    try:
        import numpy as np
        
        # Validate input
        if not scores:
            print("Error: Scores list is empty")
            return
        
        # Convert to numpy array
        scores_array = np.array(scores)
        
        # Use NumPy functions for calculations
        avg = np.mean(scores_array)
        highest = np.max(scores_array)
        lowest = np.min(scores_array)
        
        print("Average:", avg)
        print("Highest:", highest)
        print("Lowest:", lowest)
    except ImportError:
        print("NumPy not installed. Using standard library instead.")
        process_scores(scores)


# Alternative Implementation v4: Using Dictionary Return (OPTIMIZED)
def process_scores_v4(scores: list) -> dict:
    """
    Process scores and return dictionary with results (OPTIMIZED).
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Parameters
    ----------
    scores : list
        A list of numeric scores.
    
    Returns
    -------
    dict
        Dictionary containing average, highest, and lowest scores.
    """
    # Validate input
    if not scores:
        return {"error": "Scores list is empty"}
    
    # Create results dictionary
    results = {
        "average": sum(scores) / len(scores),
        "highest": max(scores),
        "lowest": min(scores)
    }
    
    # Display results
    print("Average:", results["average"])
    print("Highest:", results["highest"])
    print("Lowest:", results["lowest"])
    
    return results


# Alternative Implementation v5: Using Functional Programming (OPTIMIZED)
def process_scores_v5(scores: list) -> None:
    """
    Process scores using functional programming approach (OPTIMIZED).
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Parameters
    ----------
    scores : list
        A list of numeric scores.
    
    Returns
    -------
    None
    """
    from functools import reduce
    
    # Validate input
    if not scores:
        print("Error: Scores list is empty")
        return
    
    # Calculate average using reduce
    avg = reduce(lambda x, y: x + y, scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)
    
    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)


# Alternative Implementation v6: Using Class-Based Approach (OPTIMIZED)
class ScoreProcessor:
    """Class to process and analyze scores."""
    
    def __init__(self, scores: list):
        """
        Initialize ScoreProcessor.
        
        Parameters
        ----------
        scores : list
            A list of numeric scores.
        """
        self.scores = scores
        self.average = None
        self.highest = None
        self.lowest = None
    
    def process(self) -> None:
        """Process the scores and calculate statistics."""
        # Validate input
        if not self.scores:
            print("Error: Scores list is empty")
            return
        
        # Calculate statistics
        self.average = sum(self.scores) / len(self.scores)
        self.highest = max(self.scores)
        self.lowest = min(self.scores)
    
    def display(self) -> None:
        """Display the calculated statistics."""
        if self.average is None:
            print("Error: Process scores first")
            return
        
        print("Average:", self.average)
        print("Highest:", self.highest)
        print("Lowest:", self.lowest)


def process_scores_v6(scores: list) -> None:
    """Wrapper function for class-based approach."""
    processor = ScoreProcessor(scores)
    processor.process()
    processor.display()


# Alternative Implementation v7: Using One-Liner with Tuple Unpacking (OPTIMIZED)
def process_scores_v7(scores: list) -> None:
    """
    Process scores using tuple unpacking (OPTIMIZED).
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Parameters
    ----------
    scores : list
        A list of numeric scores.
    
    Returns
    -------
    None
    """
    # Validate and process in one step
    if scores:
        avg, highest, lowest = sum(scores) / len(scores), max(scores), min(scores)
        print("Average:", avg)
        print("Highest:", highest)
        print("Lowest:", lowest)
    else:
        print("Error: Scores list is empty")


# Alternative Implementation v8: Using Lambda with Map (OPTIMIZED)
def process_scores_v8(scores: list) -> None:
    """
    Process scores using lambda and functional approach (OPTIMIZED).
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Parameters
    ----------
    scores : list
        A list of numeric scores.
    
    Returns
    -------
    None
    """
    # Validate input
    if not scores:
        print("Error: Scores list is empty")
        return
    
    # Calculate using built-in functions
    calculations = {
        "average": lambda s: sum(s) / len(s),
        "highest": lambda s: max(s),
        "lowest": lambda s: min(s)
    }
    
    # Apply calculations
    results = {key: calc(scores) for key, calc in calculations.items()}
    
    print("Average:", results["average"])
    print("Highest:", results["highest"])
    print("Lowest:", results["lowest"])


# Alternative Implementation v9: Using Sorted Approach (OPTIMIZED)
def process_scores_v9(scores: list) -> None:
    """
    Process scores using sorted approach (OPTIMIZED).
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Parameters
    ----------
    scores : list
        A list of numeric scores.
    
    Returns
    -------
    None
    """
    # Validate input
    if not scores:
        print("Error: Scores list is empty")
        return
    
    # Sort scores
    sorted_scores = sorted(scores)
    
    # Get statistics from sorted list
    avg = sum(sorted_scores) / len(sorted_scores)
    highest = sorted_scores[-1]
    lowest = sorted_scores[0]
    
    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)


# Alternative Implementation v10: Using heapq for Extremes (OPTIMIZED)
def process_scores_v10(scores: list) -> None:
    """
    Process scores using heapq for finding extremes (OPTIMIZED).
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Parameters
    ----------
    scores : list
        A list of numeric scores.
    
    Returns
    -------
    None
    """
    import heapq
    
    # Validate input
    if not scores:
        print("Error: Scores list is empty")
        return
    
    # Calculate average
    avg = sum(scores) / len(scores)
    
    # Get highest and lowest
    highest = max(scores)
    lowest = min(scores)
    
    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)


# Alternative Implementation v11: Using zip and Reduce (OPTIMIZED)
def process_scores_v11(scores: list) -> None:
    """
    Process scores using zip and reduce (OPTIMIZED).
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Parameters
    ----------
    scores : list
        A list of numeric scores.
    
    Returns
    -------
    None
    """
    from functools import reduce
    
    # Validate input
    if not scores:
        print("Error: Scores list is empty")
        return
    
    # Calculate statistics
    avg = sum(scores) / len(scores)
    highest = reduce(lambda a, b: a if a > b else b, scores)
    lowest = reduce(lambda a, b: a if a < b else b, scores)
    
    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)


# Comprehensive Testing
def run_comparison_tests():
    """Run comprehensive tests for all implementations."""
    
    test_cases = [
        ([85, 90, 78, 92, 88], "Normal case"),
        ([100, 100, 100], "All same"),
        ([50], "Single score"),
        ([75, 80, 85, 90, 95], "Ascending order"),
        ([95, 90, 85, 80, 75], "Descending order"),
        (list(range(1, 101)), "Large dataset (1-100)"),
    ]
    
    implementations = [
        ("Original (Optimized)", process_scores),
        ("v2: Statistics Module", process_scores_v2),
        ("v3: NumPy", process_scores_v3),
        ("v4: Dictionary Return", process_scores_v4),
        ("v5: Functional (Reduce)", process_scores_v5),
        ("v6: Class-Based", process_scores_v6),
        ("v7: Tuple Unpacking", process_scores_v7),
        ("v8: Lambda/Map", process_scores_v8),
        ("v9: Sorted Approach", process_scores_v9),
        ("v10: HeapQ", process_scores_v10),
        ("v11: Reduce Both", process_scores_v11),
    ]
    
    print("="*80)
    print("Score Processing - Multiple Implementations Comparison")
    print("="*80)
    
    for test_num, (scores, description) in enumerate(test_cases, 1):
        print(f"\nTest Case {test_num}: {description}")
        print(f"Scores: {scores if len(str(scores)) < 60 else str(scores)[:60] + '...'}")
        print("-" * 80)
        
        for impl_name, impl_func in implementations:
            try:
                print(f"\n{impl_name}:")
                impl_func(scores)
            except Exception as e:
                print(f"✗ Error: {e}")


def run_performance_tests():
    """Run performance comparison tests."""
    import time
    
    print("\n" + "="*80)
    print("PERFORMANCE COMPARISON (Time in seconds)")
    print("="*80)
    
    sizes = [1000, 10000, 100000, 1000000]
    
    for size in sizes:
        print(f"\nTest Size: {size} scores")
        print("-" * 80)
        
        scores = list(range(1, size + 1))
        
        implementations = [
            ("Original (Optimized)", process_scores),
            ("v2: Statistics", process_scores_v2),
            ("v5: Functional", process_scores_v5),
            ("v7: Tuple Unpacking", process_scores_v7),
            ("v8: Lambda/Dict", process_scores_v8),
            ("v9: Sorted", process_scores_v9),
        ]
        
        for impl_name, impl_func in implementations:
            try:
                start = time.time()
                for _ in range(100):  # Run 100 times
                    # Redirect output to suppress print statements
                    import io
                    import sys
                    old_stdout = sys.stdout
                    sys.stdout = io.StringIO()
                    
                    impl_func(scores)
                    
                    sys.stdout = old_stdout
                
                elapsed = time.time() - start
                print(f"{impl_name:30} : {elapsed:.6f}s")
            except Exception as e:
                print(f"{impl_name:30} : ✗ Error - {str(e)[:30]}")


def demonstrate_differences():
    """Demonstrate the differences between implementations."""
    
    print("\n" + "="*80)
    print("Demonstrating Different Approaches")
    print("="*80)
    
    scores = [85, 90, 78, 92, 88]
    
    print("\nApproach 1: Original Optimized (Using Built-in Functions)")
    print("-" * 80)
    process_scores(scores)
    
    print("\nApproach 2: Statistics Module")
    print("-" * 80)
    process_scores_v2(scores)
    
    print("\nApproach 3: Class-Based")
    print("-" * 80)
    process_scores_v6(scores)
    
    print("\nApproach 4: Dictionary Return")
    print("-" * 80)
    result = process_scores_v4(scores)
    print(f"Returned: {result}")
    
    print("\nApproach 5: NumPy (if available)")
    print("-" * 80)
    process_scores_v3(scores)


if __name__ == "__main__":
    # Run comparison tests
    run_comparison_tests()
    
    # Run performance tests
    run_performance_tests()
    
    # Demonstrate differences
    demonstrate_differences()