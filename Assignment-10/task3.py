class emp:
    """
    A class to represent an employee with salary management capabilities.
    
    Attributes
    ----------
    n : str
        The name of the employee.
    s : float
        The current salary of the employee.
    
    Methods
    -------
    inc(p):
        Increase the salary by a given percentage.
    pr():
        Print the employee details.
    """
    
    def __init__(self, n: str, s: float):
        """
        Initialize an emp object.
        
        Parameters
        ----------
        n : str
            The name of the employee.
        s : float
            The initial salary of the employee.
        """
        # Store employee name
        self.n = n
        # Store employee salary
        self.s = s
    
    def inc(self, p: float) -> None:
        """
        Increase the employee's salary by a given percentage.
        
        Parameters
        ----------
        p : float
            The percentage to increase the salary by.
        
        Returns
        -------
        None
        """
        # Calculate new salary by adding percentage increment
        self.s = self.s * (1 + p / 100)
    
    def pr(self) -> None:
        """
        Display the employee details.
        
        Returns
        -------
        None
        """
        # Print employee information
        print(f"emp: {self.n} salary: {self.s}")


# Alternative Implementation v2: Using Addition Instead of Multiplication
class emp_v2:
    """Alternative implementation using addition."""
    
    def __init__(self, n: str, s: float):
        self.n = n
        self.s = s
    
    def inc(self, p: float) -> None:
        # Add increment to salary
        self.s += self.s * p / 100
    
    def pr(self) -> None:
        print(f"emp: {self.n} salary: {self.s}")


# Alternative Implementation v3: Using Augmented Assignment
class emp_v3:
    """Alternative implementation using augmented assignment."""
    
    def __init__(self, n: str, s: float):
        self.n = n
        self.s = s
    
    def inc(self, p: float) -> None:
        # Augmented assignment operator
        self.s += (self.s * p) / 100
    
    def pr(self) -> None:
        print(f"emp: {self.n} salary: {self.s}")


# Alternative Implementation v4: Using Apply Decorator Pattern
class emp_v4:
    """Alternative implementation with method chaining capability."""
    
    def __init__(self, n: str, s: float):
        self.n = n
        self.s = s
    
    def inc(self, p: float) -> 'emp_v4':
        # Return self for method chaining
        self.s = self.s + self.s * p / 100
        return self
    
    def pr(self) -> None:
        print(f"emp: {self.n} salary: {self.s}")
        return self


# Alternative Implementation v5: Using Formula Approach
class emp_v5:
    """Alternative implementation with formula-based calculation."""
    
    def __init__(self, n: str, s: float):
        self.n = n
        self.s = s
    
    def inc(self, p: float) -> None:
        # Calculate using formula: new_salary = salary * (1 + p/100)
        multiplier = 1 + (p / 100)
        self.s = self.s * multiplier
    
    def pr(self) -> None:
        print(f"emp: {self.n} salary: {self.s}")


# Alternative Implementation v6: Using Helper Method
class emp_v6:
    """Alternative implementation with helper method."""
    
    def __init__(self, n: str, s: float):
        self.n = n
        self.s = s
    
    def _calculate_increment(self, current_salary: float, percentage: float) -> float:
        """Calculate increment amount."""
        return current_salary + (current_salary * percentage / 100)
    
    def inc(self, p: float) -> None:
        self.s = self._calculate_increment(self.s, p)
    
    def pr(self) -> None:
        print(f"emp: {self.n} salary: {self.s}")


# Alternative Implementation v7: Using Property Decorator
class emp_v7:
    """Alternative implementation using property decorator."""
    
    def __init__(self, n: str, s: float):
        self._n = n
        self._s = s
    
    @property
    def n(self):
        return self._n
    
    @property
    def s(self):
        return self._s
    
    @s.setter
    def s(self, value: float):
        self._s = value
    
    def inc(self, p: float) -> None:
        self.s = self.s + self.s * p / 100
    
    def pr(self) -> None:
        print(f"emp: {self.n} salary: {self.s}")


# Alternative Implementation v8: Using Dictionary Storage
class emp_v8:
    """Alternative implementation using dictionary storage."""
    
    def __init__(self, n: str, s: float):
        self.data = {'n': n, 's': s}
    
    def __getattr__(self, name: str):
        if name in self.data:
            return self.data[name]
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
    
    def __setattr__(self, name: str, value):
        if name == 'data':
            super().__setattr__(name, value)
        else:
            if not hasattr(self, 'data'):
                super().__setattr__('data', {})
            self.data[name] = value
    
    def inc(self, p: float) -> None:
        current = self.data['s']
        self.data['s'] = current + current * p / 100
    
    def pr(self) -> None:
        print(f"emp: {self.data['n']} salary: {self.data['s']}")


