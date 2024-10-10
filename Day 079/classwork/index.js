function validateForm() {
    const namelValue = form.elements.name.value;
    const emailValue = form.elements.email.value;
    const passValue = form.elements.password.value;
    const colorValue = form.elements.color.value;

    if(emailValue == '' || passValue == '') {
        alert('Please fill in all fields');
        return;
    } 

    console.log('Form submitted successfully');
    console.log("Email: " + emailValue);
    console.log("Password: " + passValue);
}