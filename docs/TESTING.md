# Testing

## Table of contents 
- [Testing](#testing)
  - [Table of contents](#table-of-contents)
  - [**Validation across site**](#validation-across-site)
    - [HTML Validator](#html-validator)
    - [CSS Validator](#css-validator)
    - [Javascript Validator](#javascript-validator)
  - [**Responsiveness across site**](#responsiveness-across-site)
  - [**Lighthouse Report**](#lighthouse-report)
    - [**Home desktop**](#home-desktop)
    - [**Home mobile**](#home-mobile)
    - [**Basket desktop**](#basket-desktop)
    - [**Basket mobile**](#basket-mobile)
    - [**Contact us desktop**](#contact-us-desktop)
    - [**Contact us mobile**](#contact-us-mobile)
    - [**Login desktop**](#login-desktop)
    - [**Login mobile**](#login-mobile)
    - [**Register desktop**](#register-desktop)
    - [**Register mobile**](#register-mobile)
    - [**My Orders desktop**](#my-orders-desktop)
    - [**My Orders mobile**](#my-orders-mobile)
    - [**Order Details desktop**](#order-details-desktop)
    - [**Order Details mobile**](#order-details-mobile)
    - [**Products desktop**](#products-desktop)
    - [**Products mobile**](#products-mobile)
    - [**Product Details desktop**](#product-details-desktop)
    - [**Product Details mobile**](#product-details-mobile)
    - [**Shipping desktop**](#shipping-desktop)
    - [**Shipping mobile**](#shipping-mobile)
  - [**Base**](#base)
  - [**Home page**](#home-page)
  - [**Products page**](#products-page)
  - [**Product Details page**](#product-details-page)
  - [**Basket page**](#basket-page)
  - [**Shipping page**](#shipping-page)
  - [**My Orders page**](#my-orders-page)
  - [**Order Details page**](#order-details-page)
  - [**Login/Register page**](#loginregister-page)
  - [**Contact Us page**](#contact-us-page)

## **Validation across site**

### [HTML Validator](https://validator.w3.org/)
HTML Validator highlighted the following issue due to handling of crispy form on Register page:
![Register_error](../docs/register_error.png)
As this part of the code is not accessible this issue is ignored. 
All of the other html files were checked and passed without any issues.  


### [CSS Validator](https://jigsaw.w3.org/css-validator/)
All the css files checked and passed without any issues.


### [Javascript Validator](https://jshint.com/)

Implemented toast message has returned with warnings upon validation through JSHint, but these warnings aren't relevant as the project is compatible with ES6 and the "undefined variables" are globally available.

All of the other javascript files were checked and passed without any issue. 


All python files checked and formatted without any issues with [PEP8](http://pep8online.com/) using `autopep8` with `isort`.

## **Responsiveness across site**
Tested and passed on various devices and displays: mobile, tablet and desktop.
Tested and passed across various browsers: Google Chrome, Safari, Firefox.

## **Lighthouse Report**
### **Home desktop**

![Home](../docs/lighthouse_reports/home_desktop.png)

### **Home mobile**

![Home](../docs/lighthouse_reports/home_mobile.png)

### **Basket desktop**

![Basket](../docs/lighthouse_reports/basket_desktop.png)

### **Basket mobile**

![Basket](../docs/lighthouse_reports/basket_mobile.png)

### **Contact us desktop**

![Contact us](../docs/lighthouse_reports/contactus_desktop.png)

### **Contact us mobile**

![Contact us](../docs/lighthouse_reports/contactus_mobile.png)

### **Login desktop**

![Login](../docs/lighthouse_reports/login_desktop.png)

### **Login mobile**

![Login](../docs/lighthouse_reports/login_mobile.png)

### **Register desktop**

![Register](../docs/lighthouse_reports/register_desktop.png)

### **Register mobile**

![Register](../docs/lighthouse_reports/register_mobile.png)

### **My Orders desktop**

![My Orders](../docs/lighthouse_reports/myorders_desktop.png)

### **My Orders mobile**

![My Orders](../docs/lighthouse_reports/myorders_mobile.png)

### **Order Details desktop**

![Order Details](../docs/lighthouse_reports/orderdetails_desktop.png)

### **Order Details mobile**

![Order Details](../docs/lighthouse_reports/orderdetails_mobile.png)

### **Products desktop**

![Products](../docs/lighthouse_reports/productlist_desktop.png)

### **Products mobile**

![Products](../docs/lighthouse_reports/productlist_mobile.png)

### **Product Details desktop**

![Product Details](../docs/lighthouse_reports/productdetails_desktop.png)

### **Product Details mobile**

![Product Details](../docs/lighthouse_reports/productdetails_mobile.png)

### **Shipping desktop**

![Shipping](../docs/lighthouse_reports/shipping_desktop.png)

### **Shipping mobile**

![Shipping](../docs/lighthouse_reports/shipping_mobile.png)



## **Base**

* Navbar  
    Navbar is positioned correctly and fully responsive (changes to burger icon on smaller devices as expected). Navbar items are highlighted on hover over. All navigation bar items navigate to the correct links. Dropdown menu for Products is fully functional, on click it navigates to each product category as well as to All Products. 

* Footer  
    Footer icons are displayed in the correct position and size. Icons color changes on hover over. Social media icons navigate to the correct links and display in a new window.  

## **Home page** 

* Carousel images  
    Carousel images are of high quality and positioned correctly across all devices and browsers. 
    Arrows navigate to the next and previous images and are positioned and displayed correctly at mid-height on both ends of the images. All carousel items navigate to the products list view on click.

* Logo image  
    Logo image is displayed in the correct position on all views and devices. Logo image navigates to Home page on click.

* FAQ  
    FAQ accordion style and items are displayed as expected if available.
    The questions and answers in the faq model are created, modified or deleted successfully through Django Admin. In case there are no questions available in the database model FAQ accordion is hidden.

## **Products page**

* Product cards  
    Product cards are displayed in a clear and organised way across all devices. In the preview the product image, name, price and current stock level is displayed for each item.  
    Products are created, modified and deleted successfully through Django Admin. 
    When current stock level equals 0 or product is not active, the item is unavailable, therefore it is dynamically removed from the product list and not displayed for users.
    On clicking a product's image it navigates the user to the detailed product view as well as the "Product Details" button. 
    The "Product Details" button displays clearly in the correct position and highlights on hover over.
    
* Pagination  
    Due to the pagination implemented, 6 product items are displayed per page across all devices. Pages are numbered and the active page number is displayed on the bottom of the page. Pages are navigated via the left and right arrows on the bottom of the page.

* Product categories  
    When clicking "Products" dropdown on navbar, a product category can be selected. Only products that are filtered to the category are displayed on the linked page.  
    Product categories and their items are added to the site through Django Admin, therefore are easy to update or remove any categories or products within.

* Search bar  
    The search bar is only displayed on the Products page and is only searching product names. The search button is displayed and functioning as expected. If product search doesn't return a result "No products were found that match your search query." message shows.


## **Product Details page**

* Text areas  
    Product information and detailed product description are displayed as expected.  

* Images  
    Product image is displayed correctly across all devices.  

* Buttons  
    "Back" button displayed and styled as expected, taking user back to the Products page on click. "Add to basket" button displayed and functioning as expected. If user is logged in, "Add to basket" button adds the product to the basket and redirects user to the Basket page. If not, user is redirected to login page, where following login user can continue shopping.

## **Basket page**

Only visible to users who are logged in.

* Text areas  
    Products in the basket are listed individually showing product name, quantity, and unit price in GBP. Basket is showing the correct total price in GBP.

* Buttons  
    Buttons are displayed and styled as expected. The "Keep shopping" button successfully redirects the user back to the products list. Quantity of each listed item are successfully updated and saved via the "Save" button. "Checkout" button successfully redirects the user to the Shipping page where customers can enter their details. 

* Item quantity
    The maximum quantity of an item in the basket cannot be more than the current stock level of the given product. If user enters a greater quantity, the quantity is automatically updated to the highest available quantity in stock and the user is notified of the change with a toast message.

If Basket is empty, item list and buttons are hidden, and a message is displayed with a link to All Products.

## **Shipping page**

Only visible to users who are logged in.

This form was built with crispy-forms.

* Text areas  
    Text is displayed as expected.  

* Images  
    Image is displayed correctly across all devices. 

* Form  
    Form validation on all input fields is working as expected, reflecting the model fields' validation. Shipping form is pre-populated with the user's most recently updated shipping address. On form submission, the user is successfully redirected to Stripe to process payment. Potential exceptions raised by the Stripe API are gracefully handled with a generic exception handler.
    Following the successful payment: the user is redirected to a "payment successful" page where they have the option to navigate back to Products or Home page. In case the payment wasn't successful, user can retry by resuming the order from the "My Orders" page. 
    
## **My Orders page**

Only visible to users who are logged in.

* Text areas  
    All text is displayed as expected.

* Buttons  
    "Order Details" button successfully redirecting user to the Detailed Order view.

* Pagination  
    Due to the pagination implemented, 6 product items are displayed per page across all devices. Pages are numbered and the active page number displayed on the bottom of the page. Pages are navigated via the left and right arrows on the bottom of the page.

* Order cards  
    User's previous orders in the list view are displayed in cards, starting with the most recent. Preview-cards contain information about the date and time the order has been placed, the full amount paid and payment status (a tick or x indicating successful/failed payment). 

In case a previous order contains 0 products, a filter has been implemented therefore the order is not visible under My Orders.

## **Order Details page**

Only visible to users who are logged in.

* Text areas  
    All text is displayed as expected. The Order Details contain the list of products ordered at the given date, price per item and quantity, the total paid for the order as well as the shipping address.

* Images  
    Image is displayed correctly across all devices.

* Buttons  
    "Back to all orders" button successfully redirects the user to the list view of previous orders on the "My Orders" page. "Continue payment" button is only visible when payment status is unsuccessful on the previous order and successfully redirects the user to Stripe to resume/retry the transaction.

 * In previous orders the item prices displayed are "frozen" at the price of that item at the time of placing the order. This feature was implemented to allow traceability and comparability for users, even if later the product price changes the users are able to see the exact amount they paid when placing that order.

## **Login/Register page**


These forms were built with crispy-forms.

* Text areas  
    All text is displayed as expected.

* Images  
    Image is displayed correctly across all devices.

* Buttons  
    Login/register buttons are displayed as expected across all devices and redirect the user to the correct links.

* Login  
    Upon providing a valid username and password, previously registered users can login to shop and/or access My Orders and Basket. In case an invalid input is submitted, login fails, and user is requested to update the failed inputs to valid details, (as part of the crispy-form validation; guidelines are displayed to the user). 
    Upon successful login, a toast message is shown providing feedback of the interaction to the user.  
    There is a prompt and link displayed on the Login page which on click redirect the user to the "Register" page. This feature allows the user to switch between Login and Register views.

* Register  
    Upon providing a valid username, email address and password, users can register to the website. In case invalid input is submitted, registration fails, and user is requested to update the failed inputs to valid details, (as part of the crispy-form validation; guidelines are displayed to the user). Upon successful registration, a toast message is shown providing feedback of the interaction to the user.

## **Contact Us page**

These form was built with crispy-forms.

* Text areas  
    All text is displayed as expected.

* Images  
    Image is displayed correctly across all devices.

* Form  
    Message cannot be submitted if either email address field or text field are empty. Submitted messages can be read by the admin through the Django Admin. The email input is pre-populated by the user's registered email if logged in, but can be altered to specify the email address to contact the user on regarding their query.