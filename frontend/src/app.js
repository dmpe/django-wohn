const open = 'fa-eye';
const close = 'fa-eye-slash';

// For login
const passwordInput = document.getElementById('inputPassword');
// For registration
const	passwordNewInput = document.getElementById('inputNewPassword');
const passwordConfirmNewInput = document.getElementById('inputConfirmNewPassword');

const icon = document.getElementById('buttonEYE');
const icon2 = document.getElementById('buttonEYE2');
const icon3 = document.getElementById('buttonEYE3');

if (typeof(icon) != 'undefined' && icon != null) {
  // If not null, then on click of the icon replace types & add/remove icon CSS classes
  icon.addEventListener("click", evt => {
    const svg_icon = evt.currentTarget.querySelector("svg");
    if(svg_icon.classList.contains(open)) {
		  	passwordInput.type="text";
		    svg_icon.classList.remove(open);
		    svg_icon.classList.add(close);
    } else {
		  	passwordInput.type="password";
		    svg_icon.classList.remove(close);
		    svg_icon.classList.add(close);
    }
  });
}

if (typeof(icon2) != 'undefined' && icon2 != null) {
  icon2.addEventListener("click", evt => {
  		const svg_icon2 = evt.currentTarget.querySelector("svg");
  		if(svg_icon2.classList.contains(open)) {
		  	passwordNewInput.type="text";
		    svg_icon2.classList.remove(open);
		    svg_icon2.classList.add(close);
	    } else {
		  	passwordNewInput.type="password";
		    svg_icon2.classList.remove(close);
		    svg_icon2.classList.add(open);
	  	}
  	});
}

if (typeof(icon3) != 'undefined' && icon3 != null) {
  icon3.addEventListener("click", evt => {
    const svg_icon3 = evt.currentTarget.querySelector("svg");
    if(svg_icon3.classList.contains(open)) {
		  	passwordConfirmNewInput.type="text";
		    svg_icon3.classList.remove(open);
      svg_icon3.classList.add(close);
	 	} else {
		  	passwordConfirmNewInput.type="password";
		    svg_icon3.classList.remove(close);
		    svg_icon3.classList.add(open);
	  	}
  });
}

