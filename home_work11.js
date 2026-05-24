const libraryBook = {
    title: "ПРеступление и наказачние",
    author : "Достоевский Ф.М.",
    genre : "Классическая литература",
    year : 1866,
    available: true
}
libraryBook.raiting = 4.8;
delete libraryBook.available;
libraryBook.available = false
console.log(libraryBook)