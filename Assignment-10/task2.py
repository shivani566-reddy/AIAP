def find_common(a: list, b: list) -> list:
    """
    Find common elements between two lists using nested loop approach.
    
    Parameters
    ----------
    a : list
        The first list.
    b : list
        The second list.
    
    Returns
    -------
    list
        A list of common elements found in both lists.
    
    Examples
    --------
    >>> find_common([1, 2, 3, 4], [3, 4, 5, 6])
    [3, 4]
    """
    # Initialize empty result list
    res = []
    
    # Iterate through each element in first list
    for i in a:
        # Iterate through each element in second list
        for j in b:
            # Check if elements are equal
            if i == j:
                # Append common element to result
                res.append(i)
    
    # Return list of common elements
    return res


def find_common_v2(a: list, b: list) -> list:
    """
    Find common elements using set intersection (OPTIMIZED).
    
    Time Complexity: O(n + m)
    Space Complexity: O(min(n, m))
    
    Parameters
    ----------
    a : list
        The first list.
    b : list
        The second list.
    
    Returns
    -------
    list
        A list of common elements found in both lists.
    
    Examples
    --------
    >>> find_common_v2([1, 2, 3, 4], [3, 4, 5, 6])
    [3, 4]
    """
    # Convert both lists to sets and find intersection
    common_set = set(a) & set(b)
    
    # Convert back to list preserving order from first list
    return [element for element in a if element in common_set]


def find_common_v3(a: list, b: list) -> list:
    """
    Find common elements using list comprehension with 'in' operator (OPTIMIZED).
    
    Time Complexity: O(n * m)
    Space Complexity: O(k) where k is number of common elements
    
    Parameters
    ----------
    a : list
        The first list.
    b : list
        The second list.
    
    Returns
    -------
    list
        A list of common elements found in both lists.
    
    Examples
    --------
    >>> find_common_v3([1, 2, 3, 4], [3, 4, 5, 6])
    [3, 4]
    """
    # Use list comprehension to filter elements present in both lists
    return [element for element in a if element in b]


def find_common_v4(a: list, b: list) -> list:
    """
    Find common elements using filter and lambda (OPTIMIZED).
    
    Time Complexity: O(n * m)
    Space Complexity: O(k) where k is number of common elements
    
    Parameters
    ----------
    a : list
        The first list.
    b : list
        The second list.
    
    Returns
    -------
    list
        A list of common elements found in both lists.
    
    Examples
    --------
    >>> find_common_v4([1, 2, 3, 4], [3, 4, 5, 6])
    [3, 4]
    """
    # Use filter with lambda to find common elements
    return list(filter(lambda x: x in b, a))


def find_common_v5(a: list, b: list) -> list:
    """
    Find common elements using set intersection with order preservation (OPTIMIZED).
    
    Time Complexity: O(n + m)
    Space Complexity: O(min(n, m))
    
    Parameters
    ----------
    a : list
        The first list.
    b : list
        The second list.
    
    Returns
    -------
    list
        A list of common elements found in both lists.
    
    Examples
    --------
    >>> find_common_v5([1, 2, 3, 4], [3, 4, 5, 6])
    [3, 4]
    """
    # Convert second list to set for O(1) lookup
    b_set = set(b)
    
    # Filter first list keeping only elements in second set
    return [element for element in a if element in b_set]


def find_common_v6(a: list, b: list) -> list:
    """
    Find common elements using dict.fromkeys to preserve order (OPTIMIZED).
    
    Time Complexity: O(n + m)
    Space Complexity: O(min(n, m))
    
    Parameters
    ----------
    a : list
        The first list.
    b : list
        The second list.
    
    Returns
    -------
    list
        A list of common elements found in both lists.
    
    Examples
    --------
    >>> find_common_v6([1, 2, 3, 4], [3, 4, 5, 6])
    [3, 4]
    """
    # Create set from second list for fast lookup
    b_set = set(b)
    
    # Use dict.fromkeys to remove duplicates while preserving order
    return list(dict.fromkeys(element for element in a if element in b_set))


def find_common_v7(a: list, b: list) -> list:
    """
    Find common elements using set operations (OPTIMIZED).
    
    Time Complexity: O(n + m)
    Space Complexity: O(min(n, m))
    
    Parameters
    ----------
    a : list
        The first list.
    b : list
        The second list.
    
    Returns
    -------
    list
        A list of common elements found in both lists.
    
    Examples
    --------
    >>> find_common_v7([1, 2, 3, 4], [3, 4, 5, 6])
    [3, 4]
    """
    # Find intersection of two sets
    common_elements = set(a) & set(b)
    
    # Convert to list
    return list(common_elements)


def find_common_v8(a: list, b: list) -> list:
    """
    Find common elements using any() with generator (OPTIMIZED).
    
    Time Complexity: O(n * m) worst case
    Space Complexity: O(k)
    
    Parameters
    ----------
    a : list
        The first list.
    b : list
        The second list.
    
    Returns
    -------
    list
        A list of common elements found in both lists.
    
    Examples
    --------
    >>> find_common_v8([1, 2, 3, 4], [3, 4, 5, 6])
    [3, 4]
    """
    # Use list comprehension with generator expression
    return [x for x in a if any(x == y for y in b)]


