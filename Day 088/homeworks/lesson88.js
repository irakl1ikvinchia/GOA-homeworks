const humanWinsP = document.getElementById("human");
const compWinsP = document.getElementById("comp");
const winsP = document.getElementById("wins");
const btnsDiv = document.getElementById("btns");
const choises = ["rock", "paper", "scissors"]

let humanWins = 0;
let compWins = 0;

btnsDiv.addEventListener("click", function(e) {

    const btnId = e.target.id;
    const compchoise = choises[Math.floor(Math.random() * choises.length)];

    if(btnId === compchoise) {
        winsP.textContent = "its a tie!";
    } else if((btnId === "rock" && compchoise === "paper" ) || (btnId === "scissors" && compchoise === "rock") || (btnId === "peper" && compchoise == "scissors")) {
        compWins++;
        compWinsP.textContent = compWins;
        winsP.textContent = "you lost!";
    } else {
        humanWins++;
        humanWinsP.textContent = humanWins;
        winsP.textContent = "you win";
    }
});