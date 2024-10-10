// N1

function evenSum(border) {
    let num = 0
    for(let i = 0; i < border;) {
        if(i % 2 == 0) {
            num += i
        }
    }

    
}


//___________________________________________________________________________


// N2

for(let i = 0; i < 20; i -= 1){
    console.log(i)
}


//___________________________________________________________________________


// N3

for(let i = 0; i < 10; i += 2){
    console.log(i)
}



//_____________________________________________________________________________


// N4


function generateEven(border){
    firstNnumList = []
    firstNnumList.push(0, border)
    
    return firstNnumList
}

function calculateSum(firstNnumList){
    let sum = 0
    for(let i = 0; i < firstNnumList;) {
        if(i % 2 == 0) {
            sum += i
        }
    }
        
    return sum
}


//____________________________________________________________________________________


// N5

const numsType = [];

for(let i = 0; i < 10; i++) {
    const numType = {
        value: i,
        type: ''
    }

    if(i % 2 === 0) {
        numType.type = 'Even';
    } else {
        numType.type = 'Odd';
    }

    numsType.push(numType);
}


console.log(numsType);

//__________________________________________________________________________________

// N6

let authorized = false;
let count = 3;

while (authorized !== true && count > 0) {
    const pass = prompt("Enter your password:");
    
    if (pass === "luka") {
        authorized = true;
        alert("Access granted!");
    } else {
        count--;
        alert("Access denied. You have " + count + " attempts left.");
    }
}