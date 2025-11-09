def calculate_average(grades):
    total = 0
    count = 0
    for grade in grades:
        total += grade
        count += 1
    if count == 0:
        return 0
    return total / count


def get_grade_text(average):
    if average >= 4.5:
        return "Отлично"
    elif average >= 3.5:
        return "Хорошо"
    elif average >= 2.5:
        return "Удовлетворительно"
    else:
        return "Плохо"

n = int(input("Введите количество студентов: "))

students = []

for i in range(n):
    name = input("Введите имя студента: ")
    grades_str = input("Введите оценки через пробел: ")
    grades_list = grades_str.split()

    grades = []
    for grade_str in grades_list:
        grades.append(int(grade_str))

    students.append([name, grades])

averages = [calculate_average(student[1]) for student in students]

print("\nИмя        Средний балл")
print("-" * 25)
for i in range(len(students)):
    name = students[i][0]
    avg = averages[i]
    print(f"{name:<10} {avg:.1f}")

max_avg = averages[0]
min_avg = averages[0]
max_index = 0
min_index = 0

for i in range(len(averages)):
    if averages[i] > max_avg:
        max_avg = averages[i]
        max_index = i
    if averages[i] < min_avg:
        min_avg = averages[i]
        min_index = i

print(f"\nЛучший студент: {students[max_index][0]} ({max_avg:.1f})")
print(f"Худший студент: {students[min_index][0]} ({min_avg:.1f})")

group_total = 0
group_count = 0
for avg in averages:
    group_total += avg
    group_count += 1

group_average = group_total / group_count if group_count > 0 else 0
print(f"Средний балл по группе: {group_average:.2f}")

print("\n--- Отчёт по оценкам ---")
for i in range(len(students)):
    name = students[i][0]
    avg = averages[i]
    grade_text = get_grade_text(avg)
    print(f"{name}: {grade_text}")

excellent_students = [students[i][0] for i in range(len(students)) if averages[i] >= 4.5]
print(f"\nСтуденты с отличной успеваемостью (>= 4.5): {excellent_students}")

