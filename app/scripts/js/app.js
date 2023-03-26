const form = document.querySelector('#login-form');

form.addEventListener('submit', function(event) {
event.preventDefault();

const username = form.elements.username.value;
const password = form.elements.password.value;

});