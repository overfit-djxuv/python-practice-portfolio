students = [
    {"name": "Alex", "marks": [85, 90, 78]},
    {"name": "Sarah", "marks": [95, 92, 98]},
    {"name": "John", "marks": [70, 75, 80]}
]

def calculate_average(marks):
    return sum(marks) / len(marks)

def calculate_grade(average):
    match average:
        case _ if average >= 90:
            grade = 'A'
        case _ if average >= 80:
            grade = 'B'
        case _ if average >= 70:
            grade = 'C'
        case _ if average >= 60:
            grade = 'D'
        case _:
            grade = 'F'
    
    return grade


def generate_class_report(students):

    averages = []

    for student in students:

        print('-'*10)
        print('Name : ',student['name'])
        print('Marks : ', student['marks'])
        average = calculate_average(student['marks'])

        grade = calculate_grade(average)
        print('Grade:', grade)

        averages.append(average)

        print('Average:', round(average, 2))

    print("---Students Reports---")
    total_student = len(students)
    print('Total_student' ,total_student)

    highest_avg = max(averages)
    print('highest Average : ',highest_avg)

    lowest_avg = min(averages)
    print('Lowest Average : ', lowest_avg)

    class_average = sum(averages) / len(averages)
    print('class Average', class_average)

    highest_index = averages.index(highest_avg)
    lowest_index = averages.index(lowest_avg)

    highest_student = students[highest_index]
    lowest_student = students[lowest_index]

    print("Top Performer:", highest_student["name"])

    print("Lowest Performer:", lowest_student["name"])

report = generate_class_report(students)




