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
    - [**How to run this project locally**](#how-to-run-this-project-locally)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

7. [**Disclaimer**](#disclaimer)

## Project Introduction

This project aims to pull together everything I have learned for the duration of the course at The Code Institute. The project includes Python, Django, HTML, CSS and JavaScript and also uses Stripe to process payments.
My inspiration for this project came from my own experience of trying to find nice cakes that do not contain gluten or dairy. As a result, I have developed recipes over the last few years to make cakes that taste just as good as those containing gluten and dairy.

## UX:

### User Stories

As a user of this platform I will be able to:
•	Register on the account but adding my email address, username and password.
•	Login with my username/email and password.
•	Log out.
•	I will be able to search for what I want using the search bar which will show results from both the title of the cake and the description of the cake.
•	I will be able to browse all products available.
•	I will be able to find out more about each product but clicking on the ‘find out more’ button.
•	I will be able to add cakes to a shopping cart and I will be able to see how many items I have in my cart by looking at the navigation bar which tells me my items have been added.
•	From the page (product_detail.html) I will be able to go use the ‘back’ button to browse more cakes and I will also be able to proceed to checkout.
•	The checkout page will allow me to amend the number of items in my cart by increasing or decreasing.
•	I will see my order items at the top of the checkout page and I will be able to input my delivery details and card details. My payment will be processed when I press the ‘submit’ button.
•	I will be able to leave a review/comment on the cakes I have purchased on the product_detail.html page.
•	I will be able to contact House of Cakes by filling out the contact form and when I press submit, my message is sent.

## Wireframes
Located in my github repo for desktop and mobile

## Design
To assist with the design of the website I used a navbar, form cards and buttons from Bootstrap. The aim of this website was to create a design that was elegant and I attempted to keep the design simple and not overcrowd the page with too much information. 
I used resources available to me on Slack by the tutors and used the following document a guide: https://code-institute-room.slack.com/archives/C7J2ZAVHB/p1556827813043100
•	I maintained website conventions to allow a user to find what they want easily eg. navbar at the top, clearly labelled buttons, search field at the top of the page.
•	I used subtle but effective user actions for example buttons change colour when buttons are hovered over.
•	I provided bite size information and ensured not to overload the user with information.
•	I have attempted to create a simple design which does not force the user to "go looking" for what they want.
•	I used styling commonly found on modern websites (see link above) such as border radius for buttons to make the edges “less-sharp” and borders.
### Colours
•	Due to using a large number of images which provide colour, I chose a simple background colour which would not clash with the colour of the images, however I placed all my products within a coloured card to not only make the page look tidy but also making it easy for the user to know where to look i.e the bolder colour directs the eye towards it.
•	According to information on the web, a pale blue (similar to a sky blue) has a calming and peaceful and connotation. https://www.canva.com/colors/color-meanings/light-blue/. I also used grey and white as they are neutral and modern colours.

Colour Palettes I took inspiration from:
https://www.shutterstock.com/blog/wp-content/uploads/sites/5/2019/05/20-Pastel-Color-Palettes-19-resize.jpg

### Typography
•	I chose ‘Satify’ for the titles across the site as I felt this was readable but elegant and easy to read.
•	I chose ‘Rubik’ as my main font which I felt was clear and easy to read.

### Icons
•	I made use of the icons from the Bootstrap icons library for things such as social media icons in the footer.

## Features

### Existing Features

•   Navbar - displays on every page of the website. Nabar collapses to a mobile view on mobile and ipad. Navbar allows the user to navigate
    to: 'home', 'shop', 'login', 'register', 'logout', 'cart' and 'contact'.
•   Footer - displays on every page of the website. Provides the user with social media links.
•	Home page – this is the landing page for the website containing some images and a brief introduction about House of Cakes. The aim of the home page is there to tell the user what the website is about, and to create something that makes the user want to buy cakes from the website
•	‘Shop’ provide the list of products available to the user. The page is displayed with 3 cakes per row, in a row of 3. Each cake is presented as a simple card (from Boostrap) providing the user with a bitesize of information, an image, and a button leading them to a page with more details on the product.
•   From the 'shop' page, the user can click the 'find out more' button which takes them to an individual page on each cake. On this page, a user can read and add comments/reviews. In addition, this page provides 3 buttons allow the user to do 3
    things; 'keep shopping', taking the user back to 'shop', 'add to cart', adds item to cart ( number of items in the 'cart' displays on navbar),
    'checkout', allowing the user to proceed to checkout and pay for their items.
•	Login/register/logout – allowing the user to register their details, log in or logout. A log in is required to perform a number of tasks i.e. proceed to checkout, leave a comment.
•	‘Cart’ taking the user directly to their shopping cart where the user can either proceed to checkout, or amend the number of items in their cart.
•	‘Contact’ allowing the user to complete a form outlining their query. When the user presses 'submit', the email is sent to my gmail account.

### Features left to implement

• User profile
• Order confirmation through to email and a previous orders page.
• Delete cart item view


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

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