def find_common_v9(a: list, b: list) -> list:
    """
    Find common elements using numpy (OPTIMIZED for large arrays).
    
    Time Complexity: O(n + m)
    Space Complexity: O(min(n, m))
    
    Parameters
    ----------
    a : list
        The first list.
    b : list
        The second list.
    
    Returns
    -------
    list
        A list of common elements found in both lists.
    
    Examples
    --------
    >>> find_common_v9([1, 2, 3, 4], [3, 4, 5, 6])
    [3, 4]
    """
    try:
        import numpy as np
        # Use numpy intersect1d for efficient intersection
        common = np.intersect1d(a, b)
        return list(common)
    except ImportError:
        # Fallback to set intersection if numpy not available
        return list(set(a) & set(b))


def find_common_v10(a: list, b: list) -> list:
    """
    Find common elements using sorted two-pointer approach (OPTIMIZED).
    
    Time Complexity: O(n log n + m log m)
    Space Complexity: O(1) excluding output
    
    Parameters
    ----------
    a : list
        The first list.
    b : list
        The second list.
    
    Returns
    -------
    list
        A list of common elements found in both lists.
    
    Examples
    --------
    >>> find_common_v10([1, 2, 3, 4], [3, 4, 5, 6])
    [3, 4]
    """
    # Sort both lists
    sorted_a = sorted(a)
    sorted_b = sorted(b)
    
    # Initialize pointers and result
    i, j = 0, 0
    result = []
    
    # Use two-pointer technique
    while i < len(sorted_a) and j < len(sorted_b):
        if sorted_a[i] == sorted_b[j]:
            # Add to result if not duplicate
            if not result or result[-1] != sorted_a[i]:
                result.append(sorted_a[i])
            i += 1
            j += 1
        elif sorted_a[i] < sorted_b[j]:
            i += 1
        else:
            j += 1
    
    # Return common elements
    return result


# Comprehensive Testing
def run_comparison_tests():
    """Run comprehensive tests comparing all implementations."""
    
    test_cases = [
        ([1, 2, 3, 4], [3, 4, 5, 6], "Basic case"),
        ([1, 1, 2, 2, 3, 3], [2, 2, 3, 3, 4], "Duplicates"),
        ([], [1, 2, 3], "Empty first list"),
        ([1, 2, 3], [], "Empty second list"),
        ([], [], "Both empty"),
        ([1, 2, 3], [1, 2, 3], "Identical lists"),
        ([1, 2, 3], [4, 5, 6], "No common elements"),
        (['a', 'b', 'c'], ['b', 'c', 'd'], "String elements"),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], "Reversed order"),
        (list(range(1000)), list(range(500, 1500)), "Large lists"),
    ]
    
    implementations = [
        ("Original (Nested Loop)", find_common),
        ("v2: Set Intersection", find_common_v2),
        ("v3: List Comprehension", find_common_v3),
        ("v4: Filter + Lambda", find_common_v4),
        ("v5: Set with Order", find_common_v5),
        ("v6: Dict.fromkeys", find_common_v6),
        ("v7: Set Operations", find_common_v7),
        ("v8: Any() Generator", find_common_v8),
        ("v9: NumPy (if available)", find_common_v9),
        ("v10: Two-Pointer", find_common_v10),
    ]
    
    print("="*100)
    print("COMPREHENSIVE OPTIMIZATION TEST - Find Common Elements")
    print("="*100)
    
    for test_num, (list_a, list_b, description) in enumerate(test_cases, 1):
        print(f"\nTest Case {test_num}: {description}")
        print(f"List A: {list_a if len(str(list_a)) < 50 else str(list_a)[:50] + '...'}")
        print(f"List B: {list_b if len(str(list_b)) < 50 else str(list_b)[:50] + '...'}")
        print("-" * 100)
        
        results = {}
        for impl_name, impl_func in implementations:
            try:
                result = impl_func(list_a, list_b)
                results[impl_name] = result
                status = "✓"
                print(f"{status} {impl_name:30} : {result if len(str(result)) < 60 else str(result)[:60] + '...'}")
            except Exception as e:
                results[impl_name] = f"ERROR: {str(e)[:50]}"
                print(f"✗ {impl_name:30} : ERROR - {str(e)[:50]}")
        
        # Verify all results match original
        original_result = results.get("Original (Nested Loop)")
        all_match = all(
            result == original_result 
            for name, result in results.items() 
            if not isinstance(result, str) or not result.startswith("ERROR")
        )
        
        print(f"Consistency: {'✓ All match' if all_match else '✗ Mismatch detected'}")


def run_performance_tests():
    """Run performance comparison tests."""
    import time
    
    print("\n" + "="*100)
    print("PERFORMANCE COMPARISON (Time in seconds)")
    print("="*100)
    
    # Create test data
    sizes = [100, 1000, 10000]
    
    for size in sizes:
        print(f"\nTest Size: {size} elements each")
        print("-" * 100)
        
        list_a = list(range(size))
        list_b = list(range(size // 2, size + size // 2))
        
        implementations = [
            ("Original (Nested Loop)", find_common),
            ("v2: Set Intersection", find_common_v2),
            ("v3: List Comprehension", find_common_v3),
            ("v5: Set with Order", find_common_v5),
            ("v10: Two-Pointer", find_common_v10),
        ]
        
        for impl_name, impl_func in implementations:
            start = time.time()
            for _ in range(10):  # Run 10 times
                result = impl_func(list_a, list_b)
            elapsed = time.time() - start
            
            print(f"{impl_name:30} : {elapsed:.6f}s")


if __name__ == "__main__":
    # Run comprehensive tests
    run_comparison_tests()
    
    # Run performance tests
    run_performance_tests()