import pandas as pd
from typing import Dict, Union
import os

def read_csv_and_calculate_stats(file_path: str) -> Dict[str, Dict[str, float]]:
    """
    Read a CSV file and calculate mean, min, and max for numeric columns.
    
    Parameters
    ----------
    file_path : str
        The path to the CSV file to read.
    
    Returns
    -------
    Dict[str, Dict[str, float]]
        A dictionary where keys are column names and values are dictionaries
        containing 'mean', 'min', and 'max' statistics.
    
    Raises
    ------
    FileNotFoundError
        If the CSV file does not exist at the specified path.
    ValueError
        If the CSV file is empty or contains no numeric columns.
    
    Examples
    --------
    >>> stats = read_csv_and_calculate_stats('data.csv')
    >>> print(stats['age'])
    {'mean': 30.5, 'min': 18, 'max': 65}
    """
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Read the CSV file using pandas
    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        raise ValueError("CSV file is empty")
    except Exception as e:
        raise ValueError(f"Error reading CSV file: {str(e)}")
    
    # Check if dataframe is empty
    if df.empty:
        raise ValueError("CSV file contains no data")
    
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=['number'])
    
    # Check if there are numeric columns
    if numeric_df.empty:
        raise ValueError("CSV file contains no numeric columns")
    
    # Calculate statistics for each numeric column
    stats = {}
    for column in numeric_df.columns:
        stats[column] = {
            'mean': round(numeric_df[column].mean(), 2),
            'min': round(numeric_df[column].min(), 2),
            'max': round(numeric_df[column].max(), 2),
            'median': round(numeric_df[column].median(), 2),
            'std': round(numeric_df[column].std(), 2),
            'count': int(numeric_df[column].count())
        }
    
    return stats


def display_statistics(stats: Dict[str, Dict[str, float]]) -> None:
    """
    Display statistics in a formatted manner.
    
    Parameters
    ----------
    stats : Dict[str, Dict[str, float]]
        Dictionary containing statistics for each column.
    
    Returns
    -------
    None
    
    Examples
    --------
    >>> stats = {'age': {'mean': 30.5, 'min': 18, 'max': 65}}
    >>> display_statistics(stats)
    """
    print("\n" + "="*70)
    print("CSV Statistics Report")
    print("="*70)
    
    for column, values in stats.items():
        print(f"\nColumn: {column}")
        print(f"  Count:  {values['count']}")
        print(f"  Mean:   {values['mean']}")
        print(f"  Min:    {values['min']}")
        print(f"  Max:    {values['max']}")
        print(f"  Median: {values['median']}")
        print(f"  Std:    {values['std']}")
    
    print("\n" + "="*70)


def create_sample_csv(file_path: str) -> None:
    """
    Create a sample CSV file for testing.
    
    Parameters
    ----------
    file_path : str
        The path where the sample CSV file will be created.
    
    Returns
    -------
    None
    
    Examples
    --------
    >>> create_sample_csv('sample_data.csv')
    """
    sample_data = {
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'age': [25, 30, 35, 28, 32],
        'salary': [50000, 60000, 75000, 55000, 70000],
        'experience': [2, 5, 8, 3, 6]
    }
    
    # Create dataframe from sample data
    df = pd.DataFrame(sample_data)
    # Write to CSV file
    df.to_csv(file_path, index=False)
    print(f"Sample CSV file created: {file_path}")


def export_stats_to_csv(stats: Dict[str, Dict[str, float]], output_path: str) -> None:
    """
    Export statistics to a CSV file.
    
    Parameters
    ----------
    stats : Dict[str, Dict[str, float]]
        Dictionary containing statistics for each column.
    output_path : str
        The path where the statistics CSV will be saved.
    
    Returns
    -------
    None
    """
    # Convert stats dictionary to list of dictionaries
    stats_list = []
    for column, values in stats.items():
        row = {'Column': column, **values}
        stats_list.append(row)
    
    # Create dataframe from stats list
    stats_df = pd.DataFrame(stats_list)
    # Export to CSV
    stats_df.to_csv(output_path, index=False)
    print(f"Statistics exported to: {output_path}")


def get_user_input() -> str:
    """
    Get CSV file path from user input with validation.
    
    Returns
    -------
    str
        The path to the CSV file provided by the user.
    """
    while True:
        file_path = input("Enter the path to your CSV file: ").strip()
        if file_path:
            return file_path
        print("Please enter a valid file path.")


def main():
    """
    Main function to demonstrate CSV reading and statistics calculation.
    
    Returns
    -------
    None
    """
    print("CSV Statistics Calculator")
    print("-" * 70)
    
    # Ask user for choice
    print("\n1. Use sample data")
    print("2. Use your own CSV file")
    choice = input("Choose option (1 or 2): ").strip()
    
    if choice == '1':
        # Create and use sample CSV file
        sample_file = "sample_data.csv"
        create_sample_csv(sample_file)
        file_to_process = sample_file
    elif choice == '2':
        # Get user input for file path
        file_to_process = get_user_input()
    else:
        print("Invalid choice. Using sample data.")
        sample_file = "sample_data.csv"
        create_sample_csv(sample_file)
        file_to_process = sample_file
    
    # Read CSV and calculate statistics
    try:
        print(f"\nProcessing file: {file_to_process}")
        statistics = read_csv_and_calculate_stats(file_to_process)
        
        # Display statistics
        display_statistics(statistics)
        
        # Ask if user wants to export statistics
        export_choice = input("Do you want to export statistics to CSV? (yes/no): ").strip().lower()
        if export_choice == 'yes':
            output_file = "statistics_report.csv"
            export_stats_to_csv(statistics, output_file)
        
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
    finally:
        # Clean up: remove sample files if they were created
        if choice == '1' and os.path.exists("sample_data.csv"):
            cleanup = input("Clean up sample file? (yes/no): ").strip().lower()
            if cleanup == 'yes':
                os.remove("sample_data.csv")
                print("Sample file removed.")


if __name__ == "__main__":
    main()