# [{'id': '100001',
#   'student': 'Ada Lovelace',
#   'coffee_preference': 'light',
#   'course': 'web development',
#   'grades': [70, 91, 82, 71],
#   'pets': [{'species': 'horse', 'age': 8}]},
# 1. How many students are there?
len(students)

# 2. How many students prefer light coffee? For each type of coffee roast?
len([student for student in students if student['coffee_preference'] == 'light'])

# 3. How many types of each pet are there?


number_of_horses = len([student for student in students if [pet['species'] for pet in student['pets'] if pet['species'].count('horse') > 0]])
number_of_cats = len([student for student in students if [pet['species'] for pet in student['pets'] if pet['species'].count('cat') > 0]])
number_of_dogs = len([student for student in students if [pet['species'] for pet in student['pets'] if pet['species'].count('dog') > 0]])




# 4. How many grades does each student have? Do they all have the same number of grades?
[len(student['grades']) for student in students]

# 5. What is each student's grade average?
all_grades = [student['grades'] for student in students]
average_grade = [[(sum(grade) / len(grade))] for grade in all_grades]

sum(all_grades[0:])

# 6. How many pets does each student have?
[len(student['pets']) for student in students]

# 7. How many students are in web development? data science?
num_students_in_web_dev = len([student for student in students if student['course'] == 'web development'])
num_students_in_data_science = len([student for student in students if student['course'] == 'data science'])

# 8. What is the average number of pets for students in web development?
students_in_web_dev = [student for student in students if student['course'] == 'web development']
num_pets_per_web_dev_student = [len(student['pets']) for student in students_in_web_dev]

# 9. What is the average pet age for students in data science?
students_in_data_science = [student for student in students if student['course'] == 'data science']
pet_info_for_ds_students_with_pets = [student['pets'] for student in students_in_data_science if len(student['pets']) > 0]



# 10. What is most frequent coffee preference for data science students?
# 11. What is the least frequent coffee preference for web development students?
# 12. What is the average grade for students with at least 2 pets?
# 13. How many students have 3 pets?
# 14. What is the average grade for students with 0 pets?
# 15. What is the average grade for web development students? data science students?
# 16. What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
# 17. What is the average number of pets for medium coffee drinkers?
# 18. What is the most common type of pet for web development students?
# 19. What is the average name length?
# 20. What is the highest pet age for light coffee drinkers?