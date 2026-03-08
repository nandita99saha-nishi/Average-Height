# Take input as comma-separated values
Student_heights = input("Input a list of student heights: ").split(",")

# Convert each string element into an integer
for n in range(len(Student_heights)):
    Student_heights[n] = int(Student_heights[n])

print(Student_heights)

# Calculate total height
total_height = 0
for height in Student_heights:
    total_height += height

# Calculate number of students
number_of_students = 0
for student in Student_heights:
    number_of_students += 1

# Calculate average height
average_height = round(total_height / number_of_students)
print("Average height:", average_height)
