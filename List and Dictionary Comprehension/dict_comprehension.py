import random

names= ['alex','beth','caroline','dave','eleanor','freddie']
student_scores = {name: random.randint(1,100) for name in names}
# passed_students = {student: student_scores[student] for student in student_scores
#                    if student_scores[student] >= 60}
passed_students = {student:score for (student,score) in student_scores.items() if score >= 60}
print(student_scores)
print(passed_students)
