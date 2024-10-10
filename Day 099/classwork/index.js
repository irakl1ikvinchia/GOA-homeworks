class Rectangle {
    #pass
    constructor(height, width) {
      this.height = height;  
      this.width = width;
    }

    get pass() {
        return this.#pass
    }
};