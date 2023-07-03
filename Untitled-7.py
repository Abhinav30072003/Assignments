def get_student_entries():
    student_records = []
    roll_numbers = set()

    while True:
        name = input("Enter student name (or 'exit' to finish): ")
        if name.lower() == "exit":
            break

        roll_number = input("Enter roll number: ")
        if roll_number in roll_numbers:
            print("Roll number already exists. Please enter a unique roll number.")
            continue
        else:
            roll_numbers.add(roll_number)

        percentage = float(input("Enter percentage: "))
        year = input("Enter year: ")

        student_records.append({
            "name": name,
            "roll_number": roll_number,
            "percentage": percentage,
            "year": year
        })
    return student_records
students = get_student_entries()
print("\nStudent Entries:")
for student in students:
    print("Name:", student["name"])
    print("Roll Number:", student["roll_number"])
    print("Percentage:", student["percentage"])
    print("Year:", student["year"])
    print()
