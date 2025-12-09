import json


def generate_report(json_file_path):
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            tasks = json.load(file)
        report = {}

        for task in tasks:
            assignee = task.get("assignee")
            status = task.get("status")

            if status == "completed":
                if assignee in report:
                    report[assignee] += 1
                else:
                    report[assignee] = 1

        return report

    except FileNotFoundError:
        print(f"Ошибка: файл '{json_file_path}' не найден!")
        return {}
    except json.JSONDecodeError:
        print(f"Ошибка: файл '{json_file_path}' содержит невалидный JSON!")
        return {}
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")
        return {}

def print_report(report):
    if not report:
        print("Отчёт пуст.")
        return

    print("ОТЧЁТ О ВЫПОЛНЕННЫХ ЗАДАЧАХ")
    print("=" * 50)
    print(f"{'Сотрудник':<20} {'Выполнено задач':>15}")
    print("-" * 50)

    sorted_report = sorted(report.items(), key=lambda x: x[1], reverse=True)

    for assignee, count in sorted_report:
        print(f"{assignee:<20} {count:>15}")

    print("=" * 50)
    print(f"Всего сотрудников: {len(report)}")
    print(f"Всего выполнено задач: {sum(report.values())}")


def main():
    print("Программа генерации отчёта о выполненных задачах")
    print("=" * 60)

    json_file = "tasks.json"

    print(f"\nЧтение данных из файла: {json_file}")

    report = generate_report(json_file)

    print(f"\nОтчёт в виде словаря:")
    print(f"  {report}")

    print_report(report)

    print("\n" + "=" * 60)
    print("ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ:")
    print("=" * 60)

    if report:
        top_performer = max(report.items(), key=lambda x: x[1])
        print(f"\nСотрудник с наибольшим количеством выполненных задач:")
        print(f"  {top_performer[0]}: {top_performer[1]} задача(и)")

        avg_tasks = sum(report.values()) / len(report)
        print(f"\nСреднее количество выполненных задач на сотрудника:")
        print(f"  {avg_tasks:.2f}")


if __name__ == "__main__":
    main()
