from typing import List, Optional


class Person:

    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    def get_info(self) -> str:
        return f"Имя: {self._name}, Возраст: {self._age}"


class Employee(Person):

    def __init__(self, name: str, age: int, position: str):
        super().__init__(name, age)
        self._position = position

    @property
    def position(self) -> str:
        return self._position

    def display_info(self) -> str:
        return f"{self.get_info()}, Должность: {self._position}"


class Manager(Employee):

    def __init__(self, name: str, age: int, position: str):
        super().__init__(name, age, position)
        self._team: List[Employee] = []

    @property
    def team(self) -> List[Employee]:
        return self._team.copy()

    def add_to_team(self, employee: Employee):
        if employee in self._team:
            print(f"Сотрудник '{employee.name}' уже в команде менеджера '{self._name}'.")
            return

        if employee == self:
            print("Менеджер не может быть в своей собственной команде.")
            return

        self._team.append(employee)
        print(f"Сотрудник '{employee.name}' добавлен в команду менеджера '{self._name}'.")

    def display_team_info(self) -> str:
        if not self._team:
            return f"У менеджера '{self._name}' нет сотрудников в команде."

        team_info = f"Команда менеджера '{self._name}':\n"
        for i, employee in enumerate(self._team, start=1):
            team_info += f"  {i}. {employee.display_info()}\n"

        return team_info.rstrip()


class CompanyUserManager:

    def __init__(self):
        self._employees: List[Employee] = []
        self._managers: List[Manager] = []

    def add_employee(self, name: str, age: int, position: str, is_manager: bool = False):
        all_people = self._employees + self._managers
        for person in all_people:
            if person.name.lower() == name.lower():
                print(f"Сотрудник с именем '{name}' уже существует.")
                return

        try:
            age = int(age)
            if age < 0:
                print("Ошибка: возраст не может быть отрицательным.")
                return
        except ValueError:
            print("Ошибка: возраст должен быть числом.")
            return

        if is_manager:
            manager = Manager(name, age, position)
            self._managers.append(manager)
            print(f"Менеджер '{name}' добавлен.")
        else:
            employee = Employee(name, age, position)
            self._employees.append(employee)
            print(f"Сотрудник '{name}' добавлен.")

    def find_employee(self, name: str) -> Optional[Employee]:
        all_employees = self._employees + self._managers
        for employee in all_employees:
            if employee.name.lower() == name.lower():
                return employee
        return None

    def find_manager(self, name: str) -> Optional[Manager]:
        for manager in self._managers:
            if manager.name.lower() == name.lower():
                return manager
        return None

    def assign_to_team(self, manager_name: str, employee_name: str):
        manager = self.find_manager(manager_name)
        if not manager:
            print(f"Ошибка: менеджер '{manager_name}' не найден.")
            return

        employee = self.find_employee(employee_name)
        if not employee:
            print(f"Ошибка: сотрудник '{employee_name}' не найден.")
            return

        if isinstance(employee, Manager):
            print(f"Ошибка: '{employee_name}' является менеджером и не может быть добавлен в команду.")
            return

        manager.add_to_team(employee)

    def display_all_employees(self):
        all_people = self._employees + self._managers

        if not all_people:
            print("В компании пока нет сотрудников.")
            return

        print("\n" + "=" * 60)
        print("СПИСОК СОТРУДНИКОВ")
        print("=" * 60)

        if self._employees:
            print("\nСотрудники:")
            for i, employee in enumerate(self._employees, start=1):
                print(f"{i}. {employee.display_info()}")

        if self._managers:
            print("\nМенеджеры:")
            for i, manager in enumerate(self._managers, start=1):
                print(f"{i}. {manager.display_info()}")
                team_info = manager.display_team_info()
                if "нет сотрудников" not in team_info:
                    print(f"  {team_info.replace(chr(10), chr(10) + '  ')}")

        print("=" * 60)


def print_menu():
    print("\n" + "=" * 60)
    print("УПРАВЛЕНИЕ СОТРУДНИКАМИ КОМПАНИИ")
    print("=" * 60)
    print("1. Добавить сотрудника")
    print("2. Добавить менеджера")
    print("3. Назначить сотрудника в команду менеджера")
    print("4. Просмотреть всех сотрудников")
    print("5. Выход")
    print("=" * 60)


def main():
    print("Программа для учета пользователей в компании")

    manager = CompanyUserManager()

    while True:
        print_menu()
        choice = input("\nВыберите пункт меню (1-5): ").strip()

        if choice == "1":
            name = input("Введите имя сотрудника: ").strip()
            if not name:
                print("Ошибка: имя не может быть пустым.")
                continue

            age_input = input("Введите возраст сотрудника: ").strip()
            position = input("Введите должность сотрудника: ").strip()
            if not position:
                print("Ошибка: должность не может быть пустой.")
                continue

            manager.add_employee(name, age_input, position, is_manager=False)

        elif choice == "2":
            name = input("Введите имя менеджера: ").strip()
            if not name:
                print("Ошибка: имя не может быть пустым.")
                continue

            age_input = input("Введите возраст менеджера: ").strip()
            position = input("Введите должность менеджера: ").strip()
            if not position:
                print("Ошибка: должность не может быть пустой.")
                continue

            manager.add_employee(name, age_input, position, is_manager=True)

        elif choice == "3":
            manager_name = input("Введите имя менеджера: ").strip()
            employee_name = input("Введите имя сотрудника: ").strip()

            if not manager_name or not employee_name:
                print("Ошибка: имена не могут быть пустыми.")
                continue

            manager.assign_to_team(manager_name, employee_name)

        elif choice == "4":
            manager.display_all_employees()

        elif choice == "5":
            print("Программа завершена. До свидания!")
            break

        else:
            print("Неизвестная команда. Выберите пункт от 1 до 5.")


if __name__ == "__main__":
    main()