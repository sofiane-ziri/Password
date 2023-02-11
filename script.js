const generateBtn = document.getElementById("generate-btn");
const passwordField = document.getElementById("password");

function generatePassword() {
    const chars =
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*";
    let password = "";
    for (let i = 0; i < 12; i++) {
        password += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return password;
}

function countDown() {
    let counter = 30;
    const interval = setInterval(() => {
        if (counter === 0) {
            clearInterval(interval);
            passwordField.value = "";
            alert("Password has been deleted");
        } else {
            console.log(counter);
            counter--;
        }
    }, 1000);
}

generateBtn.addEventListener("click", () => {
    passwordField.value = generatePassword();
    countDown();
});

