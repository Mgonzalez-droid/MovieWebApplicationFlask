
const loginForm = document.getElementById("create-user-form");
const loginButton = document.getElementById("create-user-form-submit");
//const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    alert("Created User Account: " + username);

    /*if (username === "user" && password === "web_dev") {
        alert("You have successfully logged in.");
        location.reload();
    } else {
        loginErrorMsg.style.opacity = 1;
    }*/
})