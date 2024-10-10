function manualFilter(func, array) {
    let result = []

    for (let i = 0; i < array; i++) {
        if (func(array[i])) {
            result.push(array[i])
        }
    }
    return result

}

function carBMW(car) {
    return car === BMW;
}

let cars = ["mitsubishi", "mersedes", "audi", "BMW", "porshe"];

let bestcar = manualFilter(carBMW, cars);
console.log(bestcar);