# Alternative Implementation v9: Using Static Method for Calculation
class emp_v9:
    """Alternative implementation with static method for calculation."""
    
    def __init__(self, n: str, s: float):
        self.n = n
        self.s = s
    
    @staticmethod
    def calculate_new_salary(salary: float, percentage: float) -> float:
        """Calculate new salary after increment."""
        return salary + salary * percentage / 100
    
    def inc(self, p: float) -> None:
        self.s = self.calculate_new_salary(self.s, p)
    
    def pr(self) -> None:
        print(f"emp: {self.n} salary: {self.s}")


# Alternative Implementation v10: Using Lambda Function
class emp_v10:
    """Alternative implementation using lambda function."""
    
    # Define increment calculation as lambda
    calculate_increment = lambda salary, p: salary + salary * p / 100
    
    def __init__(self, n: str, s: float):
        self.n = n
        self.s = s
    
    def inc(self, p: float) -> None:
        self.s = emp_v10.calculate_increment(self.s, p)
    
    def pr(self) -> None:
        print(f"emp: {self.n} salary: {self.s}")


# Comprehensive Testing
def run_comparison_tests():
    """Run comprehensive tests for all implementations."""
    
    test_data = [
        ("Alice", 50000, 10),
        ("Bob", 60000, 5),
        ("Charlie", 75000, 15),
    ]
    
    implementations = [
        ("Original (Refactored)", emp),
        ("v2: Addition Assignment", emp_v2),
        ("v3: Augmented Assignment", emp_v3),
        ("v4: Method Chaining", emp_v4),
        ("v5: Formula Based", emp_v5),
        ("v6: Helper Method", emp_v6),
        ("v7: Property Decorator", emp_v7),
        ("v8: Dictionary Storage", emp_v8),
        ("v9: Static Method", emp_v9),
        ("v10: Lambda Function", emp_v10),
    ]
    
    print("="*80)
    print("Employee Class - Multiple Implementations Comparison")
    print("="*80)
    
    for impl_name, impl_class in implementations:
        print(f"\n{impl_name}:")
        print("-" * 80)
        
        try:
            for name, salary, percentage in test_data:
                # Create employee
                employee = impl_class(name, salary)
                # Display initial
                employee.pr()
                # Apply increment
                employee.inc(percentage)
                # Display after increment
                employee.pr()
            print("✓ All tests passed")
        except Exception as e:
            print(f"✗ Error: {e}")


def demonstrate_different_scenarios():
    """Demonstrate different usage scenarios."""
    
    print("\n" + "="*80)
    print("Different Usage Scenarios")
    print("="*80)
    
    # Scenario 1: Single employee with multiple increments
    print("\nScenario 1: Single Employee with Multiple Increments")
    print("-" * 80)
    employee1 = emp("John", 50000)
    employee1.pr()
    employee1.inc(5)
    employee1.pr()
    employee1.inc(10)
    employee1.pr()
    
    # Scenario 2: Multiple employees
    print("\nScenario 2: Multiple Employees")
    print("-" * 80)
    employees = [
        emp("Alice", 55000),
        emp("Bob", 60000),
        emp("Charlie", 65000),
    ]
    
    for employee in employees:
        employee.pr()
        employee.inc(8)
        employee.pr()
    
    # Scenario 3: Processing employee list
    print("\nScenario 3: Processing Employee List with Different Increments")
    print("-" * 80)
    increments = [
        ("Employee1", 40000, 5),
        ("Employee2", 45000, 10),
        ("Employee3", 50000, 15),
    ]
    
    for name, salary, percent in increments:
        emp_obj = emp(name, salary)
        print(f"Before: ", end="")
        emp_obj.pr()
        emp_obj.inc(percent)
        print(f"After {percent}% increment: ", end="")
        emp_obj.pr()


def compare_output():
    """Compare output of all implementations to ensure they're identical."""
    
    print("\n" + "="*80)
    print("Output Verification - All Implementations Produce Same Result")
    print("="*80)
    
    test_name = "TestEmployee"
    test_salary = 50000
    test_percent = 10
    
    implementations = [
        ("Original", emp),
        ("v2", emp_v2),
        ("v3", emp_v3),
        ("v5", emp_v5),
        ("v6", emp_v6),
        ("v9", emp_v9),
        ("v10", emp_v10),
    ]
    
    print(f"\nInitial: Name='{test_name}', Salary={test_salary}, Increment={test_percent}%\n")
    
    outputs = {}
    for impl_name, impl_class in implementations:
        emp_obj = impl_class(test_name, test_salary)
        emp_obj.inc(test_percent)
        
        # Calculate expected result
        expected = test_salary + test_salary * test_percent / 100
        actual = emp_obj.s
        
        status = "✓ MATCH" if abs(actual - expected) < 0.01 else "✗ MISMATCH"
        outputs[impl_name] = actual
        
        print(f"{impl_name:20} : Final Salary = {actual:10.2f} | {status}")


if __name__ == "__main__":
    # Run comparison tests
    run_comparison_tests()
    
    # Demonstrate different scenarios
    demonstrate_different_scenarios()
    
    # Compare outputs
    compare_output()