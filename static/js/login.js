var uname_or_email = document.getElementById('uname_or_email');
var password = document.getElementById('password');
var uname_or_email_error = document.getElementById('uname_or_email_error');
var password_error = document.getElementById('password_error');

function validate(event){
    var valid = true;
    
    uname_or_email_error.innerText = '';
    password_error.innerText = '';

    if (uname_or_email.value.trim() === ''){
        uname_or_email_error.innerText = 'Username or Email required';
        valid = false;
    }
    if (password.value.trim() === ''){
        password_error.innerText = 'Password is required';
        valid = false;
    }

    if (!valid){
        event.preventDefault();
    }

    return valid;
}

document.querySelector('.form-cnt').addEventListener('submit', validate);