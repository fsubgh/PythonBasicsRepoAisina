let numInput1 = prompt("Введите первое число");
let num1 = Number(numInput1);
let numInput2 = prompt("Введите второе число");
let num2 = Number(numInput2);
if (numInput1 === null || numInput2 === null || isNaN(num1) || isNaN(num2) || numInput1.trim() === "" || numInput2.trim() === ""){
    console.log("Ошибка! Введите число");
}
let remainder = num1 % num2;
if(remainder === 0){
    console.log(`Число ${num1} делится на ${num2} без остатка`);
}
else{
    console.log(`Число ${num1} не делится на ${num2} без остатка.Остаток ${remainder}`);
}
