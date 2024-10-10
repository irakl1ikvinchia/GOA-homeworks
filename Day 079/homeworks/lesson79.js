const getPassword = document.getElementById("pass");
const errorMassage = document.getElementById("error");

getPassword.addEventListener("input", () => {
    if (getPassword.len < 8) {
        errorMassage.textContent = "your pass len not 8"
    } else {
        errorMassage.textContent = "";
    }
})