class Item:
    """
    Базовый элемент библиотеки.
    Атрибуты:
        id: Уникальный идентификатор.
        title: Название.
        year: Год издания.
    """

    def __init__(self, item_id: int, title: str, year: int):
        """
        Создать элемент.
        Args:
            item_id: id элемента (int).
            title: название (str).
            year: год издания (int).
        """
        self.id = item_id
        self.title = title
        self.year = year

    def __str__(self):
        """Красивое строковое представление элемента."""
        return f"[{self.id}] {self.title} ({self.year})"


class Book(Item):
    """
    Книга в библиотеке.
    Наследуется от Item и добавляет:
        author: автор книги
        isbn: ISBN
        available: статус (True — доступна, False — выдана)
    """

    def __init__(self, item_id: int, title: str, year:str, author:str, isbn:str, available=True):
        """Создать книгу.
        Args:
            item_id: id книги (int).
            title: название (str).
            year: год издания (int).
            author: автор (str).
            isbn: ISBN (str).
            available: доступность (bool).
        """
        super().__init__(item_id, title, year)
        self.author = author
        self.isbn = isbn
        self.available = bool(available)

    def __str__(self):
        """Красивое представление книги."""
        status = "доступна" if self.available else "выдана"
        return (
            f"[{self.id}] '{self.title}' ({self.year}), "
            f"автор: {self.author}, ISBN: {self.isbn}, статус: {status}"
        )


class Reader:
    """Читатель библиотеки.

    Атрибуты:
        id: идентификатор читателя
        name: имя читателя
        books: список взятых книг (Book)
    """

    def __init__(self, reader_id: int, name:str):
        """Создать читателя.

        Args:
            reader_id: id читателя (int).
            name: имя (str).
        """
        self.id = reader_id
        self.name = name
        self.books = []  # список объектов Book

    def take_book(self, book):
        """Добавить книгу в список взятых.

        Args:
            book: объект Book.
        """
        self.books.append(book)

    def give_back_book(self, book):
        """Убрать книгу из списка взятых.

        Args:
            book: объект Book.
        """
        self.books.remove(book)

    def __str__(self):
        """Красивое представление читателя."""
        books_str = ", ".join(str(book.id) for book in self.books) if self.books else "нет книг"
        return f"Читатель [{self.id}] {self.name}, книги: {books_str}"


class BookAlreadyLentError(Exception):
    """Ошибка: книга уже выдана."""


class BookNotFoundError(Exception):
    """Ошибка: книга не найдена."""


class ReaderNotRegisteredError(Exception):
    """Ошибка: читатель не зарегистрирован."""


class BookNotBorrowedByReaderError(Exception):
    """Ошибка: читатель не брал эту книгу."""


class Library:
    """Библиотека: хранит книги и читателей и управляет выдачей/возвратом."""

    def __init__(self):
        """Создать пустую библиотеку."""
        self.books = {}
        self.readers = {}

    def add_book(self, book):
        """Добавить книгу в библиотеку.

        Args:
            book: объект Book.
        """
        self.books[book.id] = book

    def register_reader(self, reader):
        """Зарегистрировать читателя.

        Args:
            reader: объект Reader.
        """
        self.readers[reader.id] = reader

    def lend_book(self, book_id, reader_id):
        """Выдать книгу читателю.

        Raises:
            BookNotFoundError: если книги нет в библиотеке
            ReaderNotRegisteredError: если читатель не зарегистрирован
            BookAlreadyLentError: если книга уже выдана
        """
        if book_id not in self.books:
            raise BookNotFoundError(f"Книга с id {book_id} не найдена")
        if reader_id not in self.readers:
            raise ReaderNotRegisteredError(f"Читатель с id {reader_id} не зарегистрирован")

        book = self.books[book_id]
        reader = self.readers[reader_id]

        if not book.available:
            raise BookAlreadyLentError(f"Книга '{book.title}' уже выдана")

        book.available = False
        reader.take_book(book)

    def return_book(self, book_id, reader_id):
        """Принять книгу от читателя.

        Raises:
            BookNotFoundError: если книги нет в библиотеке
            ReaderNotRegisteredError: если читатель не зарегистрирован
            BookNotBorrowedByReaderError: если читатель не брал эту книгу
        """
        if book_id not in self.books:
            raise BookNotFoundError(f"Книга с id {book_id} не найдена")
        if reader_id not in self.readers:
            raise ReaderNotRegisteredError(f"Читатель с id {reader_id} не зарегистрирован")

        book = self.books[book_id]
        reader = self.readers[reader_id]

        if book not in reader.books:
            raise BookNotBorrowedByReaderError("Этот читатель не брал данную книгу")

        reader.give_back_book(book)
        book.available = True

    def find_books_by_author(self, author: str):
        """Найти все книги по автору.

        Args:
            author: имя автора (str).

        Returns:
            Список книг (list[Book]).
        """
        return [book for book in self.books.values() if book.author == author]

    def get_reader_books(self, reader_id: int):
        """Получить список книг у читателя.
        Args:
            reader_id: id читателя (int).
        Raises:
            ReaderNotRegisteredError: если читатель не зарегистрирован
        Returns:
            Список книг (list[Book]).
        """
        if reader_id not in self.readers:
            raise ReaderNotRegisteredError(f"Читатель с id {reader_id} не зарегистрирован")
        return self.readers[reader_id].books


if __name__ == "__main__":
    """Демонстрация работы системы управления библиотекой."""
    library = Library()

    b1 = Book(1, "Война и мир", 1869, "Лев Толстой", "111-111")
    b2 = Book(2, "Преступление и наказание", 1866, "Фёдор Достоевский", "222-222")
    b3 = Book(3, "Анна Каренина", 1877, "Лев Толстой", "333-333")

    library.add_book(b1)
    library.add_book(b2)
    library.add_book(b3)

    r1 = Reader(1, "Иван Иванов")
    r2 = Reader(2, "Мария Петрова")

    library.register_reader(r1)
    library.register_reader(r2)

    try:
        library.lend_book(1, 1)
        library.lend_book(2, 1)
        '''
        попробуем выдать уже выданную книгу
        '''
        library.lend_book(2, 2)
    except (BookNotFoundError, ReaderNotRegisteredError, BookAlreadyLentError) as e:
        print("Ошибка:", e)

    print("Книги читателя 1:")
    for book in library.get_reader_books(1):
        print(book)

    print("\nКниги Льва Толстого:")
    for book in library.find_books_by_author("Лев Толстой"):
        print(book)


    try:
        library.return_book(1, 1)
        library.return_book(3, 1)
    except (BookNotFoundError, ReaderNotRegisteredError, BookNotBorrowedByReaderError) as e:
        print("Ошибка:", e)
    print("\nПосле возврата книги 1:")
    for book in library.get_reader_books(1):
        print(book)
