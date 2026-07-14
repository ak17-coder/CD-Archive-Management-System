const password = document.getElementById("password");
const toggle = document.getElementById("togglePassword");

toggle.addEventListener("click", function(){

    if(password.type==="password"){
        password.type="text";
        toggle.classList.remove("fa-eye");
        toggle.classList.add("fa-eye-slash");
    }else{
        password.type="password";
        toggle.classList.remove("fa-eye-slash");
        toggle.classList.add("fa-eye");
    }

});
// const form = document.getElementById("loginform");
// const username = document.getElementById("username");
// const error = document.getElementById("error-message");

// form.addEventListener("submit", function(e){

//     e.preventDefault();

//     if(username.value.trim()===""){
//         error.textContent="Please enter your username.";
//         return;
//     }

//     if(password.value.trim()===""){
//         error.textContent="Please enter your password.";
//         return;
//     }

//     error.textContent="";

//     window.location.href="pages/dashboard.html";

// });

