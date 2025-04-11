from school import Student, SchoolOne, SchoolTwo

# Create 4 student objects with their respective grade lists
s1 = Student("Alice", [88, 92, 95])      # High achiever
s2 = Student("Bob", [75, 80, 70])        # Average grades
s3 = Student("Charlie", [60, 58, 65])    # Below average
s4 = Student("Daisy", [95, 98, 93])      # Excellent student

# Create two school instances using different school classes
school1 = SchoolOne("Sunrise High")
school2 = SchoolTwo("Moonlight Academy")

# Assign students to their respective schools (Aggregation)
school1.add_student(s1)
school1.add_student(s2)

school2.add_student(s3)
school2.add_student(s4)

# Call display_report (polymorphic method) on each school
school1.display_report()
school2.display_report()
