var email = document.getElementById('email');
var fname = document.getElementById('fname');
var lname = document.getElementById('lname');
var password = document.getElementById('password');
var confirm_password = document.getElementById('confirm_password');
// Error messages
var email_error = document.getElementById('email_error');
var fname_error = document.getElementById('fname_error');
var lname_error = document.getElementById('lname_error');
var password_error = document.getElementById('password_error');
var confirm_password_error = document.getElementById('confirm_password_error');

function validate(event){
    var valid = true;

    email_error.innerText = '';
    fname_error.innerText = '';
    lname_error.innerText = '';
    password_error.innerText = '';
    confirm_password_error.innerText = '';

    if (email.value.trim() === ''){
        email_error.innerText = 'Email is required.';
        valid = false;
    }
    if (fname.value.trim() === ''){
        fname_error.innerText = 'First name is required.';
        valid = false;
    }
    if (lname.value.trim() === ''){
        lname_error.innerText = 'Last name is required.';
        valid = false;
    }
    if (password.value.trim() === ''){
        password_error.innerText = 'Password is required.';
        valid = false;
    }
    if (confirm_password.value.trim() === ''){
        confirm_password_error.innerText = 'Conform password is required.';
        valid = false;
    }
    else if (password.value.trim() !== '' && password.value !== confirm_password.value){
        confirm_password_error.innerText = 'Password must be the same.';
        valid = false;
    }

    if (!valid){
        event.preventDefault();
    }

    return valid;
}

document.querySelector('.form-cnt').addEventListener('submit', validate);