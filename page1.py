import csv

# File to store results
filename = "results.csv"

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = []
    for i in range(3):  # 3 subjects
        mark = int(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)
    total = sum(marks)
    avg = total / 3
    grade = "A" if avg >= 75 else "B" if avg >= 50 else "C"
    
    # Save to CSV
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, *marks, total, avg, grade])
    
    print("✅ Student record added successfully!")

def view_students():
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            print("\nRoll | Name | Marks | Total | Avg | Grade")
            print("-"*50)
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("No records found. Please add a student first.")

# Main menu
while True:
    print("\n--- Student Result Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice, try again!")
