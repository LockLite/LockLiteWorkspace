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
	const iconClassList = event.target.classList;

	switch (input.type) {
		case INPUT.HIDE:
			input.type = INPUT.SHOW;
			iconClassList.replace(ICON.HIDE, ICON.SHOW);
			break;

		case INPUT.SHOW:
			input.type = INPUT.HIDE;
			iconClassList.replace(ICON.SHOW, ICON.HIDE);
			break;

		default:
			break;
	}
}
