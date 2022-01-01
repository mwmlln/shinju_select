# Testing

## Automated Testing

------- Comlete this area if automated testing is done


### Testing using Django Unittest

-------- Comlete this area if automated testing is done

## User Story testing

Issue No. | Title | Acceptance criteria | Manual test carried out
----------|-------|---------------------|-------
#01 | Create Landing page |  State clear purpose of the site in the page and no confusing elements for site visitors | &#9745;
#02 | View a list of the products | Create product list page with clear display of the products | &#9745;
#03 | View specific categry of products | Create category buttons to filter by category and ensure the appropriate items are displayed | &#9745;
#04 | View individual product details | Product detail page to display the product info in details and button to add the item in the bag with quantity and sizing options where applicable | &#9745;
#05| Filter/Tag special items | Special items list can be selected and displayed in the product list page | &#9745;
#06 | Total price and number of items in the bag |  Display the number of items and total price under bag icon in the navbar | &#9745;
#07 | Product ratings/Reviews |  Use rating with stars and reviews for items displayed in product detail page | &#9744;
#08 | Registering account |  Clear and easy login page and ensure the necessary validation works and feedback returned to the user  | &#9745;
#09 | Login/Log out | Login/Logout button easily accessed from navbar | &#9745;
#10 | Password recovery |  Email vilification to recover password | &#9744;
#11 | Email verification on registration |  Ensure the email is sent when registration is completed | &#9744;
#12 | User profile page |  User profile is accessible when user is registered and validate all the entry when entered | &#9745;
#13 | Sign up to newsletter | Newsletter signup located in footer registers the emails and deliver the newsletter | &#9744;
#14 | Sorting products |  Fully functioning sorting is present in shop page | &#9744;
#15 | Filter by price range | Price range can be set to filter the product that matches the price range | &#9744;
#16 | List of new/limited items |  New/special items added to the site is marked new so that returning users can quickly filter them | &#9744;
#17 | Quantity and available stock  | Clear feed back and display for items in the cart | &#9745;
#18 | View items in bag | Numbers of the items in the cart is easily viewed from any page within the site | &#9745;
#19 | Adjust bag items |  Increase/Decrease and remove functionality is present and working in the bag page | &#9744;
#20 | Making payment | Retrieve the profile address information if available and validation for the form entry is working and payment information is successfully in stripe dashboard | &#9745;
#21 | Secure payment |  Profile record is only available to its user and staff and payment page is secure  | &#9745;
#22 | Order confirmation |  Oder detail page displayed on successful payment. Order history and status is available in profile page. | &#9744;
#23 | Email confirmation after checking out |  Ensure that automated email is sent on completing each purchase | &#9744;
#24 | Get a email when product is dispatched |  Automated email when the order status is changed to DISPATCHED  | &#9744;
#25 | Add a product |  Add product page is available to staff only and staff can add products | &#9744;
#26 | Edit/update a product |  Edit product page is available and retrieves the existing data for staff to update the data.  | &#9744;
#27 | Delete a product |  Delete product page is available and retrieves the existing data for staff to delete products.  | &#9744;
#28 | Blog Page |  Functioning blog page that any staff member can create, edit and post | &#9744;
#29 | SEO |Keywords, sitemap and robots.txt | &#9744;
#30 | SNS (Facebook) | All necessary information are added and accurate in FACEBOOK page. | &#9744;
#31 | Contabe act us page | Page should ccessible from anywhere in the site | &#9744;
#32 | Automated testing |Automated testing in addition to manual testing | &#9744;


## Manual testing on each page.

### Navbar and Footer

Manual testing to ensure navigation and footer function and display as intended.

* All links are tested to ensure that no broken links are present and user is directed to appropriate page. External links opens in a new tab in the browser.

* Navigation menus reflect user login status and user's privilege 
  Profile page link is visible and accessible for logged in users only
  Product management manus are visible and accesible only for users with superuser status 

* Newsletter Signup ---- Fill it here when implemented and tested -------
  
#### Landing page

**Users who have not logged in**  

Visual inspections are carried out to ensure that the images are showing properly in all device sizes. All the bottons are tested to ensure that it opens appropriate page when clicked.

**Registered and logged in users**


#### Product List page


#### Product Detail page


#### Shoppint bag page




#### Profile Edit page


#### About the Site page


#### Register page


#### Login page


#### Logout page




  [<<< Back to README](../../README.md)