import json
import os


class Task:

    def __init__(self, title: str, is_done: bool = False):
        self.title = title
        self.is_done = is_done

    def mark_done(self):
        self.is_done = True

    def get_status(self) -> str:
        return "Выполнено" if self.is_done else "Не выполнено"

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "is_done": self.is_done
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Task':
        """Создает задачу из словаря (для загрузки из JSON)"""
        return cls(data["title"], data.get("is_done", False))


class TaskManager:

    def __init__(self, filename: str = "tasks.json"):
        self.tasks = []
        self.filename = filename
        self.load_from_file()

    def add_task(self, title: str):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                print(f'Задача "{title}" уже существует в списке.')
                return

        new_task = Task(title)
        self.tasks.append(new_task)
        print(f'Задача "{title}" добавлена.')

    def mark_task_done(self, title: str):
        task_found = False
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_done()
                print(f'Задача "{title}" отмечена как выполненная.')
                task_found = True
                break

        if not task_found:
            print(f'Задача "{title}" не найдена в списке.')

    def show_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
            return

        for index, task in enumerate(self.tasks, start=1):
            status = task.get_status()
            print(f'{index}. {task.title} - {status}')

    def save_to_file(self):
        try:
            tasks_data = [task.to_dict() for task in self.tasks]


            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(tasks_data, file, ensure_ascii=False, indent=2)

            print("Данные сохранены. Программа завершена.")
        except Exception as e:
            print(f"Ошибка при сохранении файла: {e}")

    def load_from_file(self):
        if not os.path.exists(self.filename):
            self.tasks = []
            return

        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                tasks_data = json.load(file)

            self.tasks = [Task.from_dict(task_dict) for task_dict in tasks_data]
        except json.JSONDecodeError:
            print(f"Ошибка: файл '{self.filename}' содержит невалидный JSON.")
            self.tasks = []
        except Exception as e:
            print(f"Ошибка при загрузке файла: {e}")
            self.tasks = []


def main():
    print("=" * 60)
    print("Программа управления списком дел")
    print("=" * 60)
    print("\nДоступные команды:")
    print("  add  - добавить новую задачу")
    print("  done - отметить задачу как выполненную")
    print("  show - вывести список задач")
    print("  exit - сохранить данные и завершить программу")
    print("=" * 60)

    manager = TaskManager()

    while True:
        command = input("\nВведите команду: ").strip().lower()

        if command == "add":
            title = input("Введите название задачи: ").strip()
            if title:
                manager.add_task(title)
            else:
                print("Ошибка: название задачи не может быть пустым.")

        elif command == "done":
            title = input("Введите название задачи: ").strip()
            if title:
                manager.mark_task_done(title)
            else:
                print("Ошибка: название задачи не может быть пустым.")

        elif command == "show":
            manager.show_tasks()

        elif command == "exit":
            manager.save_to_file()
            break

        else:
            print(f'Неизвестная команда "{command}". Используйте: add, done, show, exit.')


if __name__ == "__main__":
    main()
