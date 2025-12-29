def number_sequence(start: int, end: int, even: bool = True):

    if even:
        current = start if start % 2 == 0 else start + 1
        step = 2
    else:
        current = start if start % 2 != 0 else start + 1
        step = 2

    while current <= end:
        yield current
        current += step


def main():
    print("=" * 60)
    print("Генератор последовательности чисел")
    print("=" * 60)

    try:
        start = int(input("Введите начало диапазона: ").strip())
        end = int(input("Введите конец диапазона: ").strip())
    except ValueError:
        print("Ошибка: введите целые числа.")
        return

    if start > end:
        print("Ошибка: начало диапазона должно быть меньше или равно концу диапазона.")
        return

    print("\nВыберите тип последовательности:")
    print("1. Чётные числа")
    print("2. Нечётные числа")

    choice = input("Ваш выбор (1 или 2): ").strip()

    if choice == "1":
        even = True
        sequence_type = "чётных"
    elif choice == "2":
        even = False
        sequence_type = "нечётных"
    else:
        print("Ошибка: выберите 1 или 2.")
        return

    print(f"\nПоследовательность {sequence_type} чисел от {start} до {end}:")
    print("-" * 60)

    numbers = list(number_sequence(start, end, even))

    if numbers:
        print(", ".join(map(str, numbers)))
        print(f"\nВсего чисел: {len(numbers)}")
    else:
        print(f"В диапазоне от {start} до {end} нет {sequence_type} чисел.")

    print("=" * 60)


if __name__ == "__main__":
    main()
