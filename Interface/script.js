const navbarMenu = document.querySelector(".navbar .links");
const hamburgerBtn = document.querySelector(".hamburger-btn");
const hideMenuBtn = navbarMenu.querySelector(".close-btn");
const showPopupBtn = document.querySelector(".login-btn");
const formPopup = document.querySelector(".form-popup");
const hidePopupBtn = formPopup.querySelector(".close-btn");
const signupLoginLink = formPopup.querySelectorAll(".bottom-link a");
const forgotPassLink = formPopup.querySelector(".forgot-pass-link");
const continueBtn = formPopup.querySelector(".continue-btn"); 
const submitBtn = formPopup.querySelector(".submit-btn"); 
const backLoginBtn = formPopup.querySelector(".backLogin-btn");
const submitNewPassword = formPopup.querySelector(".new-pass form button"); 

hamburgerBtn.addEventListener("click", () => {
    navbarMenu.classList.toggle("show-menu");
});

hideMenuBtn.addEventListener("click", () => hamburgerBtn.click());

showPopupBtn.addEventListener("click", () => {
    document.body.classList.add("show-popup");
    formPopup.classList.remove("show-signup", "show-forgot-pass", "show-code-verif", "show-new-pass");
    formPopup.classList.add("show-login");
});

hidePopupBtn.addEventListener("click", () => {
    document.body.classList.remove("show-popup");
    formPopup.classList.remove("show-login", "show-signup", "show-forgot-pass", "show-code-verif", "show-new-pass");
});

signupLoginLink.forEach(link => {
    link.addEventListener("click", (e) => {
        e.preventDefault();
        if (link.id === 'signup-link') {
            formPopup.classList.remove("show-login", "show-forgot-pass");
            formPopup.classList.add("show-signup");
        } else {
            formPopup.classList.remove("show-signup", "show-forgot-pass");
            formPopup.classList.add("show-login");
        }
    });
});

forgotPassLink.addEventListener("click", (e) => {
    e.preventDefault();
    formPopup.classList.remove("show-login", "show-signup", "show-code-verif", "show-new-pass");
    formPopup.classList.add("show-forgot-pass");
});

continueBtn.addEventListener("click", (e) => {
    e.preventDefault();
    const forgotPassForm = formPopup.querySelector(".forgot-pass form");
    if (forgotPassForm.checkValidity()) {
        formPopup.classList.remove("show-forgot-pass");
        formPopup.classList.add("show-code-verif");  
    } else {
        forgotPassForm.reportValidity();
    }
});

submitBtn.addEventListener("click", (e) => {
    e.preventDefault();
    const forgotPassForm = formPopup.querySelector(".code-verif form");
    if (forgotPassForm.checkValidity()) {
        formPopup.classList.remove("show-code-verif");
        formPopup.classList.add("show-new-pass");  
    } else {
        forgotPassForm.reportValidity();
    }
});

submitNewPassword.addEventListener("click", (e) => {
    e.preventDefault();
    const newPassForm = formPopup.querySelector(".new-pass form");

    if (newPassForm.checkValidity()) {
        alert("Your password changed. Now you can login with your new password.");
        formPopup.classList.remove("show-new-pass");
        formPopup.classList.add("show-login"); 
        document.body.classList.remove("show-popup");  
    } else {
        newPassForm.reportValidity();
    }
});


backLoginBtn.addEventListener("click", (e) => {
    e.preventDefault();
    const newPassForm = formPopup.querySelector(".new-pass form");

    if (newPassForm.checkValidity()) {
        formPopup.classList.remove("show-new-pass");
        formPopup.classList.add("show-login");
        document.body.classList.remove("show-popup");
    } else {
        newPassForm.reportValidity();  
    }
});
