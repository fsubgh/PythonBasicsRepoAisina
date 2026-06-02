const work = {
place : "Kaxan", 
position : "bebe", 
year_start : 2026,
year_end : 2027
}

Object.freeze(work);
Object.defineProperty(work, 'salary', {
    value: 5000,
    writeble: false,
    enumerable: true,
    configurable: true
});
console.log(Object.keys(work));