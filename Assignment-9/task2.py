class SruStudent:
    """
    Class representing a student at SRU.

    Attributes:
        name (str): The name of the student.
        roll_no (int): The roll number of the student.
        hostel_status (bool): Indicates if the student is in a hostel.
    """

    def __init__(self, name: str, roll_no: int, hostel_status: bool):
        """
        Initializes a new instance of SruStudent.

        Args:
            name (str): The name of the student.
            roll_no (int): The roll number of the student.
            hostel_status (bool): The hostel status of the student.
        """
        self.name = name  # Assign the provided name to the student instance
        self.roll_no = roll_no  # Assign the provided roll number to the student instance
        self.hostel_status = hostel_status  # Assign the provided hostel status to the student instance

    def fee_update(self, amount: float) -> None:
        """
        Update the fee status of the student.

        Args:
            amount (float): The amount to be added to the fee.
        """
        # Print a message indicating the fee has been updated
        print(f"Fee updated by {amount} for {self.name}.")  # Confirm the fee update for the student

    def display_details(self) -> None:
        """
        Display the details of the student.
        """
        # Print the student's name
        print(f"Name: {self.name}")
        # Print the student's roll number
        print(f"Roll No: {self.roll_no}")
        # Print whether the student is in a hostel
        print(f"Hostel Status: {'Yes' if self.hostel_status else 'No'}")


# Example usage
if __name__ == "__main__":
    student = SruStudent("Alice", 101, True)  # Create a new instance of SruStudent
    student.display_details()  # Call the method to display student details
    student.fee_update(1500.00)  # Call the method to update the fee