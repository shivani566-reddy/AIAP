def discount(price: float, category: str) -> float:
   
    # Define discount rates for student category
    student_discounts = {
        'high': 0.9,   # 10% discount for price > 1000
        'low': 0.95    # 5% discount for price <= 1000
    }
    
    # Define discount rates for regular category
    regular_discounts = {
        'high': 0.85,  # 15% discount for price > 2000
        'low': 1.0     # No discount for price <= 2000
    }
    
    # Determine which discount structure to use
    discounts = student_discounts if category == "student" else regular_discounts
    
    # Get the threshold price for determining discount level
    threshold = 1000 if category == "student" else 2000
    
    # Select appropriate discount rate based on price threshold
    discount_rate = discounts['high'] if price > threshold else discounts['low']
    
    # Calculate and return discounted price
    return price * discount_rate


# Alternative implementation using dictionary mapping
def discount_v2(price: float, category: str) -> float:
    """
    Calculate discounted price using dictionary-based approach.
    
    Parameters
    ----------
    price : float
        The original price of the item.
    category : str
        The customer category ('student' or other).
    
    Returns
    -------
    float
        The discounted price.
    """
    # Define pricing rules as a nested dictionary
    pricing_rules = {
        "student": [(1000, 0.9), (float('inf'), 0.95)],
        "regular": [(2000, 0.85), (float('inf'), 1.0)]
    }
    
    # Get rules for the given category
    rules = pricing_rules.get(category, pricing_rules["regular"])
    
    # Find applicable discount rate
    discount_rate = next(rate for threshold, rate in rules if price > threshold)
    
    # Return discounted price
    return price * discount_rate


# Alternative implementation using lambda functions
def discount_v3(price: float, category: str) -> float:
    """
    Calculate discounted price using functional programming approach.
    
    Parameters
    ----------
    price : float
        The original price of the item.
    category : str
        The customer category ('student' or other).
    
    Returns
    -------
    float
        The discounted price.
    """
    # Define discount logic as lambda functions
    student_discount = lambda p: p * 0.9 if p > 1000 else p * 0.95
    regular_discount = lambda p: p * 0.85 if p > 2000 else p
    
    # Select appropriate discount function
    discount_func = student_discount if category == "student" else regular_discount
    
    # Apply and return discounted price
    return discount_func(price)


# Alternative implementation using ternary operators
def discount_v4(price: float, category: str) -> float:
    """
    Calculate discounted price using conditional ternary operators.
    
    Parameters
    ----------
    price : float
        The original price of the item.
    category : str
        The customer category ('student' or other).
    
    Returns
    -------
    float
        The discounted price.
    """
    # Apply discount using nested ternary operators
    return (
        price * 0.9 if category == "student" and price > 1000
        else price * 0.95 if category == "student"
        else price * 0.85 if price > 2000
        else price
    )


# Alternative implementation using match-case (Python 3.10+)
def discount_v5(price: float, category: str) -> float:
    """
    Calculate discounted price using match-case pattern matching.
    
    Parameters
    ----------
    price : float
        The original price of the item.
    category : str
        The customer category ('student' or other).
    
    Returns
    -------
    float
        The discounted price.
    """
    # Determine price range
    is_high_price_student = category == "student" and price > 1000
    is_high_price_regular = category != "student" and price > 2000
    
    # Apply discounts based on conditions
    match (category, is_high_price_student, is_high_price_regular):
        case ("student", True, _):
            return price * 0.9
        case ("student", False, _):
            return price * 0.95
        case (_, _, True):
            return price * 0.85
        case _:
            return price


# Test cases
def run_tests():
    """Run comprehensive test cases for all implementations."""
    
    test_cases = [
        ("student", 500, 475.0),      # Student, low price: 5% discount
        ("student", 1500, 1350.0),    # Student, high price: 10% discount
        ("regular", 1500, 1500.0),    # Regular, low price: no discount
        ("regular", 2500, 2125.0),    # Regular, high price: 15% discount
        ("student", 1000, 950.0),     # Boundary: student at 1000
        ("regular", 2000, 2000.0),    # Boundary: regular at 2000
    ]
    
    print("="*70)
    print("Testing All Discount Implementations")
    print("="*70)
    
    implementations = [
        ("Original", discount),
        ("Dictionary-based", discount_v2),
        ("Lambda-based", discount_v3),
        ("Ternary-based", discount_v4),
        ("Match-case-based", discount_v5),
    ]
    
    for impl_name, impl_func in implementations:
        print(f"\n{impl_name} Implementation:")
        print("-" * 70)
        all_pass = True
        
        for category, price, expected in test_cases:
            try:
                result = impl_func(price, category)
                status = "✓ PASS" if result == expected else "✗ FAIL"
                
                if result != expected:
                    all_pass = False
                
                print(f"{status} | Category: {category:8} | Price: ${price:7} | "
                      f"Result: ${result:7} | Expected: ${expected:7}")
            except Exception as e:
                print(f"✗ ERROR | {e}")
                all_pass = False
        
        print(f"Status: {'All tests passed ✓' if all_pass else 'Some tests failed ✗'}")
    
    print("\n" + "="*70)


if __name__ == "__main__":
    run_tests()