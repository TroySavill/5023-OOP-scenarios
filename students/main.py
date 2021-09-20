import grades

student_list = []

#Create Michael object
michael = grades.Student('Michael',80,70,70,True)
print('id(michael):',id(michael))
student_list.append(michael)

#create Angela Object
angela = grades.Student('Angela',60,65,75,True)
print('id(angela):',id(angela))
# Adds the dictionary for Angela to the students list
student_list.append(angela)

#create Natalie Object
natalie = grades.Student('Natalie',60,65,75,False)
print('id(natalie):',id(natalie))
# Adds the dictionary for Natalie to the students list
student_list.append(natalie)

# Print the names and marks for each of the students
print('\nStudents:\n')
# TODO: Change code in loop to access Student objects' attributes, rather than dictionary
for student in student_list:
    print('---')
    print(f"Name: {student.name}")
    print(f"English: { student.english_mark }")
    print(f"Science: { student.science_mark }")
    print(f"Mathematics: { student.mathematics_mark }")
    if student.completed_assessments:
        print("Completed assessments: Yes")
    else:
        print("Completed assessments: No")
    print(f"Average: {student.average_mark()}")
    print('---\n')