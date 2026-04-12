const libraryBook = {
    title: "Преступление и наказание",
    author: "Ф. М. Достоевский",
    genre: "detektiv",
    year: 1866,
    available: true,
}
libraryBook.raiting = 4.8;
libraryBook.available = !libraryBook.available;
delete libraryBook.genre;
console.log(libraryBook);