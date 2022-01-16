# Testing

## Automated Testing

### Testing using Django Unittest




## User Story testing


### #01 Create Landing page

  * Acceptance criteria - State clear purpose of the site in the page and no confusing elements for site visitors &#9745;
  
    Tasks
    * a. There should be a button to open the product page clearly visible when the landing page is opened so that the site victors can easily move to the page to see the products &#9745;
    * b. Pages should be responsive in all screen sizes &#9745;
    * c. Home button in Navbar and About page button should be located in footer so that site user can access these pages anywhere within the site &#9745;

### #02 View a list of the products

  * Acceptance criteria : Create product list page with clear display of the products &#9745;

  Tasks

  * a. 4 products listed in a row and 2 rows per page. Pagination in place for 8 items  - changed to 3 products in a row and 12 per page to inmprove the visual impact of the products &#9745;
  * b. Product name, price and category is listed under the product image &#9745;

  * c. Sort bar and price filter should be located at the top - Not implemented

### #03 View specific categry of products

  * Acceptance criteria : Create category buttons to filter by category and ensure the appropriate items are displayed &#9745;

  Tasks

  * a. category buttons in the landing page and product list page - only impletemted in landing page &#9745;
  * b.  Choosing category should only displays the chosen category products &#9745;
  * c. There should be 4 categories at least as a start up &#9745;

### #04 View individual product details

  * Acceptance criteria : Product detail page to display the product info in details and button to add the item in the bag with quantity and sizing options where applicable &#9745;

  Tasks

  * a. Product images display on the left &#9745;
  * b.  Product name, adjust size and quantity, price, category, back to shopping page link and add button on the right - Size option not implemented 
  * c. Product description below the image and buttons - Changed to the side as it looked neater
  * d. Product review box at the bottom of the page - Not implemented 

### #05 Filter/Tag special items

  * Acceptance criteria : Special items list can be selected and displayed in the product list page &#9745;

  Tasks

  * a. Special items link included in the category - changed to independent tag from category for easier filtering &#9745;
  * b.  Special items should have budges to make them stand out in the list &#9745;

### #06 Total price and number of items in the bag

  * Acceptance criteria : Display the number of items and total price under bag icon in the navbar &#9745;

  Tasks

  * a. Number of items in the bag and total price visible under the cart icon at all times if there is anything in the bag &#9745;

### #07 Product ratings/Reviews

  * Acceptance criteria :  Use rating with stars and reviews for items displayed in product detail page - Displaying the reviews in product detail page and showing average are not impletement 

  Tasks

  * a. Rating should use 5 stars with average review result is filled in yellow inside them &#9745;
  * b. Reviews should be displayed in the product detail page for relevant items only - changed to independent review page. 

### #08 Registering account

  * Acceptance criteria : Clear and easy login page and ensure the necessary validation works and feedback returned to the user &#9745;

  Tasks

  * a. Register button located in the navbar is visible to any site visitor who are not logged in &#9745;
  * b. Register page contains minimum required fields for the user to sign up &#9745;
  * c. Email entry is required and confirmation emails should be sent with link to confirm the email authentication &#9745;
  * d. Password confirmation input is required &#9745;

### #09 Login/Log out 

  * Acceptance criteria : Login/Logout button easily accessed from navbar &#9745;

  Tasks

  * a. Login button should be replaced to log out button once users logged in &#9745;
  * b. Logout button should bring to the logout confirmation page &#9745;
  * c. Login/Log out status should return a feedback message &#9745;

### #10 Password recovery

  * Acceptance criteria : Email vilification to recover password

  Tasks &#9745;

  * a. Forgot password button should send a email to the registered email account with a link to reset password &#9745;

### #11 Email verification on registration

  * Acceptance criteria : Ensure the email is sent in order for registration to completed &#9745;

  Tasks

  * a. Ensure the email delivery is successful &#9745;
  * b. Email body should include the link to valify email for successful registration &#9745;

### #12 User profile page

  * Acceptance criteria : User profile is accessible when user is registered and validate all the entry when entered &#9745;

  Tasks

  * a. Form should include the delivery information so that user can retrieve the information when shopping &#9745;
  * b. Profile page should include the order history &#9745;

