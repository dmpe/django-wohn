var open = 'fa-eye';
var close = 'fa-eye-slash';

var passwordInput = document.getElementById('inputPassword');
var	passwordNewInput = document.getElementById('inputNewPassword');
var passwordConfirmNewInput = document.getElementById('inputConfirmNewPassword');

var icon = document.getElementById('buttonEYE');
var icon2 = document.getElementById('buttonEYE2');
var icon3 = document.getElementById('buttonEYE3');

if (typeof(icon) != 'undefined' && icon != null) {
	// if not null, then on click of the icon replace types & add/remove icon CSS classes
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
}

if (typeof(icon2) != 'undefined' && icon2 != null) {
	icon2.onclick = function() {
		if(icon2.classList.contains(open)) {
	  	passwordNewInput.type="text";
	    icon2.classList.remove(open);
	    icon2.className += ' '+ close;
	  } else {
	  	passwordNewInput.type="password";
	    icon2.classList.remove(close);
	    icon2.className += ' '+ open;
	  }
	}
}

if (typeof(icon3) != 'undefined' && icon3 != null) {
	icon3.onclick = function() {
		if(icon3.classList.contains(open)) {
	  	passwordConfirmNewInput.type="text";
	    icon3.classList.remove(open);
	    icon3.className += ' '+ close;
	  } else {
	  	passwordConfirmNewInput.type="password";
	    icon3.classList.remove(close);
	    icon3.className += ' '+ open;
	  }
	}
}

$("#emailSendAlert").click(function(){
	$("#checkEmailAlert").addClass("show");
});