// N1

// Objeqts

let user = {
    name: "irakli",
    lastname: "kvinchia",
    age: 17,
};

let cars = {
    carName1: "BMW",
    carName2: "MERSEDES-BENZ",
    carName3: "AUDI"
};

//__________________________________________________________________________

// N2

// Constructor, operator "new"

function User(name) {
    this.name = name;
    this.isAdmin = false;
  }
  
  let User = new User("irakli");