### #13 Sign up to newsletter

  * Acceptance criteria : Newsletter signup located in footer registers the emails and deliver the newsletter &#9745;


  Tasks

  * a. Opted users can receive emails on product related news - Tested to ensure the email address is registered ready to receive emails &#9745;

### #14 Sorting products

  * Acceptance criteria : Fully functioning sorting is present in shop page. As products number is small to start with this functions is set as Could Have


  Tasks

  * a. Sort by price and category - Not implemented
  * b. Ascending and descending sort option should be given - Not implemented

### #15 Filter by price range

  * Acceptance criteria : Price range can be set to filter the product that matches the price range - As products number is small to start with this functions is set as Sould Have and other issues were prioritized

  Tasks

  * a. Price range can be set below the navbar - Not implemented
  * b. Returned result should include the number of items matched within the range - Not implemented

### #16 List of new/limited items

  * Acceptance criteria : New/special items added to the site is marked accordingly so that returning users can quickly filter them &#9745;

  Tasks

  * a. New and limited items marked with badges &#9745;
  * b. Filter function in place in the product list page &#9745;

### #17 Quantity and available stock

  * Acceptance criteria : State the number of available stock clearly in the product detail page and prevent exceeding stock number in the shopping bag &#9745;

  Tasks

  * a. Up and down button to change quantity of the item to put in the bag &#9745;
  * b. Quantity modified reflects the bag immediately &#9745;
  * c. Stock availability is displayed to inform the shoppers and shoppers can not select any larger quantity to purchase &#9745;

### #18 View items in bag

  * Acceptance criteria : Numbers of the items in the cart is easily viewed from any page within the site &#9745;

  Tasks

  * a. Number of items and total price to be displayed in the navbar under the shopping cart icon. &#9745;

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
  * c. Form validation present and working as intendedon &#9745;

### #21 Secure payment 

  * Acceptance criteria : Payment process constantly works without issues &#9745;

### #22 Order confirmation

  * Acceptance criteria : Oder detail page displayed on successful payment. Order history and status is available in profile page. &#9745;

  Tasks 

  * a. On successful checkout, users should be directed to "thank you for your order" page &#9745;
  * b. In user's profile, order history with order status should be displayed &#9745;

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

  * a. Ideally, product admin page created and made available only for staff status &#9745;
  * b. Added product will be included in new item - need to set New tag manually &#9745;
  * c. For the minimum required feature, Django admin page must be made user friendly for superuser to easily enter new products &#9745;

### #26 Edit/update a product
  * Acceptance criteria : Edit product page is available and retrieves the existing data for staff to update the data. &#9745;

  Tasks 

  * a. Edit product page link available in product management menu &#9745;
  * b. Access to the page is restricted to staff only. &#9745;

### #27 Delete a product
  * Acceptance criteria : Delete product page is available and retrieves the existing data for staff to delete products. &#9745;

  Tasks 

  * a. Access to the page is restricted to staff only. &#9745;
  * b. Confirm Delete button is present to avoid accidentally removing a product &#9745;

### #28 Blog Page
  * Acceptance criteria : Functioning blog page that any staff member can create, edit and post - As this was a extra feature, other issues were prioritized and this feature was not implemented

### #29 SEO
  * Acceptance criteria : Keywords, sitemap and robots.txt &#9745;

 Tasks 

  * a. Keywords research and included in the meta tag &#9745;
  * b. sitemap and robots.txt present &#9745;

### #30 SNS (Facebook)
  * Acceptance criteria : All necessary information are added and accurate in FACEBOOK page. &#9745;

 Tasks 

  * a. Facebook page with the site link &#9745;
  * b. state business description &#9745;

### #31 Contact us page
  * Acceptance criteria : Page should be accessible from anywhere in the site &#9745;

 Tasks 

  * a. Link should be located in the footer &#9745;
  * b. Required fields should be kept minimal to provide easy contact &#9745;



## Manual testing on each page.

### Navbar and Footer

Manual testing to ensure navigation and footer function and display as intended.

* All links are tested to ensure that no broken links are present and user is directed to appropriate page. External links opens in a new tab in the browser.

* The navbar is visible as a hamburger menu on mobile devices.

* Navigation menus reflect user login status and user's privilege 
  Profile page link is visible and accessible for logged in users only
  Product management manus are visible and accesible only for users with superuser status 

