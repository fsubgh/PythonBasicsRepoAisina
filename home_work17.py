from datetime import datetime
from functools import wraps
from typing import List, Optional


def log_action(action_name: str):

    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{current_time}] Выполняется: {action_name}")

            start_time = datetime.now()
            result = func(self, *args, **kwargs)
            end_time = datetime.now()

            execution_time = (end_time - start_time).total_seconds()
            if execution_time > 0:
                print(f"[{current_time}] Время выполнения: {execution_time:.4f} секунд")

            return result

        return wrapper

    return decorator


class TaskManager:

    def __init__(self):
        self.tasks: List[str] = []
        self.undo_stack: List[str] = []

    @log_action("Add task")
    def add_task(self, task: str):
        if not task.strip():
            print("Ошибка: задача не может быть пустой.")
            return

        self.tasks.append(task.strip())
        print("Задача добавлена.")

    @log_action("Show tasks")
    def show_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
            return

        print("\nСписок задач:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")
        print()

    @log_action("Complete task")
    def complete_task(self, task_number: int):
        if not self.tasks:
            print("Ошибка: список задач пуст.")
            return

        if task_number < 1 or task_number > len(self.tasks):
            print(f"Ошибка: задача с номером {task_number} не существует.")
            return

        removed_task = self.tasks.pop(task_number - 1)
        self.undo_stack.append(removed_task)
        print("Задача выполнена.")

    @log_action("Undo last action")
    def undo(self):
        if not self.undo_stack:
            print("Нет действий для отмены.")
            return

        restored_task = self.undo_stack.pop()
        self.tasks.append(restored_task)
        print(f"Задача '{restored_task}' восстановлена.")

    def run(self):
        print("=" * 60)
        print("Программа управления списком задач")
        print("=" * 60)
        print("\nДоступные команды:")
        print("  add      - добавить новую задачу")
        print("  show     - показать список всех задач")
        print("  complete - выполнить задачу (удалить её)")
        print("  undo     - отменить последнее действие")
        print("  exit     - завершить программу")
        print("=" * 60)

        while True:
            command = input("\nВведите команду (add, show, complete, undo, exit): ").strip().lower()

            if command == "add":
                task = input("Введите задачу: ").strip()
                self.add_task(task)

            elif command == "show":
                self.show_tasks()

            elif command == "complete":
                if not self.tasks:
                    print("Ошибка: список задач пуст.")
                    continue

                try:
                    task_number = int(input("Введите номер задачи для выполнения: ").strip())
                    self.complete_task(task_number)
                except ValueError:
                    print("Ошибка: введите корректный номер задачи.")

            elif command == "undo":
                self.undo()

            elif command == "exit":
                print("Программа завершена.")
                break

            else:
                print(f'Неизвестная команда "{command}". Используйте: add, show, complete, undo, exit.')


def main():
    manager = TaskManager()
    manager.run()


if __name__ == "__main__":
    main()
