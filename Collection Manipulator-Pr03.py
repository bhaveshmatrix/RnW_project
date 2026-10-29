
print("Welcome to the Student Data Organizer!")

student = []

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nEnter student details:")

        student_id = input("Student ID: ")

        if any(s[0] == student_id for s in student):
            print("Student ID already exists!")
            continue

        Name = input("Name: ")
        Age = int(input("Age: "))
        Grade = input("Grade: ")
        Date = input("Date of Birth (YYYY-MM-DD): ")
        Subjects = input("Subjects (comma-separated): ")

        student.append(
            (student_id, Name, Age, Grade, Date, Subjects)
        )

        print("\nStudent added successfully!")

    elif choice == 2:
        print("\n--- Display All Students ---")

        if len(student) == 0:
            print("No students found!")
        else:
            for s in student:
                print(
                    f"Student ID: {s[0]} | "
                    f"Name: {s[1]} | "
                    f"Age: {s[2]} | "
                    f"Grade: {s[3]} | "
                    f"Subjects: {s[5]}"
                )

    elif choice == 3:
        student_id = input("Enter Student ID to update: ")

        for i, s in enumerate(student):
            if s[0] == student_id:
                print("Leave blank to keep the old value.")

                Name = input(f"Name ({s[1]}): ") or s[1]
                Age_input = input(f"Age ({s[2]}): ")
                Grade = input(f"Grade ({s[3]}): ") or s[3]
                Date = input(f"Date of Birth ({s[4]}): ") or s[4]
                Subjects = input(f"Subjects ({s[5]}): ") or s[5]

                try:
                    Age = int(Age_input) if Age_input else s[2]
                except ValueError:
                    print("Invalid age. Keeping old age.")
                    Age = s[2]

                student[i] = (
                    student_id, Name, Age, Grade, Date, Subjects
                )

                print("Student updated successfully!")
                break
        else:
            print("Student not found!")

    elif choice == 4:
        student_id = input("Enter Student ID to delete: ")

        for s in student:
            if s[0] == student_id:
                student.remove(s)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found!")

    elif choice == 5:
        print("\n--- Subjects Offered ---")
        print("Math")
        print("Science")
        print("English")

    elif choice == 6:
        print("Thank you for using Student Data Organizer!")
        break

    else:
        print("Invalid choice! Please select 1 to 6.")
