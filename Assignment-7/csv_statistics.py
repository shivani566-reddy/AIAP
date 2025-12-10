"""
Python program to read a CSV file and calculate mean, min, and max statistics.
This program uses user input to get the CSV file path and column selection.
"""

import csv
import os
import statistics


def get_csv_file_path():
    """
    Get CSV file path from user input.
    
    Returns:
        str: Path to the CSV file
    """
    while True:
        file_path = input("Enter the path to the CSV file: ").strip()
        
        # Remove quotes if user added them
        file_path = file_path.strip('"').strip("'")
        
        if os.path.exists(file_path):
            if file_path.lower().endswith('.csv'):
                return file_path
            else:
                print("Warning: File doesn't have .csv extension. Proceeding anyway...")
                return file_path
        else:
            print(f"File not found: {file_path}")
            retry = input("Would you like to try again? (yes/no): ").strip().lower()
            if retry != 'yes':
                return None


def read_csv_file(file_path):
    """
    Read CSV file and return data as a list of dictionaries.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        tuple: (headers, rows) where rows is a list of dictionaries
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            headers = csv_reader.fieldnames
            rows = list(csv_reader)
            return headers, rows
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None, None


def display_csv_preview(headers, rows, num_rows=5):
    """
    Display a preview of the CSV file structure.
    
    Args:
        headers (list): Column headers
        rows (list): CSV rows
        num_rows (int): Number of rows to preview
    """
    print("\n" + "="*60)
    print("CSV FILE PREVIEW")
    print("="*60)
    print(f"Columns: {', '.join(headers)}")
    print(f"Total rows: {len(rows)}")
    print(f"\nFirst {min(num_rows, len(rows))} rows:")
    print("-"*60)
    
    for i, row in enumerate(rows[:num_rows], 1):
        print(f"Row {i}:")
        for header in headers:
            print(f"  {header}: {row[header]}")
        print()


def get_column_choice(headers):
    """
    Get column selection from user input.
    
    Args:
        headers (list): List of column headers
        
    Returns:
        str: Selected column name
    """
    print("\nAvailable columns:")
    for i, header in enumerate(headers, 1):
        print(f"  {i}. {header}")
    
    while True:
        try:
            choice = input("\nEnter column number or name to analyze: ").strip()
            
            # Try to parse as number
            if choice.isdigit():
                col_index = int(choice) - 1
                if 0 <= col_index < len(headers):
                    return headers[col_index]
                else:
                    print(f"Invalid column number. Please enter a number between 1 and {len(headers)}.")
            # Try to match by name
            elif choice in headers:
                return choice
            else:
                print(f"Column '{choice}' not found. Please enter a valid column name or number.")
        except ValueError:
            print("Invalid input. Please enter a number or column name.")


def extract_numeric_values(rows, column_name):
    """
    Extract numeric values from a specific column.
    
    Args:
        rows (list): List of dictionaries (CSV rows)
        column_name (str): Name of the column to extract
        
    Returns:
        list: List of numeric values
    """
    numeric_values = []
    
    for i, row in enumerate(rows, 1):
        try:
            value = row[column_name].strip()
            if value:  # Skip empty values
                numeric_value = float(value)
                numeric_values.append(numeric_value)
        except ValueError:
            print(f"Warning: Row {i} has non-numeric value '{row[column_name]}' in column '{column_name}'. Skipping.")
        except KeyError:
            print(f"Error: Column '{column_name}' not found in row {i}.")
            return []
    
    return numeric_values


def calculate_statistics(values):
    """
    Calculate mean, min, and max for a list of numeric values.
    
    Args:
        values (list): List of numeric values
        
    Returns:
        dict: Dictionary containing mean, min, max, and count
    """
    if not values:
        return {
            'mean': None,
            'min': None,
            'max': None,
            'count': 0
        }
    
    return {
        'mean': statistics.mean(values),
        'min': min(values),
        'max': max(values),
        'count': len(values)
    }


def display_statistics(column_name, stats):
    """
    Display calculated statistics.
    
    Args:
        column_name (str): Name of the analyzed column
        stats (dict): Dictionary containing statistics
    """
    print("\n" + "="*60)
    print("STATISTICS RESULTS")
    print("="*60)
    print(f"Column: {column_name}")
    print(f"Valid numeric values: {stats['count']}")
    
    if stats['count'] > 0:
        print(f"\nMean (Average): {stats['mean']:.2f}")
        print(f"Minimum: {stats['min']:.2f}")
        print(f"Maximum: {stats['max']:.2f}")
    else:
        print("\nNo valid numeric values found in this column.")
    
    print("="*60)


def main():
    """
    Main function to run the CSV statistics calculator.
    """
    print("="*60)
    print("CSV STATISTICS CALCULATOR")
    print("="*60)
    print("This program reads a CSV file and calculates mean, min, and max")
    print("for a selected numeric column.\n")
    
    # Get CSV file path from user
    file_path = get_csv_file_path()
    if not file_path:
        print("Exiting...")
        return
    
    # Read CSV file
    print(f"\nReading CSV file: {file_path}")
    headers, rows = read_csv_file(file_path)
    
    if headers is None or rows is None:
        print("Failed to read CSV file. Exiting...")
        return
    
    if not rows:
        print("CSV file is empty. Exiting...")
        return
    
    # Display preview
    display_csv_preview(headers, rows)
    
    # Get column choice from user
    column_name = get_column_choice(headers)
    
    # Extract numeric values from selected column
    print(f"\nExtracting numeric values from column '{column_name}'...")
    numeric_values = extract_numeric_values(rows, column_name)
    
    if not numeric_values:
        print(f"No valid numeric values found in column '{column_name}'.")
        return
    
    # Calculate statistics
    print(f"Calculating statistics for {len(numeric_values)} values...")
    stats = calculate_statistics(numeric_values)
    
    # Display results
    display_statistics(column_name, stats)


if __name__ == "__main__":
    main()






