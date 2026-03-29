let name = prompt("Введите ваше имя");
let ageInput = prompt("Введите ваш возраст");
let age = Number(ageInput);
if (ageInput === null || isNaN(age || ageInput.trim() === " ")){
    console.log("Ошика.Введите число");
}
else{
    console.log(`Привет, ${name}, твой возраст ${age}`);
}