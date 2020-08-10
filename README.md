# House of Cakes

</div>

## Table of Contents
1. [**UX**](#ux)
    - [**Project Introduction**](#project-introduction)
    - [**User Stories**](#user-stories)
    - [**Wireframes**](#wireframes)
    - [**Design Decisions**](#design-decisions)


2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies used**](#technologies-used)

4. [**Testing**](#testing)

5. [**Deployment**](#deployment)
    - [**Deployment to Heroku**](#deployment-to-heroku)

6. [**Credits**](#credits)

7. [**Acknowledgment**](#acknowledgment)

## Project Introduction

This project aims to pull together everything I have learned for the duration of the course at The Code Institute. The project includes Python, Django, HTML, CSS and JavaScript and also uses Stripe to process payments.
My inspiration for this project came from my own experience of trying to find nice cakes that do not contain gluten or dairy. As a result, I have developed recipes over the last few years to make cakes that taste just as good as those containing gluten and dairy.

## UX:

### User Stories

As a user of this platform I will be able to:
-	Register on the account by adding my email address, username and password.
-	Login with my username/email and password.
-	Log out.
-	I will be able to search for what I want using the search bar which will show results from both the title of the cake and the description of the cake.
-	I will be able to browse all products available.
-	I will be able to find out more about each product but clicking on the ‘find out more’ button.
-	I will be able to add cakes to a shopping cart and I will be able to see how many items I have in my cart by looking at the navigation bar which tells me my items have been added to the cart.
-	From the page (product_detail.html) I will be able to use the ‘back’ button to browse more cakes and I will also be able to proceed to checkout.
-	The checkout page will allow me to amend the number of items in my cart by increasing or decreasing.
-	I will see my order items at the top of the checkout page and I will be able to input my delivery details and card details. My payment will be processed when I press the ‘submit’ button.
-	I will be able to leave a review/comment on the cakes I have purchased on the product_detail.html page.
-	I will be able to contact House of Cakes by filling out the contact form and when I press submit, my message is sent.

## Wireframes
Located in my github repo for desktop and mobile

## Design
To assist with the design of the website I used a navbar, form, cards and buttons from Bootstrap. The aim of this website was to create a design that was elegant and I attempted to keep the design simple and not overcrowd the page with too much information. 
I used resources available to me on Slack by the tutors and used the following document a guide: https://code-institute-room.slack.com/archives/C7J2ZAVHB/p1556827813043100
-	I maintained website conventions to allow a user to find what they want easily eg. navbar at the top, clearly labelled buttons, search field at the top of the page.
-	I used subtle but effective user actions for example buttons change colour when buttons are hovered over.
-	I provided bite size information and ensured not to overload the user with information.
-	I have attempted to create a simple design which does not force the user to "go looking" for what they want.
-	I used styling commonly found on modern websites (see link above) such as border radius for buttons to make the edges “less-sharp” and borders.
### Colours
-	Due to using a large number of images which provide colour, I chose a simple background colour which would not clash with the colour of the images, however I placed all my products within a coloured card to not only make the page look tidy but also making it easy for the user to know where to look i.e the bolder colour directs the eye towards it.
-	According to information on the web, a pale blue (similar to a sky blue) has a calming and peaceful and connotation. https://www.canva.com/colors/color-meanings/light-blue/. I also used grey and white as they are neutral and modern colours.

Colour Palettes I took inspiration from:
https://www.shutterstock.com/blog/wp-content/uploads/sites/5/2019/05/20-Pastel-Color-Palettes-19-resize.jpg

### Typography
-	I chose ‘Satify’ for the titles across the site as I felt this was readable but elegant and easy to read.
-	I chose ‘Rubik’ as my main font which I felt was clear and easy to read.

### Icons
-	I made use of the icons from the Bootstrap icons library for things such as social media icons in the footer.

## Features

### Existing Features

-   Navbar - displays on every page of the website. Nabar collapses to a mobile view on mobile and ipad. Navbar allows the user to navigate
    to: 'home', 'shop', 'login', 'register', 'logout', 'cart' and 'contact'.
-   Footer - displays on every page of the website. Provides the user with social media links.
-	Home page – this is the landing page for the website containing some images and a brief introduction about House of Cakes. The aim of the home page is there to tell the user what the website is about, and to create something that makes the user want to buy cakes from the website
-	‘Shop’ provide the list of products available to the user. The page is displayed with 3 cakes per row, in a row of 3. Each cake is presented as a simple card (from Boostrap) providing the user with a bitesize of information, an image, and a button leading them to a page with more details on the product.
-   From the 'shop' page, the user can click the 'find out more' button which takes them to an individual page on each cake. On this page, a user can read and add comments/reviews. In addition, this page provides 3 buttons allow the user to do 3
    things; 'keep shopping', taking the user back to 'shop', 'add to cart', adds item to cart ( number of items in the 'cart' displays on navbar),
    'checkout', allowing the user to proceed to checkout and pay for their items.
-	Login/register/logout – allowing the user to register their details, log in or logout. A log in is required to perform a number of tasks i.e. proceed to checkout, leave a comment.
-	‘Cart’ taking the user directly to their shopping cart where the user can either proceed to checkout, or amend the number of items in their cart.
-	‘Contact’ allowing the user to complete a form outlining their query. When the user presses 'submit', the email is sent to my gmail account.

### Features left to implement

- User profile
- Order confirmation through to email and a previous orders page.
- Delete cart item view
- Delete comment


## Technologies Used

[HTML](https://en.wikipedia.org/wiki/HTML) - Used as the base for the project
[CSS](https://www.w3schools.com/css/) - Used as the base for cascading styles.
[Bootstrap](https://getbootstrap.com/) - Used for the design framework.
[Github](https://github.com/) - Used to hold my repository and deploy website.
[Google Fonts](https://fonts.google.com/) - Used to import specific fonts I wanted to use on my website.
[Python](https://www.python.org/)- The language used to build the backend of the website.
[Django](https://www.djangoproject.com/) - Python framework used in order to build out the routes/views of my website.
[JavaScript](https://www.javascript.com/) - Used as part of Stripe payments.
[Heroku](https://id.heroku.com/login) - Used to deploy my website.
[Stripe](https://stripe.com/gb) - Used to deploy my website.
[Postgres](https://www.postgresql.org/) - A robust database provided by Heroku for production development.
[Sqlite3](https://www.sqlite.org/index.html) - A database provided by Django.
[AWS S3](https://aws.amazon.com/s3/) - A storage service used to hold my static files.


## Testing

|   Manual Test                                                      | Desired Outcome                                                              | Outcome  |
| -------------                                                      |:-------------:                                                               | -----:|
| Navbar > click 'shop'                                              | directed to all cakes                                                        | Pass |
| Navbar > click 'login'                                             | Login with email & password. Details remembered                              | Pass |
| Navbar > click 'register                                           | Register with personal details. Details remembered                           | Pass |
| Navbar > click 'log out'                                           | Click logout. User is locked out                                             | Pass |
| Navbar > click 'cart'                                              | Show cart items if items are in the cart. If not "Your cart is now empty"    | Pass |
| Navbar > click 'contact'                                           | Contact form. All fields mandatory. Email received upon 'submit'             | Pass |
| 'Shop' > click find out more                                       | directs user to product details page                                         | Pass |
| 'Search bar' > search cake                                         | displays search items from title and description                             | Pass |
| 'product detail' > click 'keep shopping'                           | takes user back to 'shop'                                                    | Pass |
| 'product detail' > click 'add to cart'                             | add items to cart, displays also on navbar                                   | Pass |
| 'product detail' > click 'checkout'                                | takes user to 'checkout page'                                                | Pass |
| 'product detail' > type comment > press submit                     | form only displays if user. User comment and username posted.                | Pass |
| 'product detail' > click 'checkout'                                | takes user to checkout page                                                  | Pass |
| 'checkout' > amend quality > click amend quantity                  | quantity and order total is updated                                          | Pass |
| 'checkout' > click 'checkout'                                      | user directed to checkout page                                               | Pass |
| 'checkut' > input delivery details & card details > click 'paynow' | page refreshes and directs back to 'home'                                    | Pass |
| Footer > click 'facebook icon'                                     | user directed to Facebook                                                    | Pass |
| Footer > click 'instagram icon'                                    | user directed to Instagram                                                   | Pass |
| Footer > click 'twitter icon'                                      | user directed to Twitter                                                     | Pass |

### Mobile & ipad

The same tests as above were carried out on both mobile and ipad devices, with the same outcomes.

### Code Validators
I put my code through validators for my HTML, CSS, JavaScript and Django. I found a few errors such as:
- trailing whitespace
- missing 'div' end tags.
I resolved these issues and ran the code through the validators again until the validators confirmed no errors.

### Browser Testing

- Google Chrome - passed
- Internet Explorer - passed
- Firefox - passed


### Notable bugs 

I have created a 'contact' form which submits emails to my gmail account. I was advised from the Code Institute tutors that Gitpod
does not handle emails well and to therefore test the emails directly from Heroku instead. The emails are received when sent
directly to Heroku. I also found it challenging to get my base.css to respond after setting up my AWS S3 Bucket, even after using the command "python3 manage.py collectstatic".
I found that after running 'collect static' and pushing to github, some css code would still not take. Despite it not being best practice to put that code
into the html template, for those classes and id's I struggled with, I included in the template to try and have my mobile and ipad view look as accurate
as possible.

## Deployment

1) Register for Heroku and once signed in click the "New" button on the dashboard to create a new app.

2) In Heroku Name the app and specify the region.

3) Create a requirement.txt file to allow Heroku to install the required dependencies to run the app. The CLI text to input is as follows pip3 freeze --local > requirements.txt.

4) Create a Procfile to inform Heroku what type of app is being deployed echo web: python run.py > Procfile.

5) In the CLI of you IDE input the following: $ heroku login $ heroku git:remote -a $ git push heroku master

6) https://houseofcakes.herokuapp.com/

## Credits

- All image links were taken from Google searches
- I used the mini project Boutique Ado to help throughout my project and used aspects of the code and amended it to my
specifications.
- I used [Stack Overflow](https://stackoverflow.com/) and [W3Schools](https://www.w3schools.com/) throughout my project
to assist with resolving bugs and error messages.
- I received alot of support from Scott (CI tutor) to get my Stripe payments working.
- I looked at a number of peer code to give me model ideas and help me with various challenges particularly with my chosen 
models 'Contact' and 'Comment'.
https://github.com/jboyd8/jamieboydphotography
https://github.com/EliasOPrado/tour-project
https://github.com/ShavingSeagull/Herculean
https://github.com/RobSimons1/ms4-ecommerce
https://github.com/tomciosegal/nutri-store

## Acknowledgments

I would very much like to thank my wonderful mentor, Anthony Ngene who has been amazing, not just on this project, but the entire way through this course.
I would also like to thank Scott, a CI tutor who gave me alot of his time when I was struggling with Stripe Payments; I don't know how
I would have done it without him - he is an absolute sport! Thank you to JoWings (alumni from Slack) who helped me late on a Saturday night 
when I couldn't push to github because a Core.Microsoft file had appeared in my code, and I had no idea what to do.
Finally to a few of the CI tutors who are always patient, supportive and never make it difficult to ask for help; Haley and Anna.


