let total = 0;
while(true){
    let line = prompt("Введите строку");
    if(line === null){
        console.log("Ошибка! Введите строку");
    }
    if(line.trim().toLowerCase === "стоп"){
        break;
    }
    let withoutSpases = line.replace(/ /g, "");
    total += withoutSpases.length;
}
console.log("Кол-во символов без пробелов" + total);