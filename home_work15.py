import sys
from typing import List, Optional


class Student:


    students: List["Student"] = []

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.grades: List[float] = []

        Student.students.append(self)


    @staticmethod
    def is_valid_grade(grade: float) -> bool:
        return 1 <= grade <= 5


    def add_grade(self, grade: float) -> None:
        if not Student.is_valid_grade(grade):
            print(f"Предупреждение: недопустимая оценка {grade}. Оценка должна быть от 1 до 5.")
            return
        self.grades.append(grade)
        print(f"Оценка {grade} добавлена студенту {self.name}.")

    def average_grade(self) -> Optional[float]:
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)


    @classmethod
    def find_by_name(cls, name: str) -> Optional["Student"]:
        for student in cls.students:
            if student.name.lower() == name.lower():
                return student
        return None

    @classmethod
    def average_all_students(cls) -> Optional[float]:
        all_grades: List[float] = []
        for student in cls.students:
            all_grades.extend(student.grades)
        if not all_grades:
            return None
        return sum(all_grades) / len(all_grades)


def print_menu() -> None:
    print("\n" + "=" * 60)
    print("УПРАВЛЕНИЕ СТУДЕНТАМИ И ИХ ОЦЕНКАМИ")
    print("=" * 60)
    print("1. Добавить нового студента")
    print("2. Добавить оценки студенту")
    print("3. Вывести среднюю оценку студента")
    print("4. Вывести среднюю оценку всех студентов")
    print("5. Проверить допустимость оценки")
    print("6. Показать всех студентов и их оценки")
    print("7. Выход")


def input_float(prompt: str) -> Optional[float]:
    try:
        return float(input(prompt).strip())
    except ValueError:
        print("Ошибка: введите число.")
        return None


def main() -> None:
    print("Программа для управления данными о студентах и их оценках")

    while True:
        print_menu()
        choice = input("\nВыберите пункт меню (1-7): ").strip()


        if choice == "1":
            name = input("Введите имя студента: ").strip()
            if not name:
                print("Имя не может быть пустым.")
                continue
            if Student.find_by_name(name):
                print(f"Студент с именем '{name}' уже существует.")
                continue
            Student(name)
            print(f"Студент '{name}' добавлен.")


        elif choice == "2":
            name = input("Введите имя студента: ").strip()
            student = Student.find_by_name(name)
            if not student:
                print(f"Студент '{name}' не найден.")
                continue

            while True:
                grade = input_float("Введите оценку (1-5) или пустую строку для завершения: ")
                if grade is None:

                    raw = input("Нажмите Enter для выхода из режима ввода оценок или введите ещё оценку: ")
                    if not raw.strip():
                        break
                    try:
                        grade = float(raw.strip())
                    except ValueError:
                        print("Ошибка: введите число.")
                        continue
                student.add_grade(grade)


        elif choice == "3":
            name = input("Введите имя студента: ").strip()
            student = Student.find_by_name(name)
            if not student:
                print(f"Студент '{name}' не найден.")
                continue
            avg = student.average_grade()
            if avg is None:
                print(f"У студента '{student.name}' еще нет оценок.")
            else:
                print(f"Средняя оценка студента '{student.name}': {avg:.2f}")


        elif choice == "4":
            avg_all = Student.average_all_students()
            if avg_all is None:
                print("Нет ни одной оценки у студентов.")
            else:
                print(f"Средняя оценка по всем студентам: {avg_all:.2f}")


        elif choice == "5":
            grade = input_float("Введите оценку для проверки: ")
            if grade is None:
                continue
            if Student.is_valid_grade(grade):
                print(f"Оценка {grade} допустима (от 1 до 5).")
            else:
                print(f"Оценка {grade} недопустима. Допустимы значения от 1 до 5.")


        elif choice == "6":
            if not Student.students:
                print("Список студентов пуст.")
                continue
            print("\nСписок студентов и их оценок:")
            for student in Student.students:
                grades_str = ", ".join(str(g) for g in student.grades) if student.grades else "нет оценок"
                print(f"- {student.name}: {grades_str}")


        elif choice == "7":
            print("Завершение программы.")
            sys.exit(0)

        else:
            print("Некорректный пункт меню. Выберите число от 1 до 7.")


if __name__ == "__main__":
    main()
