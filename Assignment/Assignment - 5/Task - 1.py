# Step 1: Create a dictionary of student names and their marks
student_marks = {
    'Alice': 85,
    'Bob': 90,
    'Charlie': 78,
    'David': 92,
    'Eve': 88
}

# Step 2: Ask the user for a student's name
student_name = input("Enter the student's name: ")

# Step 3: Retrieve and display the corresponding marks
if student_name in student_marks:
    print(f"{student_name}'s marks are: {student_marks[student_name]}")
else:
    print("Student not found. Please check the name and try again.")
