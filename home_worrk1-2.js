const name = prompt("Введите ваше имя:");
const ageInput = prompt("Введите ваш возраст:");
const age = Number(ageInput);

if (ageInput === null || name === null) {
  console.log("Ввод отменён.");
} else if (ageInput.trim() === "" || isNaN(age)) {
  console.log("Ошибка: возраст должен быть числом.");
} else {
  console.log(`Привет, ${name.trim()}! Тебе ${age} лет.`);
}