const ICON = {
	SHOW : 'fa-eye',
	HIDE : 'fa-eye-slash',
}

const INPUT = {
	SHOW : 'text',
	HIDE : 'password',
}

const togglePassword = (id) => {
	const input = document.getElementById(id);
	const classList = event.target.classList;

	if (classList.contains(ICON.HIDE)) {
		classList.replace(ICON.HIDE, ICON.SHOW);
		input.type = INPUT.SHOW;
	} else if (classList.contains(ICON.SHOW)) {
		classList.replace(ICON.SHOW, ICON.HIDE);
		input.type = INPUT.HIDE;
	}
}