* Search bar is tested to ensure that appropriate result returns.
 Also No result found message displays when no item with search words were returned.

* Newsletter Signup  
Ensure that email address is registered in mailchimp every time users enter their email address.
  
#### Landing page

Visual inspections are carried out to ensure that the images are showing properly in all device sizes. All the bottons are tested to ensure that it opens appropriate page when clicked.

* Category links - these buttons were tested that they display correctly in all device sizes and clinking them will open product list page with appropriate filter applied.

* All products and New Arrival buttons - Ensure that buttons display properly in all device sizes and clinking the buttons open appropriate pages

#### Product List page

Display on all device sizes were checked to ensure there are no issues with any of the page elements visibility.
Testing was carried to check all buttons and links to open the appropriate pages.
Tested various filter on numbers of occations to ensure that appropriate items are displayed.

#### Product Detail page

Tested deisplay on all device sizes for responsiveness.
Image display is tested numbers of times to ensure that main images swiches on click or tap appropriately in any device.
Quantity input form was tested with attempt of various numbers input to ensure it only allows valid numbers between 1 and stock amount. Input for deciaml numbers are prevented as it results in server error.
KEEP SHOPPING button brings the page back to product list.
ADD TO BAG button adds the item in the shopping bag and feefback in toast message diaplays and cart in the navbar reflect the change immidiately.

#### Shoppint bag page

Tested deisplay on all device sizes for responsiveness.
Changing the quantity by + and - buttons and update link work and reflect the change as intended. Decimal numbers input are prevented from entered by disabling the manual input in the quantity field.
Delete link removes the selected item only from the shopping bag.
Buttons both open the page appropriately.

#### Checkout page

Tested deisplay on all device sizes for responsiveness.
Order details displays on the left side.
Order details reflect current items in the shopping bag.
Shipping info is prefilled if the user has updated thier profile except name field.
User can manually input or modify the fields as needed.
Adjust bag will return to the shopping bag page where users can make adjustments to their items.
Red warning textsto inform the total amount to be charged matches the order total.
With the testing payment details, Complete Order button will process the payment and record is updated in Stripe page.

#### Checkout success page

Tested deisplay on all device sizes for responsiveness.
Toast message includes all nessasary information including order number and email address.

All the informaion related to the order is included in the page include order number, order date, items in the order,shippping information and the amount of the order.

#### My Profile page

Shipping infomation located on the left for bigger screen and top for smaller devices.
If user has filled the fields previously, fields are prefilled.
Update informaion button reflect the changes made and return to the same page with up-to-date informaion.
Toast message displays to notify the change.
Order history is located on the right on the bigger screen and below the delivery infomation with smaller device screens.
Write a review link in purchase history opens create review page

#### Create/Edit review page

Tested to create a new review to ensure that new review is properly created and listed in the review page.
Editing the review is tested to ensure the fields are prefilled with appropriate entries and update reflect as expected.

#### Delete review page

Tested to ensure that this page is only accessible to review user. Typing this url address with other user status redirects to home with a error message to state the user has no permission.
Confirmed that the review is removed from the reviews page and DB on pressing the delete button.

#### Reviews page

Ensure that all reviews has links to their reviewed product detail page.
Pagination is properly in place.
Images and review contains display properly.

#### Product management page

Opening this page from the main manu should open the empty form to add a new product. Each fields have validation in place and product saves as expected.
If opened from edit/delete link, it should retreive the instance of the product.
All links for this page is restricted to superuser and ensured that access is denied for users with non-superuser status.

#### About the Site page

Responsiveness is tested to ensure all elements in the page display properly.

#### Deleivery info page#

Responsiveness is tested to ensure all elements in the page display properly. Ensured the image doesn't display to avoid congestion in smaller screen.

#### Contact us page

Responsiveness tested on all device sizes.
Test was carried out to ensure that forms are validated, email sent also saved in the database on submission of the form.
Email delievery to the site owner is confirmed.

#### Register page

Tested in to ensure the validation works and email with confirmation link is provided.

#### Login page

Tested numerous times loggin in using boths emails and usernames.

#### Logout page

Tested to ensure that user status cahnges once the logout button is clicked and user will no longer to allow the restricted pages.


  [<<< Back to README](../../README.md)