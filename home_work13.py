#1
# def find_min_max_avg(numbers):
#     if not numbers:
#         return None, None, None
#
#     minimum = min(numbers)
#     maximum = max(numbers)
#     average = sum(numbers) / len(numbers)
#
#     return minimum, maximum, average
#
#
# def filter_positive(numbers):
#     return list(filter(lambda x: x > 0, numbers))
#
# def smooth_list(numbers):
#     if not numbers:
#         return []
#
#     smoothed = []
#     n = len(numbers)
#
#     for i in range(n):
#         if i == 0:
#             smoothed.append(numbers[i] + numbers[i + 1])
#         elif i == n - 1:
#             smoothed.append(numbers[i - 1] + numbers[i])
#         else:
#             smoothed.append(numbers[i - 1] + numbers[i + 1])
#
#     return smoothed
#
#
# def input_numbers():
#
#     try:
#         user_input = input("Введите числа через пробел: ")
#         numbers = [float(x) for x in user_input.split()]
#         return numbers
#     except ValueError:
#         print("Ошибка: введите только числа!")
#         return []
#
#
# def main():
#     print("Программа обработки списка чисел")
#     print("=" * 50)
#
#     numbers = input_numbers()
#     if not numbers:
#         print("Список пуст. Программа завершена.")
#         return
#
#     print(f"\nВходящие данные: {numbers}")
#     print("-" * 50)
#
#     minimum, maximum, average = find_min_max_avg(numbers)
#
#     print(f"\n1. Минимум: {minimum}")
#     print(f"   Максимум: {maximum}")
#     print(f"   Среднее: {average:.4f}")
#
#     positive_numbers = filter_positive(numbers)
#     print(f"\n2. Положительные: {positive_numbers}")
#
#     smoothed = smooth_list(numbers)
#     print(f"\n3. Сглаженный список: {smoothed}")
#
# if __name__ == "__main__":
#     main()
from _pyrepl import commands


#2

# def sort_by_score(students):
#     return sorted(students, key=lambda x: x["score"], reverse=True)
#
#
# def filter_by_score(students, min_score=80):
#     return list(filter(lambda x: x["score"] >= min_score, students))
#
# def get_names_uppercase(students):
#     return list(map(lambda x: x["name"].upper(), students))
#
# def input_students():
#     students = []
#     print("Введите данные студентов (нажмите Enter без ввода для завершения):")
#
#     while True:
#         name = input("Имя студента: ").strip()
#         if not name:
#             break
#
#         try:
#             score = float(input("Балл студента: ").strip())
#             students.append({"name": name, "score": score})
#         except ValueError:
#             print("Ошибка: введите число для балла!")
#             continue
#
#     return students
#
# def main():
#     print("Программа обработки списка студентов")
#     print("=" * 50)
#
#     students = input_students()
#     if not students:
#         print("Список студентов пуст. Программа завершена.")
#         return
#
#     print(f"\nВходящие данные: {students}")
#     print("-" * 50)
#
#     sorted_students = sort_by_score(students)
#     print(f"\n1. Отсортировано по баллу (по убыванию):")
#     for student in sorted_students:
#         print(f"   {student['name']}: {student['score']}")
#
#
#     filtered_students = filter_by_score(sorted_students, min_score=80)
#     print(f"\n2. Студенты с баллом >= 80:")
#     for student in filtered_students:
#         print(f"   {student['name']}: {student['score']}")
#
#
#     names_uppercase = get_names_uppercase(filtered_students)
#     print(f"\n3. Список имён в верхнем регистре:")
#     print(f"   {names_uppercase}")
#
# if __name__ == "__main__":
#     main()

