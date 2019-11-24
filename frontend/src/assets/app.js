const open = "fa-eye";
const close = "fa-eye-slash";

// For login
const passwordInput = document.getElementById("inputPassword");
// For registration
const passwordNewInput = document.getElementById("inputNewPassword");
const passwordConfirmNewInput = document.getElementById("inputConfirmNewPassword");

const icon = document.getElementById("buttonEYE");
const icon2 = document.getElementById("buttonEYE2");
const icon3 = document.getElementById("buttonEYE3");

if (typeof (icon) != "undefined" && icon != null) {
  // If not null, then on click of the icon replace types & add/remove icon CSS classes
  icon.addEventListener("click", evt => {
    const svgIcon = evt.currentTarget.querySelector("svg");
    if (svgIcon.classList.contains(open)) {
      passwordInput.type = "text";
      svgIcon.classList.remove(open);
      svgIcon.classList.add(close);
    } else {
      passwordInput.type = "password";
      svgIcon.classList.remove(close);
      svgIcon.classList.add(close);
    }
  });
}

if (typeof (icon2) != "undefined" && icon2 != null) {
  icon2.addEventListener("click", evt => {
    const svgIcon2 = evt.currentTarget.querySelector("svg");
    if (svgIcon2.classList.contains(open)) {
      passwordNewInput.type = "text";
      svgIcon2.classList.remove(open);
      svgIcon2.classList.add(close);
    } else {
      passwordNewInput.type = "password";
      svgIcon2.classList.remove(close);
      svgIcon2.classList.add(open);
    }
  });
}

if (typeof (icon3) != "undefined" && icon3 != null) {
  icon3.addEventListener("click", evt => {
    const svgIcon3 = evt.currentTarget.querySelector("svg");
    if (svgIcon3.classList.contains(open)) {
      passwordConfirmNewInput.type = "text";
      svgIcon3.classList.remove(open);
      svgIcon3.classList.add(close);
    } else {
      passwordConfirmNewInput.type = "password";
      svgIcon3.classList.remove(close);
      svgIcon3.classList.add(open);
    }
  });
}

