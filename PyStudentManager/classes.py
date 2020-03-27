# the simplest possible class - but essentially it does nothing
class testClass:
    pass


students = []


class basicStudent:
    # the self part refers to the instance of the class; it doesn't have to be passed when calling the method, it'll be inferred from the class instance itself
    # using 'self' is the way to refer to the class from within the class; so if we want to call the same function again, we can call self.add_student()
    # it is akin to 'this' in other languages
    def add_student(self, name, student_id=332):
        student = {"name": name, "student_id": student_id}
        students.append(student)


student = basicStudent()
student.add_student("Mark")
print(students)


# this class has a constructor method (__init__)
# and a definition of __str__ (so it returns "Student" instead of a memory location), the __str_ is called if the class instance is printed
class constructorStudent:
    def __init__(self, name, student_id=456):
        student = {"name": name, "student_id": student_id}
        students.append(student)

    def __str__(self):
        return "constructorStudent"


# this passes an argument to the constructor method
james = constructorStudent("James")
print(students)
print(james)


# this class is more advanced as has instance attributes (tied to 'self')
# the class also has class attributes (not tied to an instance, but shared for them all) - they can be printed directly from the class as well
class Student:

    school_name = "Springfield Elementary"

    def __init__(self, name, student_id=789):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalise(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


jessica = Student("Jessica")
print(jessica)
print(jessica.school_name)
print(Student.school_name)


# Inheritance and Polymorphism
# When there are two similar classes; such as a Student and a Highschool Student, we can inherit the Student behaviour into the Highschool
# We inherit a class by passing the parent's name inside the parenthesis; then we can override the inherited behaviour inside the new class definition
# and we can of course add new methods, new instance/class attributes etc.
# Here the 'Student' is the Parent class, whereas the 'HighSchoolStudent' is a Derived class - derived classes has access to all methods of its parent class
# Using 'super()' keyword we can override the parent method and still execute it
class HighSchoolStudent(Student):
    school_name = "Springfield High School"

    def get_school_name(self):
        return "This is a High School student!"

    def get_name_capitalise(self):
        # super() executes the method from the parent class
        original_value = super().get_name_capitalise()
        return original_value + "-HS"


jim = HighSchoolStudent("jim")
print(jim.get_name_capitalise())
print(jim.get_school_name())
