// N1

const numbers = [1, 2, 3, 4, 5];
const doubledNumbers = numbers.map(num => num * 2);
console.log(doubledNumbers);

//_____________________________________________________________________________________________


// N2

const nums = [1, 2, 3, 4, 5, 6];
const evenNumbers = nums.filter(num => num % 2 === 0);
console.log(evenNumbers);

// ___________________________________________________________________________________________


// N3

const squareNumbers = numbers.map(num => num ** 2);
console.log(squareNumbers);

//______________________________________________________________________________________________


// N4

const names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve'];
const longNames = names.filter(name => name.length > 5);
console.log(longNames);

//______________________________________________________________________________________________


// N5

const strings = ['hello', 'world', 'javascript', 'is', 'great'];
const capitalizedStrings = strings.map(str => str.charAt(0).toUpperCase() + str.slice(1));
console.log(capitalizedStrings);

//_______________________________________________________________________________________________


// N6

let total = 0;
numbers.forEach(num => {
    total += num;
});
console.log(total);

//_________________________________________________________________________________________________


// N7

const words = ['a', 'an', 'the', 'quick', 'brown', 'fox'];
const longWords = words.filter(word => word.length > 3);
console.log(longWords);

//_________________________________________________________________________________________________



// N8

const wordList = ['cat', 'dog', 'fish'];
const prefixedWords = wordList.map(word => 'super' + word);
console.log(prefixedWords);

//_________________________________________________________________________________________________



// N9

const moreNumbers = [1, 2, 3, 4, 5, 6, 7];
const oddNumbers = moreNumbers.filter(num => num % 2 !== 0);
console.log(oddNumbers);

//_________________________________________________________________________________________________



// N10

const numberArray = [10, 20, 30, 40, 50];
numberArray.forEach(num => {
    console.log(num); 
});

//_________________________________________________________________________________________________
