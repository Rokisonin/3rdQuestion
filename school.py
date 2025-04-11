from abc import ABC, abstractmethod

class Student:
    def __init__(self, name, grades):
        self.__name = name
        self.__grades = grades  # encapsulated list of grades

    @property
    def name(self):
        return self.__name

    def average(self):
        return sum(self.__grades) / len(self.__grades)

    def gpa(self):
        return Student.grade_to_gpa(self.average())

    @staticmethod
    def grade_to_gpa(grade):
        if grade >= 90:
            return 4.0
        elif grade >= 80:
            return 3.0
        elif grade >= 70:
            return 2.0
        elif grade >= 60:
            return 1.0
        else:
            return 0.0

    def __str__(self):
        return f"{self.name} | Avg: {self.average():.2f} | GPA: {self.gpa():.1f}"

class SchoolBase(ABC):
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    @abstractmethod
    def display_report(self):
        pass

class SchoolOne(SchoolBase):
    def display_report(self):
        print(f"\n[School One Report - {self.school_name}]")
        for student in self.students:
            print(student)

class SchoolTwo(SchoolBase):
    def display_report(self):
        print(f"\n[School Two Report - {self.school_name}]")
        for student in self.students:
            print(student)
