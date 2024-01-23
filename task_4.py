import json


def calculate_average_grade(students):
    total_average = 0

    for student in students:
        grade = student.get("grade")
        if grade is not None:
            total_average += grade
            student["average_grade"] = grade
        else:
            student["average_grade"] = None

    group_average = total_average / len(students)

    return group_average



with open("students.json", "r", encoding="utf-8") as file:
    students_data = json.load(file)

group_average = calculate_average_grade(students_data)

for student in students_data:
    print(f"{student['name']} {student['surname']}: Балл - {student['average_grade']}")

print(f"\nОбщий средний балл по группе: {group_average}")
