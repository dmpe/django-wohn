var open = 'fa-eye';
var close = 'fa-eye-slash';

// for login
var passwordInput = document.getElementById('inputPassword');
// for registration
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
	var svg_icon = document.querySelector(CSS.escape(icon2) + "> svg:first-of-type");
	icon2.onclick = function() {
		if(svg_icon.classList.contains(open)) {
	  	passwordNewInput.type="text";
	    svg_icon.classList.remove(open);
	    svg_icon.className += ' ' + close;
	  } else {
	  	passwordNewInput.type="password";
	    svg_icon.classList.remove(close);
	    svg_icon.className += ' '+ open;
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

$("#buttonEYE2").click(function() {
  // Change the child svg attribute data-icon to the new icon (remove fa-)
  $("#buttonEYE2 > svg").addClass('fa-eye').removeClass('fa-eye-slash');
});