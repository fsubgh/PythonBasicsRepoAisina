class FileManager:

    def __init__(self, filename: str):
        self.filename = filename
        self.file = None

    def write(self, text: str):
        if self.file is None:
            raise ValueError("Файл не открыт. Используйте конструкцию with.")

        self.file.write(text)

    def __enter__(self):
        self.file = open(self.filename, 'w', encoding='utf-8')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file is not None:
            self.file.close()
            self.file = None
        return False


def main():
    print("Пример использования FileManager:")
    print("=" * 50)

    with FileManager('test.txt') as fm:
        fm.write('Hello, World!')

    print("Текст записан в файл test.txt")

    print("\nДополнительный пример:")
    print("=" * 50)

    with FileManager('example.txt') as fm:
        fm.write('Первая строка\n')
        fm.write('Вторая строка\n')
        fm.write('Третья строка')

    print("Текст записан в файл example.txt")

    print("\nСодержимое файла test.txt:")
    print("-" * 50)
    with open('test.txt', 'r', encoding='utf-8') as f:
        print(f.read())


if __name__ == "__main__":
    main()
