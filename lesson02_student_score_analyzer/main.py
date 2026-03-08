'''
Task 1 — Count total records
Task 2 — Find unique students
Task 3 — Find unique subjects
Task 4 — Count how many times each student appears
Task 5 — Compute average score per student
Task 6 — Find the highest scoring record
Task 7 — Find students who scored 90 or above
'''

from data import students

print("=== Student Score Analyzer ===")
print('\n')

# Task 1 — Count total records
print(f'Total records: {len(students)}')
print('\n')

# Task 2 — Find unique students

unique_students = set()
unique_subjects = set()

for student_name, subject, score in students:
    unique_students.add(student_name)
    unique_subjects.add(subject)

print('Unique students: ')
for item in sorted(unique_students):
    print(f'- {item}')
print(f'Total unique students: {len(unique_students)}')
print('\n')

print('Unique subjects: ')
for item in unique_subjects:
    print(f'- {item}')
print('\n')

# Task 4 — Count how many times each student appears
count_student_dict = dict()

for student_name, subject, score in students:
    count_student_dict[student_name] = count_student_dict.get(student_name, 0) + 1

print('Records per student:')
for key, value in count_student_dict.items():
    print(f'- {key}: {value}')
    
print('\n')

# Task 5 — Compute average score per student
total_score = dict()
score_count = dict()

print('Average score per student:')
for student_name, subject, score in students:
    total_score[student_name] = total_score.get(student_name, 0) + score
    score_count[student_name] = score_count.get(student_name, 0) + 1


for score in total_score:
    average = total_score[score] / score_count[score]
    print(f'- {score}: {average:.2f}')


print('\n')


# Task 6 — Find the highest scoring record
max_score = 0
max_student = None
max_subject = None

for student_name, subject, score in students:
    if score > max_score:
        max_score = score
        max_student = student_name
        max_subject = subject

print('Highest scoring record:')
print(f'- {max_student} | {max_subject} | {max_score}')
print('\n')

# Task 7 — Find students who scored 90 or above


print('Top performers:')
for student_name, subject, score in students:
    if score >= 90:
        print(f'- {student_name} | {subject} | {score}')
        