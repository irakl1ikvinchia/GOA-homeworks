const pop = document.getElementById(pop)

pop.addEventListener('click', function() {
    const p = document.createElement('p');
    p.textContent = Math.floor(Math.random() * 100) + 1;

    document.body.appendChild(p);
})