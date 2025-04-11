from school import Student, SchoolOne, SchoolTwo

# Create students
s1 = Student("Alice", [88, 92, 95])
s2 = Student("Bob", [75, 80, 70])
s3 = Student("Charlie", [60, 58, 65])
s4 = Student("Daisy", [95, 98, 93])

# Create schools
school1 = SchoolOne("Sunrise High")
school2 = SchoolTwo("Moonlight Academy")

# Assign students
school1.add_student(s1)
school1.add_student(s2)

school2.add_student(s3)
school2.add_student(s4)

# Show reports
school1.display_report()
school2.display_report()
