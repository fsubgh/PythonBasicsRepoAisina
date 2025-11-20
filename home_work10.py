def read_numbers():
    while True:
        raw = input("Числа (через пробел): ").strip()
        if not raw:
            print("Введите хотя бы одно число.")
            continue
        try:
            return list(map(int, raw.split()))
        except ValueError:
            print("Нужно вводить только целые числа.")


def linear(nums, value):
    for i, x in enumerate(nums):
        if x == value:
            return i
    return -1


def binary(nums, value):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == value:
            return mid
        if nums[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def bubble(nums):
    nums = nums[:]
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def get_min(nums):
    return min(nums) if nums else None


def get_max(nums):
    return max(nums) if nums else None


def get_avg(nums):
    return sum(nums) / len(nums) if nums else None


def get_median(nums):
    if not nums:
        return None
    data = sorted(nums)
    n = len(data)
    mid = n // 2
    if n % 2 == 1:
        return data[mid]
    return (data[mid - 1] + data[mid]) / 2


def run():
    numbers = read_numbers()
    while True:
        print("\n1) Линейный поиск")
        print("2) Бинарный поиск")
        print("3) Пузырёк")
        print("4) Минимум")
        print("5) Максимум")
        print("6) Среднее")
        print("7) Медиана")
        print("8) Выход")
        choice = input("Выбор: ").strip()

        if choice == "1":
            try:
                val = int(input("Число: "))
            except ValueError:
                print("Нужно ввести число.")
                continue
            print("Результат:", linear(numbers, val))
        elif choice == "2":
            sorted_nums = sorted(numbers)
            print("Отсортировано:", sorted_nums)
            try:
                val = int(input("Число: "))
            except ValueError:
                print("Нужно ввести число.")
                continue
            print("Результат:", binary(sorted_nums, val))
        elif choice == "3":
            numbers = bubble(numbers)
            print("Новый список:", numbers)
        elif choice == "4":
            print("Минимум:", get_min(numbers))
        elif choice == "5":
            print("Максимум:", get_max(numbers))
        elif choice == "6":
            print("Среднее:", get_avg(numbers))
        elif choice == "7":
            print("Медиана:", get_median(numbers))
        elif choice == "8":
            break
        else:
            print("Ошибка.")


if __name__ == "__main__":
    run()



