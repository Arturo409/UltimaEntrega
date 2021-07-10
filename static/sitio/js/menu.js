
var btnMenu = document.getElementById('btn-menu');
var nav = document.getElementById('nav');

btnMenu.addEventListener('click', function() {
    nav.classList.toggle('menu-bar');
})

var input = document.getElementsByClassName('form_input');
for (var i = 0; i < input.length; i++) {
    input[i].addEventListener('keyup', function() {
        if (this.value.length >= 1) {
            this.nextElementSibling.classList.add('fijar');
        } else {
            this.nextElementSibling.classList.remove('fijar');
        }
    });
}