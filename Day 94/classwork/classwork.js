const fruits0 = ['apple', 'banana', 'cherry'];

fruits.forEach((fruit) => {
    console.log(fruit);
});


// forEach clone

Array.prototype.myForEach = function(callback) {
    for (let i = 0; i < this.length; i++) {
        if (i in this) { 
            callback(this[i], i, this);
        }
    }
};

const fruits1 = ['apple', 'banana', 'cherry'];

fruits0.myForEach((fruit) => {
    console.log(fruit);
});