window.addEventListener("DOMContentLoaded", function(){
	quantityChangeEvents();
	deleteItemEvent();
});

/**
 * Change the provided HTML element's CSS display to 'inline-block'
 * @param {HTMLElement} element The HTML element to be display in the DOM.
 */
function showElement(element){
	element.style.display = "inline-block";
}

/**
 * Change the provided HTML element's CSS display to 'none'
 * @param {HTMLElement} element The HTML element to be removed from the DOM.
 */
function hideElement(element){
	element.style.display = "none";
}

/**
 * Handling of input quantity changes.
 * Check the changed input value against its original value.
 * Toggle between ready-to-save and ready-to-checkout states.
 */
function quantityChangeEvents(){
	const quantityInputs = document.querySelectorAll("[name^=\"quantity-product\"]");
	const saveButton = document.querySelector("#save-button");
	const checkoutButton = document.querySelector("#checkout-button");
	const originalInputValues = {};
	let noneDefaultQuantityInputs = [];
	quantityInputs.forEach(function(element){
		originalInputValues[element.name] = element.value;
		element.addEventListener("change", function(){
			if (element.value !== originalInputValues[element.name]){
				noneDefaultQuantityInputs.push(element.name);
			} else {
				noneDefaultQuantityInputs.pop(element.name);
			}
			if (noneDefaultQuantityInputs.length > 0){
				showElement(saveButton);
				hideElement(checkoutButton);
			} else {
				hideElement(saveButton);
				showElement(checkoutButton);
			}
		});
	});
}

/**
 * Set the quantity of the related basket item to zero.
 * Trigger the "change" event to be picked up by event handler.
 */
function deleteItemEvent(){
	const deleteButtons = document.querySelectorAll("[id^=\"delete-\"]");
	deleteButtons.forEach(function(deleteButton){
		deleteButton.addEventListener("click", function(){
			// e.g. "delete-product-6" -> "6"
			const productId = deleteButton.id.replace("delete-product-", "");
			const inputId = `quantity-product-${productId}`;
			const inputElement = document.querySelector(`[name="${inputId}"]`);
			inputElement.value = 0;
			inputElement.dispatchEvent(new Event("change"));
		});
	});
}
