const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

const numberss = numbers.map((num, endex) => {
    if(index % 2 === 0) {
        return num * 2;
    } else {
        return num;
    }
})

console.log(numberss)