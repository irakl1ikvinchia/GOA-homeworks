const names = ['alice', 'bob', 'charlie', 'dave', 'eve'];

const transformedNames = names.map((name, index) => {
    return index % 2 === 0 ? name.toUpperCase() : name.toLowerCase();
});

console.log(transformedNames);


// map clone

Array.prototype.myMap = function(callback) {
    const result = [];
    for (let i = 0; i < this.length; i++) {
        if (i in this) {
            result.push(callback(this[i], i, this));
        }
    }
    return result;
};

const customTransformedNames = names.myMap((name, index) => {
    return index % 2 === 0 ? name.toUpperCase() : name.toLowerCase();
});

console.log(customTransformedNames);

