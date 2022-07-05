window.addEventListener("DOMContentLoaded", function(){
	const deleteButtons = document.querySelectorAll('[id^="delete-"]');
	deleteButtons.forEach(function(deleteButton){
		deleteButton.addEventListener("click", function(){
			// delete-product-6 -> 6
			const productId = deleteButton.id.replace("delete-product-", "")
			const inputId = `quantity-product-${productId}`
			const inputElement = document.querySelector(`[name="${inputId}"]`)
			inputElement.value = 0;
		})
	})
})