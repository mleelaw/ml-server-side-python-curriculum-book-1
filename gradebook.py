# initialize and empty directory
student_grades = {}


# function to add a student and grade to dictionary
def add_student(name, grade):
    student_grades[name] = grade
    print(f"{name} scored a {grade}")


# removes students from dictionary
def remove_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been removed")

    else:
        print(f"{name} not found!")


# f8nction to display student list
def displaystudents():

    print("Student List")
    for name, grade in student_grades.items():
        print(f"student: {name} - grade: {grade}")


# function to update a students grade
def update_grade(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} new grade is {grade}")


add_student("mlee", 45)
add_student("abigail", 95)

update_grade("mlee", 100)


# function find a students grade
def find_grade(name):
    if name in student_grades:
        print(f"Student found. Grade: {student_grades[name]}")
    else:
        print(f"Student not found")


# function to find average of grades
def average_grade():
    grades = []
    for name, grade in student_grades.items():
        grades.append(grade)
    if grades:
        num_students = len(grades)
        average = sum(grades) / num_students
        print(f"average: {average}")
    else:
        print("no student grades found")


displaystudents()

find_grade("mlee")

find_grade("abigail")

average_grade()
