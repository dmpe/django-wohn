var openEye = "fa-eye";
var closeEye = "fa-eye-slash";

// For login
var passwordInput = document.getElementById("inputPassword");
// For registration
var passwordNewInput = document.getElementById("inputNewPassword");
var passwordConfirmNewInput = document.getElementById("inputConfirmNewPassword");

var icon = document.getElementById("buttonEYE");
var icon2 = document.getElementById("buttonEYE2");
var icon3 = document.getElementById("buttonEYE3");

if (typeof (icon) != "undefined" && icon != null) {
  // If not null, then on click of the icon replace types & add/remove icon CSS classes
  icon.addEventListener("click", evt => {
    var svgIcon = evt.currentTarget.querySelector("svg");
    if (svgIcon.classList.contains(openEye)) {
      passwordInput.type = "text";
      svgIcon.classList.remove(openEye);
      svgIcon.classList.add(closeEye);
    } else {
      passwordInput.type = "password";
      svgIcon.classList.remove(closeEye);
      svgIcon.classList.add(closeEye);
    }
  });
}

if (typeof (icon2) != "undefined" && icon2 != null) {
  icon2.addEventListener("click", evt => {
    var svgIcon2 = evt.currentTarget.querySelector("svg");
    if (svgIcon2.classList.contains(openEye)) {
      passwordNewInput.type = "text";
      svgIcon2.classList.remove(openEye);
      svgIcon2.classList.add(closeEye);
    } else {
      passwordNewInput.type = "password";
      svgIcon2.classList.remove(closeEye);
      svgIcon2.classList.add(openEye);
    }
  });
}

if (typeof (icon3) != "undefined" && icon3 != null) {
  icon3.addEventListener("click", evt => {
    var svgIcon3 = evt.currentTarget.querySelector("svg");
    if (svgIcon3.classList.contains(openEye)) {
      passwordConfirmNewInput.type = "text";
      svgIcon3.classList.remove(openEye);
      svgIcon3.classList.add(closeEye);
    } else {
      passwordConfirmNewInput.type = "password";
      svgIcon3.classList.remove(closeEye);
      svgIcon3.classList.add(openEye);
    }
  });
}

