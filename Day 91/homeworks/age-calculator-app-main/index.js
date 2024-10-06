document.getElementById('age-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const day = parseInt(document.getElementById('day').value);
    const month = parseInt(document.getElementById('month').value);
    const year = parseInt(document.getElementById('year').value);
    const errorMessage = document.getElementById('error-message');
    const resultDiv = document.getElementById('result');
    
    // Reset messages
    errorMessage.innerText = '';
    resultDiv.innerText = '';

    const today = new Date();
    const birthDate = new Date(year, month - 1, day);
    
    // Validation
    if (!day || !month || !year) {
        errorMessage.innerText = 'All fields are required.';
        return;
    }
    
    if (day < 1 || day > 31 || month < 1 || month > 12) {
        errorMessage.innerText = 'Invalid day or month.';
        return;
    }
    
    if (birthDate > today) {
        errorMessage.innerText = 'Date cannot be in the future.';
        return;
    }
    
    const ageInMilliseconds = today - birthDate;
    const ageDate = new Date(ageInMilliseconds);
    const years = ageDate.getUTCFullYear() - 1970;
    const months = ageDate.getUTCMonth();
    const days = ageDate.getUTCDate() - 1;

    // Display result with animation
    resultDiv.innerHTML = `<h2>${years} Years, ${months} Months, ${days} Days</h2>`;
    resultDiv.classList.add('animate'); // Add a class for animation (CSS can handle this)
});