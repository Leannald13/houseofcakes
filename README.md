House of Cakes

This project aims to pull together everything I have learned for the duration of the course at The Code Institute. The project includes Python, Django, HTML, CSS and JavaScript and also uses Stripe to process payments.
My inspiration for this project came from my own experience of trying to find nice cakes that do not contain gluten or dairy. As a result, I have developed recipes over the last few years to make cakes that taste just as good as those containing gluten and dairy.

UX:

User Stories

As a user of this platform I will be able to:
•	Register on the account but adding my email address, username and password.
•	Login with my username/email and password.
•	Log out.
•	I will be able to search for what I want using the search bar which will show results from both the title of the cake and the description of the cake.
•	I will be able to browse all products.
•	I will be able to find out more about each product but clicking on the ‘find out more’ button.
•	I will be able to add cakes to a shopping cart and I will be able to see how many items I have in my cart by looking at the navigation bar which tells me my items have been added.
•	From the page (product_detail.html) I will be able to go use the ‘back’ button to browse more cakes and I will also be able to proceed to checkout.
•	The checkout page will allow me to amend the number of items in my cart by increasing or decreasing.
•	I will see my order items at the top of the checkout page and I will be able to input my delivery details and card details. My payment will be processed when I press the ‘submit’ button.
•	I will be able to leave a review/comment on the cakes I have purchased on the product_detail.html page.
•	I will be able to contact House of Cakes by filling out the contact form and when I press submit, my message is sent.

Wireframes
Located in my github repo for desktop and mobile

Design
To assist with the design of the website I used a navbar, form cards and buttons from Bootstrap. The aim of this website was to create a design that was elegant and I attempted to keep the design simple and not overcrowd the page with too much information. 
I used resources available to me on Slack by the tutors and used the following document a guide: https://code-institute-room.slack.com/archives/C7J2ZAVHB/p1556827813043100
•	I maintained website conventions to allow a user to find what they want easily eg. navbar at the top, clearly labelled buttons, search field at the top of the page.
•	I used subtle but effective user actions for example buttons change colour when buttons are hovered over.
•	I provided bite size information and ensured not to overload the user with information.
•	I have attempted to create a simple design which does not force the user to "go looking" for what they want.
•	I used styling commonly found on modern websites (see link above) such as border radius for buttons to make the edges “less-sharp” and borders.
Colours
•	Due to using a large number of images which provide colour, I chose a simple background colour which would not clash with the colour of the images, however I placed all my products within a coloured card to not only make the page look tidy but also making it easy for the user to know where to look i.e the bolder colour directs the eye towards it.
•	According to information on the web, a pale blue (similar to a sky blue) has a calming and peaceful and connotation. https://www.canva.com/colors/color-meanings/light-blue/. I also used grey and white as they are neutral and modern colours.

Colour Palettes I took inspiration from:
https://www.shutterstock.com/blog/wp-content/uploads/sites/5/2019/05/20-Pastel-Color-Palettes-19-resize.jpg

Typography
•	I chose ‘Satify’ for the titles across the site as I felt this was readable but elegant and easy to read.
•	I chose ‘Rubik’ as my main font which I felt was clear and easy to read.

Icons
•	I made use of the icons from the Bootstrap icons library for things such as social media icons in the footer.

Features

Base
All pages contain a navigation bar at the top of the page on desktop and a footer at the bottom of each page. The navbar and footer becomes a mobile friendly navbar when the user uses a mobile or ipad device. This navbar allows the user to jump to the following pages:
•	Home page – this is the landing page for the website. It includes the navbar, footer, some images of cakes and a brief introduction about House of Cakes. The items on the home page are there to tell the user what the website is about, and to create something that makes the user want to buy cakes from the website
•	‘Shop’ provide the list of products available to the user. The page is displayed with 3 cakes per row, in a row of 3. Each cake is presented as a simple card providing the user with a bitesize of information, an image, and a button leading them to a page with more details on the product.
•	Login/register/logout – allowing the user to register their details, log in or logout. A log in is required to perform a number of tasks i.e. proceed to checkout.
•	‘Cart’ taking the user directly to their shopping cart.
•	‘Contact’ allowing the user to complete a form outlining their query. 
