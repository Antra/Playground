students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    student_titlecase = get_students_titlecase()
    print(student_titlecase)


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file!")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file!")


# Demonstration stuff - get a variable number of arguments (returns a list)
def var_args(name, *args):
    print(name)
    print(args)


# Demonstration stuff - get a variable number of arguments with keywords (returns a dictionary)
def var_kwargs(name, **kwargs):
    print(name)
    print(kwargs["description"], kwargs["feedback"])


# Demonstration stuff - try the variable arguments
var_args("Mark", "Loves Python", None, "Hello", True)
var_kwargs("Mark", description="Loves Python",
           feedback=None, pluralsight_subscriber=True)

print("running program!")
read_file()
print_students_titlecase()

student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")

add_student(student_name, student_id)
save_file(student_name)
