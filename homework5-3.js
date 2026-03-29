function askMood(mood, callback){
    callback(mood);
}
function recommended(mood){
    if(mood === "веселое"){
        console.log("Послушай музыку или позвони другу!");
    }
    else if(mood === "грустное") {
        console.log("Соверши небольшую прогулку или посмотри комедию");
    }
    else if(mood === "подавленное"){
        console.log("Отдохни! Можно просто поспать или принять ванну");
    }
    else{
        console.log("Сделай что-то приятное для себя")
    }
}
let mood = prompt ("Введите ваще настроение");
askMood(mood,recommended);