students = {
    "Afzal": {"age": 20, "grade": "A"},
    "Rahul": {"age": 21, "grade": "B"},
    "Sara": {"age": 22, "grade": "A+"}
}

name = input("Enter student name: ")
if name in students:
    print("Details:", students[name])
else:
    print("Student not found.")
