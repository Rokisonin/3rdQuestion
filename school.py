from abc import ABC, abstractmethod

# Student class holds student data and grade operations
class Student:
    def __init__(self, name, grades):
        # Private name and grades (encapsulation)
        self.__name = name
        self.__grades = grades

    # Getter for name
    @property
    def name(self):
        return self.__name

    # Calculate average grade
    def average(self):
        return sum(self.__grades) / len(self.__grades)

    # Convert average to GPA using static method
    def gpa(self):
        return Student.grade_to_gpa(self.average())

    # Static method to convert a grade to a GPA scale
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

    # Dunder method for readable printout of the student
    def __str__(self):
        return f"{self.name} | Avg: {self.average():.2f} | GPA: {self.gpa():.1f}"

# Abstract base class for all schools
class SchoolBase(ABC):
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []  # Will contain Student objects (aggregation)

    # Add a student to the list
    def add_student(self, student):
        self.students.append(student)

    # Abstract method to enforce that derived classes implement reporting
    @abstractmethod
    def display_report(self):
        pass

# SchoolOne class inherits from SchoolBase
class SchoolOne(SchoolBase):
    def display_report(self):
        # Overridden method to display student report (polymorphism)
        print(f"\n[School One Report - {self.school_name}]")
        for student in self.students:
            print(student)

# SchoolTwo class also inherits from SchoolBase
class SchoolTwo(SchoolBase):
    def display_report(self):
        # Same structure, different school (polymorphism)
        print(f"\n[School Two Report - {self.school_name}]")
        for student in self.students:
            print(student)