#3
# def count_vowels_consonants(text):
#     vowels = "aeiouа"
#     consonants = "bcdfghjklmnpqrstvw"
#
#     text_lower = text.lower()
#
#     vowel_count = 0
#     consonant_count = 0
#
#     for char in text_lower:
#         if char in vowels:
#             vowel_count += 1
#         elif char in consonants:
#             consonant_count += 1
#
#     return vowel_count, consonant_count
#
#
# def reverse_string(text):
#     return text[::-1]
#
# def remove_spaces(text):
#     return text.replace(" ", "")
#
#
# def main():
#     print("Программа обработки строки")
#     print("=" * 50)
#
#     text = input("Введите строку: ").strip()
#
#     if not text:
#         print("Ошибка: введите непустую строку!")
#         return
#
#     print(f"\nВходящие данные: \"{text}\"")
#     print("-" * 50)
#
#     vowel_count, consonant_count = count_vowels_consonants(text)
#
#     print(f"\nГласных: {vowel_count}")
#     print(f"Согласных: {consonant_count}")
#
#     reversed_text = reverse_string(text)
#     print(f"\nРеверс: \"{reversed_text}\"")
#
#     text_without_spaces = remove_spaces(text)
#     print(f"\nБез пробелов: \"{text_without_spaces}\"")
#
# if __name__ == "__main__":
#     main()

#4
# def make_operator(operation):
#     operations = {
#         "+": lambda x, y: x + y,
#         "*": lambda x, y: x * y,
#         "max": lambda x, y: x if x > y else y,
#     }
#
#     return operations.get(operation, lambda x, y: None)
#
#
# def main():
#     print("Программа создания операторов через lambda и высшие функции")
#     print("=" * 60)
#
#     print("\n1. Создание оператора умножения:")
#     op = make_operator("*")
#     result = op(3, 4)
#     print(f"   op = make_operator('*')")
#     print(f"   op(3, 4)")
#     print(f"   Результат: {result}")
#
#     print("\n2. Создание оператора сложения:")
#     op_add = make_operator("+")
#     result_add = op_add(3, 4)
#     print(f"   op = make_operator('+')")
#     print(f"   op(3, 4)")
#     print(f"   Результат: {result_add}")
#
#     print("\n3. Создание оператора максимума:")
#     op_max = make_operator("max")
#     result_max = op_max(3, 4)
#     print(f"   op = make_operator('max')")
#     print(f"   op(3, 4)")
#     print(f"   Результат: {result_max}")
#
#
# if __name__ == "__main__":
#     main()
#
#Task 5
# def move_robot(commands):
#     x, y = 0, 0
#
#     movements = {
#         "up": lambda pos: (pos[0], pos[1] + 1),  # Увеличиваем y
#         "down": lambda pos: (pos[0], pos[1] - 1),  # Уменьшаем y
#         "left": lambda pos: (pos[0] - 1, pos[1]),  # Уменьшаем x
#         "right": lambda pos: (pos[0] + 1, pos[1]),  # Увеличиваем x
#     }
#
#
#     for command in commands:
#         if command in movements:
#             x, y = movements[command]((x, y))
#         else:
#             print(f"Предупреждение: неизвестная команда '{command}'")
#
#     return (x, y)
#
#
# def main():
#     print("Программа управления роботом")
#     print("=" * 50)
#
#     commands = ["up", "up", "left", "down"]
#
#     print(f"Входящие данные:")
#     print(f"  {commands}")
#     print()
#
#     final_position = move_robot(commands)
#
#     print(f"Исходящие данные:")
#     print(f"  {final_position}")
#
# if __name__ == "__main__":
#     main()


#Task 6
# def bubble_sort(arr, compare_func):
#     result = arr.copy()
#     n = len(result)
#
#     for i in range(n):
#         swapped = False
#
#         for j in range(0, n - i - 1):
#             if compare_func(result[j], result[j + 1]):
#                 result[j], result[j + 1] = result[j + 1], result[j]
#                 swapped = True
#         if not swapped:
#             break
#
#     return result
#
# def main():
#     print("Программа пузырьковой сортировки с функцией сравнения")
#     print("=" * 60)
#
#     nums = [5, 2, 7, 3]
#     comp = lambda a, b: a > b
#
#     print(f"Входящие данные:")
#     print(f"  nums = {nums}")
#     print(f"  comp = lambda a, b: a > b")
#     print()
#
#     sorted_nums = bubble_sort(nums, comp)
#
#     print(f"Исходящие данные:")
#     print(f"  {sorted_nums}")
#
# if __name__ == "__main__":
#     main()


