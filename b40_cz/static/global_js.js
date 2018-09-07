var open = 'fa-eye';
var close = 'fa-eye-slash';
var passwordInput = document.getElementById('inputPassword');
var icon = document.getElementById('buttonEYE');

// on click of the icon outline
icon.onclick = function() {
	if(icon.classList.contains(open)) {
  	passwordInput.type="text";
    icon.classList.remove(open);
    icon.className += ' '+ close;
  } else {
  	passwordInput.type="password";
    icon.classList.remove(close);
    icon.className += ' '+ open;
  }
}