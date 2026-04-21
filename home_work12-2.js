
const work1 = {
    place: "ООО Ромашка",
    position: "Менеджер",
    year_start: 2098,
    year_end: 2078,
}
const work2 = {
    place: "ООО Звезда",
    position: "Менеджер",
    year_start: 2020,
    year_end: 2023,
}
const work3 = {
    place: "ООО Липтон",
    position: "Менеджер",
    year_start: 2030,
    year_end: 2021,
}
Object.freeze(work1);
Object.freeze(work2);
Object.freeze(work3);

const person = {
    Familia: "Idrsiova",
    Otchectvo: "Ernestovna",
    work: [work1, work2, work3]
}
Object.defineProperty(person, "Имя", {
  value: "Анна",
  enumerable: true,
  writable: false, 
  configurable: false, 
});
Object.freeze(person);

console.log(person);
console.log("Object.keys:", Object.keys(person));