#Task 7
# def linear_search(arr, target):
#     for i, value in enumerate(arr):
#         if value == target:
#             return i
#     return -1
#
#
# def sort_list(arr):
#     return sorted(arr)
#
#
# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return -1
#
#
# def main():
#     print("Программа поиска и сортировки")
#     print("=" * 50)
#
#     nums = [3, 8, 1, 6]
#     target = 6
#
#     print(f"Входящие данные:")
#     print(f"  {nums}, target={target}")
#     print()
#
#     linear_result = linear_search(nums, target)
#     print(f"Линейный поиск: {linear_result}")
#
#     sorted_nums = sort_list(nums)
#     print(f"Отсортированный список: {sorted_nums}")
#
#     binary_result = binary_search(sorted_nums, target)
#     print(f"Бинарный: {binary_result}")
#
#     print("\n" + "=" * 50)
#     print("ИСХОДЯЩИЕ ДАННЫЕ:")
#     print("=" * 50)
#     print(f"Линейный поиск: {linear_result}")
#     print(f"Бинарный: {binary_result}")
#
# if __name__ == "__main__":
#     main()


#Task 8
def sum_rows(matrix):
    row_sums = []
    for row in matrix:
        row_sums.append(sum(row))
    return row_sums


def sum_columns(matrix):
    if not matrix:
        return []

    num_cols = len(matrix[0])
    column_sums = []

    for col_index in range(num_cols):
        col_sum = 0
        for row in matrix:
            col_sum += row[col_index]
        column_sums.append(col_sum)

    return column_sums


def transpose_matrix(matrix):
    if not matrix:
        return []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    transposed = []
    for col_index in range(num_cols):
        new_row = []
        for row_index in range(num_rows):
            new_row.append(matrix[row_index][col_index])
        transposed.append(new_row)

    return transposed

def multiply_by_two(matrix):
    return [list(map(lambda x: x * 2, row)) for row in matrix]

def print_matrix(matrix, title="Матрица"):
    print(f"\n{title}:")
    for row in matrix:
        print(f"  {row}")


def main():
    print("Программа операций с матрицами")
    print("=" * 60)

    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    print(f"Входящие данные:")
    print_matrix(matrix, "Исходная матрица")

    print("\n" + "=" * 60)
    print("ВЫПОЛНЕНИЕ ОПЕРАЦИЙ:")
    print("=" * 60)

    row_sums = sum_rows(matrix)
    print(f"\n1. Сумма по строкам:")
    print(f"   {row_sums}")
    for i, row_sum in enumerate(row_sums):
        print(f"   Строка {i}: {row_sum}")

    column_sums = sum_columns(matrix)
    print(f"\n2. Сумма по столбцам:")
    print(f"   {column_sums}")
    for i, col_sum in enumerate(column_sums):
        print(f"   Столбец {i}: {col_sum}")

    transposed = transpose_matrix(matrix)
    print(f"\n3. Транспонированная матрица:")
    print_matrix(transposed, "Транспонированная")

    multiplied = multiply_by_two(matrix)
    print(f"\n4. Матрица с умноженными на 2 элементами (через map):")
    print_matrix(multiplied, "Умноженная на 2")

    print("\n" + "=" * 60)
    print("ИСХОДЯЩИЕ ДАННЫЕ:")
    print("=" * 60)
    print(f"Сумма по строкам: {row_sums}")
    print(f"Сумма по столбцам: {column_sums}")
    print(f"Транспонированная матрица: {transposed}")
    print(f"Матрица * 2: {multiplied}")

if __name__ == "__main__":
    main()



