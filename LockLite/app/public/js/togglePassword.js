const togglePasswords = document.querySelectorAll(".togglePassword");
const passwords = document.querySelectorAll(".password");

togglePasswords.forEach(function(togglePassword, index) {
	togglePassword.addEventListener("click", function () {
		// toggle the type attribute of corresponding password input
		const password = passwords[index];
		const type = password.getAttribute("type") === "password" ? "text" : "password";
		password.setAttribute("type", type);

		// toggle the icon
		const icon = this.querySelector("i");
		icon.classList.toggle("fa-eye");
	});
});
