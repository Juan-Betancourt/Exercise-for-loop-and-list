# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights \n\n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_height = 0
for height in student_heights:
  total_height += height
print(f"\nThe total height for students is {total_height}\n")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"The total number of students is {number_of_students}\n")

average_height = round(total_height / number_of_students)

print(f"The average height between all students is {average_height}\n")