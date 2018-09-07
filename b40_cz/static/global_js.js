var open = 'fa-eye';
var close = 'fa-eye-slash';
var passwordInput = document.getElementById('inputPassword');
var eye_outline = document.getElementById('inputGroupAppendButton');
var icon = document.getElementById('inputGroupAppendEYE');

// on click of the icon outline
eye_outline.onclick = function() {
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