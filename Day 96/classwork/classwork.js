const numbers = [1,2,3,4,5];

const sum = numbers.reduce((acc, cur) => {
    return acc + cur
}, 10);

const multyplay = numbers.reduce((acc, cur) => {
    return acc * cur
}, 10);


const manualReduce = (arr, func, startingValue = 0) => {
    let acc = startingValue;

    for(const value of arr){
        acc = func(acc, value);
    }

    return acc;
}

console.log(manualReduce(numbers, (acc, cur) => acc + cur, 10))