// forEach

const array0 = ['BMW', 'TOYOTA', ',MERSEDES'];

array.forEach(element => console.log(element));


// map

const array1 = [1, 2, 4, 6];

const newArray = array.map(element => x + 2);
console.log(newArray);


// filter

const numbers0 = [25, 28, 10, 4, 8, 18];

const result = numbers.filter(number => number > 8);
console.log(result);


// reduce

const numbers1 = [2,3,4,5];
const reducer = (accumulator, currentValue, index) => accumulator + currentValue;

//2 + 3 + 4 + 5
const sum = numbers.reduce(reducer);
//accumulator+2+3+4+5
const sunWithInitialValue = numbers.reduce(reducer, 1);

console.log(sum);

