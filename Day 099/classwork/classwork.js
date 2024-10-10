class Accaunt {

    static #userCount = 0;

    constructor(name, lastname, age) {
        this.name = name;
        this.lastname = lastname;
        this.age = age;
        this.userId = user.#userCount++;
    }

    get userInfo() {
        return {
            name: this.name,
            lastname: this.lastname,
            age: this.age,
            userId: this.userId
        }
    }
}