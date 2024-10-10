let number = 0;

const paragrap = document.getElementById("p1");
const button = document.getElementById("b1");

button.addEventListener("click", () => {
    number += 1;
    paragrap.textContent = number
});