def main():
    students = [
        {"name": "Анна", "score": 88},
        {"name": "Павел", "score": 95},
        {"name": "Игорь", "score": 72},
        {"name": "Марина", "score": 91},
    ]

    sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)

    print("\n1. Студенты, отсортированные по баллам (по убыванию):")
    for student in sorted_students:
        print(f"  {student['name']}: {student['score']}")

    filtered_students = list(filter(lambda x: x["score"] > 85, students))

    print("\n2. Студенты с баллом > 85:")
    for student in filtered_students:
        print(f"  {student['name']}: {student['score']}")

    names_uppercase = list(map(lambda x: x["name"].upper(), filtered_students))

    print("\n3. Имена студентов с баллом > 85 в верхнем регистре:")
    print(f"   {names_uppercase}")

if __name__ == "__main__":
    main()