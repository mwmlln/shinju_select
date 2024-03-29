# Testing


## Responsiveness 

Throughout, the site is tested to ensure all pages are displayed appropriately in all screen sizes

* Responsiveness of the pages are tested with [Chrome DevTools](https://developer.chrome.com/docs/devtools/) and [Responsive Design Checker](https://www.responsivedesignchecker.com/). Results of the tests:

  <details><summary>Responsiveness Tests</summary>
  <img src="ss/responsiveness.png" width="600">
  </details>

## Browser compatibility

  Tested as follows:

  <img src="ss/browser_compatibility.png" width="500">

## Automated Testing

### Testing using Django Unittest

This site was mainly tested manually, but some automated tests using unittest were carried out. The test files are located in the test directories under the corresponding app. 

## Manual Testing


## User Story testing


### #01 Create Landing page

  * Acceptance criteria - State clear purpose of the site in the page and no confusing elements for site visitors &#9745;
  
    Tasks
    * a. There should be a button to open the product page clearly visible when the landing page is opened so that the site visitors can easily move to the page to see the products &#9745;
    * b. Pages should be responsive in all screen sizes &#9745;
    * c. Home button visible in Navbar and About page button should be located in footer so that site user can access these pages anywhere within the site &#9745;

### #02 View a list of the products

  * Acceptance criteria : Create product list page with clear display of the products &#9745;

    Tasks

    * a. 4 products listed in a row and 2 rows per page. Pagination in place for 8 items  - changed to 3 products in a row and 12 per page to improve the visual impact of the products &#9745;
    * b. Product name, price and category is listed under the product image &#9745;
    * c. Sort bar and price filter should be located at the top - Not implemented

### #03 View specific category of products

  * Acceptance criteria : Create category buttons to filter by category and ensure the appropriate items are displayed &#9745;

    Tasks

    * a. category buttons in the landing page and product list page - only implemented in landing page &#9745;
    * b.  Choosing category should only displays the chosen category products &#9745;
    * c. There should be 4 categories at least as a start up &#9745;

### #04 View individual product details

  * Acceptance criteria : Product detail page to display the product info in details and button to add the item in the bag with quantity and sizing options where applicable &#9745;

    Tasks

    * a. Product images displayed on the left &#9745;
    * b.  Product name, adjust size and quantity, price, category, back to shopping page link and add button on the right - Size option not implemented 
    * c. Product description below the image and buttons - Changed to the side as it looked neater
    * d. Product review box at the bottom of the page &#9745;

### #05 Filter/Tag special items

  * Acceptance criteria : Special items list can be selected and displayed in the product list page &#9745;

    Tasks

    * a. Special items link included in the category - changed to independent tag from category for easier filtering &#9745;
    * b.  Special items should have budges to make them stand out in the list &#9745;

### #06 Total price and number of items in the bag

  * Acceptance criteria : Display the number of items and total price under bag icon in the navbar &#9745;

    Tasks

    * a. Number of items in the bag and total price visible under the cart icon at all times if there is anything in the bag - only total price due to small space &#9745;

### #07 Product ratings/Reviews

  * Acceptance criteria :  Use rating with stars and reviews for items displayed in product detail page - Showing average is not implemented

    Tasks

    * a. Rating should use 5 stars with average review result is filled in yellow inside them - Average not implemented
    * b. Reviews should be displayed in the product detail page for relevant items only &#9745;

### #08 Registering account

  * Acceptance criteria : Clear and easy login page and ensure the necessary validation works and feedback returned to the user &#9745;

    Tasks

    * a. Register button located in the navbar is visible to any site visitor who are not logged in &#9745;
    * b. Register page contains minimum required fields for the user to sign up &#9745;
    * c. Email field is required and verification emails should be sent with link to confirm the email authentication &#9745;
    * d. Password confirmation input is required &#9745;

### #09 Login/Log out 

  * Acceptance criteria : Login/Logout button easily accessed from navbar &#9745;

    Tasks

    * a. Login button should be replaced to log out button once users logged in &#9745;
    * b. Logout button should open logout confirmation page &#9745;
    * c. Login/Log out status should return a feedback message &#9745;

### #10 Password recovery

  * Acceptance criteria : Email verification to recover password

    Tasks

    * a. Forgot password button should send a email to the registered email account with a link to reset password &#9745;

### #11 Email verification on registration

  * Acceptance criteria : Ensure the email is sent in order for registration to be completed &#9745;

    Tasks

    * a. Ensure the email delivery is successful &#9745;
    * b. Email body should include the link to verify email for successful registration &#9745;

### #12 User profile page

  * Acceptance criteria : User profile is accessible when user is registered. Validate all the entry when entered &#9745;

    Tasks

    * a. Form should include the delivery information so that user can retrieve the information when shopping &#9745;
    * b. Profile page should include the order history &#9745;

### #13 Sign up to newsletter

  * Acceptance criteria : Newsletter signup located in footer. Site users can register to receive newsletter &#9745;


    Tasks

    * a. Opted users can receive emails on product related news - Tested to ensure the email address is registered ready to receive emails &#9745;

### #14 Sorting products

  * Acceptance criteria : Fully functioning sorting is present in shop page. As products number is small to start with, this function is set as Could Have


    Tasks

    * a. Sort by price and category - Not implemented
    * b. Ascending and descending sort option should be given - Not implemented

### #15 Filter by price range

  * Acceptance criteria : Price range can be set to filter the product that matches the price range - As products number is small to start with, this function is set as Should Have and other issues were prioritized

    Tasks

    * a. Price range can be set below the navbar - Not implemented
    * b. Returned result should include the number of items matched within the range - Not implemented

### #16 List of new/limited items

  * Acceptance criteria : New/special items added to the site is marked accordingly so that returning users can quickly filter them &#9745;

    Tasks

    * a. New and limited items marked with badges &#9745;
    * b. Filter function in place for the product list page &#9745;

### #17 Quantity and available stock

  * Acceptance criteria : State the number of available stocks clearly in the product detail page and prevent exceeding stock number in the shopping bag &#9745;

    Tasks

    * a. Up and down button to change quantity of the item to put in the bag &#9745;
    * b. Quantity modified reflects the bag immediately &#9745;
    * c. Stock availability is displayed to inform the shoppers and shoppers can not select any larger quantity to purchase &#9745;

### #18 View items in bag

  * Acceptance criteria : Numbers of the items in the cart is easily accessed from any page within the site &#9745;

    Tasks

    * a. Number of items and total price to be displayed in the navbar under the shopping cart icon. - Only total amount due to small space

### #19 Adjust bag items

  * Acceptance criteria : Increase/Decrease and remove functionality is present and working in the bag page &#9745;

    Tasks

    * a. Up and down arrow buttons located beside quantity and remove button or link nearby &#9745;
    * b. Pressing buttons reflects the change including total price straight away &#9745;

### #20 Making payment

  * Acceptance criteria : Retrieve the profile address information if available and validation for the form entry is working and payment information is successfully in stripe dashboard &#9745;
  
    Tasks

    * a. Stripe payment form functioning and sent to stripe to process &#9745; 
    * b. Webhook working before redirection &#9745;
    * c. Form validation present and working as intended &#9745;

### #21 Secure payment 

  * Acceptance criteria : Payment process constantly works without issues &#9745;

### #22 Order confirmation

  * Acceptance criteria : Oder detail page displayed on successful payment. Order history and status is available in profile page. &#9745;

    Tasks 

    * a. On successful checkout, users should be directed to "thank you for your order" page &#9745;
    * b. In user's profile, order history with order status should be displayed - Order status not implemented

### #23 Email confirmation after checking out

  * Acceptance criteria : Ensure that automated email is sent on completing each purchase &#9745;

    Tasks 

    * a. Email is sent to registered user &#9745;
    * b. Title should contain the order number &#9745;

### #24 Email when order is dispatched

  * Acceptance criteria : Automated email when the order status is changed to DISPATCHED - As this was a extra feature, other issues were prioritized and this feature was not implemented

### #25 Add a product
  * Acceptance criteria : Add product page is available to staff only and staff can add products &#9745;

    Tasks 

    * a. Ideally, product admin page created and made available only for staff status - Superuser can add product without images
    * b. Added product will be included in new item - need to set New tag manually &#9745;
    * c. For the minimum required feature, Django admin page must be made user friendly for superuser to easily enter new products &#9745;

### #26 Edit/update a product
  * Acceptance criteria : Edit product page is available and retrieves the existing data for staff to update the data. - Superuser can update product without images

    Tasks 

    * a. Edit product page link available in product management menu - Link available in both product list and detail pages
    * b. Access to the page is restricted to superuser only. &#9745;

### #27 Delete a product
  * Acceptance criteria : Delete product page is available and retrieves the existing data for staff to delete products. &#9745;

    Tasks 

    * a. Access to the page is restricted to superuser only. &#9745;
    * b. Confirm Delete button is present to avoid accidentally removing a product &#9745;

### #28 Blog Page
  * Acceptance criteria : Functioning blog page that any staff member can create, edit and post - As this was a extra feature, other issues were prioritized and this feature was not implemented

### #29 SEO
  * Acceptance criteria : Keywords, sitemap and robots.txt &#9745;

    Tasks 

      * a. Keywords research and included in the meta tag &#9745;
      * b. sitemap and robots.txt present &#9745;

### #30 SNS (Facebook)
  * Acceptance criteria : All necessary information is added and accurate in FACEBOOK page. &#9745;

    Tasks 

      * a. Facebook page with the site link &#9745;
      * b. State business description &#9745;

### #31 Contact us page
  * Acceptance criteria : Page should be accessible from anywhere in the site &#9745;

    Tasks 

      * a. Link should be located in the footer &#9745;
      * b. Required fields should be kept minimal to provide easy contact &#9745;



## Manual testing on each page.

### Navbar and Footer

Testing to ensure navigation and footer function and display as intended.

  * All links are tested to ensure that no broken links are present and user is directed to appropriate page. External links open in a new tab in the browser.
  * The navbar is visible as a hamburger menu on mobile devices.
  * Navigation menus reflect user login status and user's privilege.
  * Profile page link is visible and accessible for logged in users only
  * Product management menus are visible and accessible only for users with superuser status 
  * Search bar is tested to ensure that appropriate result returns. No result found message displays when no item for search words were returned.
  * Newsletter Signup - Ensure that email address is registered in mailchimp every time users enter their email address.
  
#### Landing page

  * Visual inspections are carried out to ensure that the images are showing properly in all device sizes.
  * All the buttons are tested to ensure that it opens appropriate page when clicked.
  * Category links will open product list page with appropriate filter applied.
  * All products and New Arrival buttons will open product list page with appropriate filter applied.

#### Product List page

 * All buttons and links to open the appropriate pages.
 * Filters such as category, tags or search results returns only related items
 * Images display 

#### Product Detail page

 * Main images switches by clicking or tapping appropriately on any device.
 * Quantity input form was tested with attempt of various numbers input to ensure it only allows valid numbers between 1 and stock amount. Input for decimal numbers are prevented as it results in server error.
 * KEEP SHOPPING button brings the page back to product list page.
 * ADD TO BAG button adds the item in the shopping bag, feedback in toast message displays and the shopping bag icon in the navbar reflect the change immediately.
 * Reviews displayed are only for the product selected.

#### Shopping bag page

 * Changing the quantity by + and - buttons and update link work and reflect the change as intended. Decimal numbers entries are prevented by disabling the manual input in the quantity field.
 * Quantity field can only update within stock numbers.
 * Delete link removes the selected item only from the shopping bag.
 * Buttons open the appropriate links.

#### Checkout page

 * Order details displays on the left side.
 * Order details reflect current items in the shopping bag.
 * Shipping info is prefilled if the user has updated their profile except name field.
 * User can manually input or modify the fields as needed.
 * Adjust bag button will return to the shopping bag page where users can make adjustments to their items.
 * Red warning texts to inform the total amount to be charged matches the order total.
 * With the testing payment details, Complete Order button will process the payment and record is updated in Stripe page.
 * Currently exceeding 10,000 euro per transaction results in the server error from stripe - This is noted in the FAQs page

#### Checkout success page

 * Toast message includes all necessary information including order number and email address.
 * All the information related to the order is included in the page include order number, order date, items in the order, shipping information and the amount of the order.

#### My Profile page

 * Shipping information located on the left for bigger screen and top for smaller devices.
 * If user has filled the fields previously, fields are prefilled.
 * Update information button reflect the changes made and return to the same page with up-to-date information.
 * Toast message displays to notify the change.
 * Order history is located on the right on the bigger screen and below the delivery information on smaller device screens.
 * Write a review link in purchase history opens create review page

#### Create/Edit review page

 * Create a test review to ensure that new review is properly created and listed in the review page.
 * Editing the review is tested to ensure the fields are prefilled with appropriate entries and update is reflected as expected.

#### Delete review page

 * Tested to ensure that this page is only accessible for review writer. Typing this url address with other user status redirects to home with an error message to state the user has no permission.
 * Confirmed that the review is removed from the reviews page and DB on pressing the delete button.

#### Reviews page

 * Ensure that all reviews have links to their reviewed product detail page.
 * Pagination is properly in place.
 * Images and contents of reviews display properly.

#### Product management page

 * Opening this page from the main menu should open the empty form to add a new product. Each fields have validation in place and product saves as expected.
 * If opened from edit link, it should retrieve the instance of the product.
 * All links for this page is restricted to superuser and ensured that access is denied for users with non-superuser status.

#### About the Site page

 * Visual inspection to ensure that page contains and displays appropriate information. 

#### Deleivery info page

  * Visual inspection to ensure that page contains and displays appropriate information. 

#### FAQs page

  * Visual inspection to ensure that page contains and displays appropriate information. 

#### Contact us page

 * Ensure that forms are validated, email sent also saved in the database on form submission.
 * Email delievery to the site owner is confirmed.

#### Register page

 * Tested in to ensure the validation works and email with confirmation link is provided.

#### Login page

 * Tested numerous times logging in using both emails and usernames.

#### Logout page

 * Tested to ensure that user status changes once the logout button is clicked and user will no longer to allow the restricted pages.


  [<<< Back to README](../../README.md)