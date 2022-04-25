# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights \n\n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_height = 0

for height in student_heights:
  total_height += height
# print(total_height)

total_students = 0

for student in student_heights:
  total_students += 1
# print(total_students)

average_height = round(total_height / total_students)

print(average_height)

#SIMPLE FUNCTION WITHOUT FOR LOOP
# total_height = sum(student_heights)
# print(total_height)

# total_students = len(student_heights)
# print(total_students)

# average_height = round(total_height / total_students)
# print(average_height)
