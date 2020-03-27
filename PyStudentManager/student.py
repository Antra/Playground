students = []


class Student:

    school_name = "Springfield Elementary"

    def __init__(self, name, student_id=789, last_name="test"):
        self.name = name
        self.student_id = student_id
        self.last_name = last_name
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalise(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name
