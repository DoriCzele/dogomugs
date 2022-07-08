# Testing

## Table of contents 
* [Validation across site](#validation-across-site)
* [Responsiveness across site](#responsiveness-across-site)
* [Home](#home-page)
* [Products](#products-page)

## **Validation across site**
All the html files checked and passed without any issue through the [HTML Validator](https://validator.w3.org/).  
All the css files checked and passed without any issue through the [CSS Validator](https://jigsaw.w3.org/css-validator/).  
All the javascript files are checked and passed without any issue through the [Javascript Validator](https://jshint.com/).

## **Responsiveness across site**
Tested and passed on various devices and displays: mobile, tablet and desktop.
Tested and passed across various browsers: Google Chrome, Safari, Firefox.

## **Base**

* Navbar  
    Navbar is positioned correctly and fully responsive (changes to burger icon on smaller devices as expected). Navbar items are highlighted on hover over. All navigation bar items navigating to the correct links. Dropdown menu for Products is fully functional, on click it navigates to each product categories as well as to All Products. 

* Footer  
    Footer icons are displayed in the correct position and size. Icons color changes on hover over. Social media icons navigating to the correct links and displaying on a new window.  

## **Home page** 

* Carousel images  
    Carousel images is of high quality and positioned correctly across all devices and browsers. 
    Arrows navigating to the next and previous images are positioned and displayed correctly at mid-height on both ends of the images. All carousel items navigate to the products list view on click.

* Logo image  
    Logo image is displayed in the correct position on all views and devices. Logo image navigates to home page on click.

* FAQ
    FAQ accordion style and iotems are displayed as expected.
    The questions and answers in the faq model are created, modified or deleted successfully through Django Admin. 
## **Products page**

* Product cards  
    Product cards are displayed in a clear and organised way across all devices. In the preview the product image, name, price and current stock level is displayed for each item.  
    Products are created, modified and deleted successfully through Django Admin, where the product modal accessible for admin.  
    When current stock level equals 0, item is unavailable, therefore it is temporarily removed from the product list and not displayed for users.
    On clicking a product's image it navigates user to the detailed product view as well ad the "Product Details" button. 
    The "Product Details" button displayed clearly in the correct position and highlights on hover over.
    
* Pagination  
    Due to the pagination implemented, 6 product items are displayed per page across all devices. Pages are numbered and the active page number displayed on the bottom of the page. Pages are navigated via the left and right arrows on the bottom of the page.

* Product categories
    When clicking "Products" dropdown on navbar, product category can be selected. Only products that are filtered to the category are displayed on the page.  
    Product categories and their items are added to the site through Django Admin, therefore easy to update or remove any categories or products within.

* Search bar
    The search bar is only displayed on the Products page and is only searching in product names. Search button displayed and functioning as expected. If product search doesn't return a result "No products were found that match your search query." message shows.



## Product Details page

* Text areas  
    Product information and detailed product description are displayed as expected.  

* Images  
    Product image is displayed correctly across all devices.  

* Buttons  
    "Back" button displayed and styled as expected, taking user back to the Products page on click. "Add to basket" button displayed and functioning as expected, adding the product to the basket and redirecting user to the Basket page.


## Basket page

* Text areas  
    Products in the basket are listed individually showing product name, quantity, and unit price in GBP. Basket is showing the correct total price in GBP.

* Buttons  
    Buttons are displayed and styled as expected. The "Keep shopping" button successfully redirecting user back to the products list. Quantity of each listed items are successfully updated and saved via the "Save" button. "Checkout" button is successfully redirecting user to the Shipping page where customers can enter their details. 

* Item quantity
    The maximum quantity of an item in the basket cannot be more than the current stock level of the given product. If user types in a greater quantity, the quantity is automatically updated to the  highest available quantity on stock.



## My Orders page





#### Items tested
* Basket contents and functions
* Buttons

#### Conclusion
* All buttons are displayed and functioning as expected.
* All items of the basket are listed, displaying the product name, chosen quantity and unit price.
* The quantity field can be successfully updated manually or via the up and down arrows within the quantity field.
* The changed quantity is saved and updated via the Save changes button.
* The total order value and required payment is correctly displayed in the Total row.
* Keep shopping button is leading customers back to Products.
* Secure checkout button is leading customers to the Shipping form. 

## Shipping page
#### Items tested
* Shipping form
* Buttons

#### Conclusion

## Payment page
#### Items tested

#### Conclusion

## Log in page

#### Items tested

#### Conclusion

## Register page
#### Items tested

#### Conclusion