
def classify_age(age: int) -> str:
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teen"
    elif age <= 64:
        return "Adult"
    else:
        return "Senior"
    # The input and print statements should be outside the classify_age function

if __name__ == "__main__":
    age = int(input("Enter age to classify: ").strip())
    print(classify_age(age))
    
    