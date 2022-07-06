window.addEventListener("DOMContentLoaded", function(){
	var toastElList = [].slice.call(document.querySelectorAll('.toast'))
	const options = {
		"animation": true,
		"autohide": true,
		"delay": 10000,
	};
	var toastList = toastElList.map(function (toastEl) {
		const toast = new bootstrap.Toast(toastEl, options);
		toast.show()
		return toast;
})
})