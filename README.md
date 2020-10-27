># Full Stack Frameworks With Django 

## Milestone Project nr.4 -- *VINTAGE*

&nbsp;
- Repository
&nbsp;
- Live website
&nbsp;
- Wireframes

#
&nbsp;
This is my 4th and final project for the Full-Stack Web Development Diploma with Code Institute.
I have decided to design a fully functional e-commerce site - The Vintage.
The idea behind it this project came from my love for vintage and unique pieces. While doing research online I have came across various websites which have inspired me to create something of my own. 
&nbsp;
As I am fascinated by the world of fashion and very often browsing the internet, I would be very intrigued if I came across a small brand selling some golden items. Obviously as those products usually come with hefty price tag, you would also relay on their social media account to check they are who they are - which is something I would want to highlight on my page and have the social media accounts always visible. 
&nbsp;
The site is created on a full stack Django framework, deployed on Heroku and uses AWS S3 to host media and static files. While working locally it uses the Sqlite3 database. When deployed to Heroku - it uses Postgres database. Full authentication on site is provided by using Django Allauth. Super users have availability to add edit and delete items. Normal users can register/login to keep track of theirs orders. Plus their delivery details can be stored to provide better user experience and faster checkout.
#
&nbsp;
# Table of Contents

 1. User Experience 
	- User stories
	- Designs 
 2. Features
	 - Exisitng 
	 - Future
 3. Technologies Used
 4. Testing
	- Devices
	- Validation
	- User Scenarios
 5. Deployment 
 6. Credits

#
># USER EXPERIENCE
&nbsp;
Main goal of this website was to have a beautiful and easy mixture of vintage items in a modern setting. I wanted this site to be easy to navigate, to feel unique and have high quality images (there is a page that focuses mainly on images)
&nbsp;
The website is fully responsive, thanks to the bootstrap template I have used to develop the page - Amado. I have actually made a payment to use this template without featuring credits but I feel as this is a student project, I shouldn’t take credit for everything.
&nbsp;
#
### A user stories
&nbsp;
The websites allows for all kind of users to enjoy the features. You can be just a random unregistered visitor, potential buyer,  but you can also create an account to keep a track of your purchases and to store some of your information.

Site administrator is created in Django and it will be granted to owner of the page and their team - per request.

*Summing up:*

**A Visitor:**

You are able to browse through the whole page - you are able to add items to the cart - you can also review your order in the cart and proceed to checkout where you will be able to finalise your order. You have an option to create an account, but you can also complete the order anonymously.

**the Registered User:**

You can register or login if you already have an account. Once you are logged in you will have an access to My Profile tab. You will be able to see your order history but also update your details which will allow for a faster checkout as details are pulled through from database.

**Site Owner:**

Super user will be created via Django. He/she can access the profile via typing ‘/admin’ url into browser. They will be able to execute simple commands like editing or deleting an item from the site itself. In admin page admin can access all orders emails and all other details needed to maintain successful business.

#
### Design
&nbsp;
I have based my site on a template called Amado - live link https://colorlib.com/preview/theme/amado/  It came with own CSS (which also included fonts and some core images) and Javascript but I did ended up adding some small changes.

As mentioned above I have had this template in site for quite some time now. It has been amended slightly to the needs of the project and to fit the requirements but it has generally stayed very similar to original template. 

I have created basic wireframes and they are available to see as images **here**.  They are a simple representation of what I was hoping to achieve as my final project.  I didn't feel the need to create mockups like for my previous projects, due to the fact I was already aware of the colour scheme and general layout of the website. 

**Images**
&nbsp;
As this is a e-commerce website I felt images would play an important role. The template's landing page was a great example how images can be used to catch attention. Due to the fact I thought my site wold need some sort of information, I have amended the landing page to be a simple welcoming page and have included original design to take care of my newest arrivals. That way best pieces would be represented on a separate page, grabbing the attention by image quality and minimalistic design. 
Temporary logo has been designed by. 
&nbsp;
#
># Features 
&nbsp;
### Exisitng
&nbsp;
The layout of this multi-page website has been created with Bootstrap 4 grid and has 7 Django Apps. 

Template and static files have been created in the root application. Base template contains Head, Navbar, Subscription and Footer. All those are applicable to other apps by including base.html in their code. 
			- Head
Contains all necessary meta, favicon, scripts and links to local files. 
			- Navbar
Navbar is a fully responsive element, which collapses on the smaller devices. On the left top corner I have included my own logo. Below you will find all necessary links to move around the website with ease. There is also a Cart and Search Icon and some Social Media links. 
	- Subscription
Visitors can subscribe using EmailJS.
	- Footer
It contains copyright information and again links to some more important parts of the website.

&nbsp;
1. Home App
&nbsp;
This is the backbone of the page. It contains the landing page with interesting background image and Logo. You will find short paragraph inviting you to shop with two links - to actually go shopping and to next app - About us.
&nbsp;
2. About App
&nbsp;
Its a simple page containing two divs. One of them is an image which disappears on smaller devices and another contains short information about the owner. You will also find another link to Products page (to invite you to browse on every occasion)
&nbsp;
3. All Items App
&nbsp;
This view is split in two. One the left side you will have a column where you can sort the products by their category (there are 2 main categories - sunglasses and handbags) or by designer. 
&nbsp;
On the right you will find all products displayed in two columns. They are sortable by name and price.  Also on top you will have a number of all the products and depending on the category chosen, the number should change accordingly. By hovering over the items, image will change. The page contains also a name, designer and their price and little cart item, where you can put the item to the shopping bag swiftly. 
&nbsp;
By clicking on a single item you will be redirected to a Single Product view - which is way more detailed than everywhere else on the site. On top of previous information you will also find 4-image carousel and detailed description of the item. You will be able to add an item to the cart. 
A superuser will have additional options to edit or delete an item.
&nbsp;
4. New Arrivals App
&nbsp;
This is probably the most attention grabbing page including 9 images with short information about the items. Those images have a hover effect over them. This was a landing page on original Amado template but as explained above - I have amended it for a better user experience. 
On a click you are taken to 'single_product' view where you will find a full description of each item. 
&nbsp;
This page of the website can be amended by superuser to feature latest arrivals to the shop in admin panel (as the app comes with its own model and fixture.json)
&nbsp;
5. Cart App
&nbsp;
The shopping bag application has two main columns. First of all you will see detailed information what is in your shopping bag with option to delete an item. As the number of item for sell is usually 1, there is no option to amend it. 
&nbsp;
To the right there will be financial information of your order: price, delivery cost and grand total. From there there are couple of options available, either to keep shopping or proceed to checkout. 
&nbsp;
6. Checkout App
&nbsp;
Similar to shopping bag, this page has also two main section. Financial cart details to the right and to the left you will find a checkout information section, where the user needs to input their billing and credit card details. The credit card section is linked to Stripe. The form needs to be fully validated before submission and card (it can be a test card from Stripe page) also needs to be valid.
&nbsp;
7. Profile App
 &nbsp;
Following the flow of the design, this application also has two main sections. Default Billing information - where logged in user can store them and each time the new order is made, the info would be pulled through. And another section contains order history details (order number, date, items and full price). When clicked it loads original details of the order. 
&nbsp;
### Features still to implement 
&nbsp;
With little time left to polish off this project there are certain things I would like to have, but couldn't sort it in time frame given:
&nbsp;
- Full Subscription Service
I have looked for simple and fast solution for this and by browsing online I came across EmailJS free service, which allows me to send automated email thanking for the subscription. In the future I would like to link it to Django.
- Login via Social Links
I have seen Allauth give you an option to log in via 3rd party social accounts. I didn't have time to explore this further but I do believe going forward it is something to learn as people are more likely to create account via fastest possible route and also to minimise number of password to store. 
- Pagination 
As this is a vintage items page, I didn't feel the massive need to include the pagination option for this project, but I believe if the business was to grow, it would be necessary. As Amado came with pagination I believe this would be a simple process to implement it. 
- Sorting Options and Starring System 
I would probably be looking to add a bit more sorting options - especially if I was to include a starring option via people opinions.
&nbsp;

#
># Technology Used
&nbsp;
Here you can find the list of all the programmes used to create this website


- [**Colorlib**](https://colorlib.com/) - I sourced my website template from this site.

- [PyCharm](https://www.jetbrains.com/pycharm/)  -  IDE for developing this project.        
        
 - [GitHub](https://github.com)  - for remotely storing project's code.

 - [**AWS**](https://aws.amazon.com/) - **Amazon Web Services** was used to store the media and static files for the Heroku enabled live version of the site.

 - [Heroku](https://heroku.com/)  - to host the project.    
&nbsp;
**Front-End** 
- HTML - to build the foundation of the project.        
        
- CSS  - to style the project.

- [**Javascript**](https://en.wikipedia.org/wiki/JavaScript) - A number of elements on the site have **Javascript** functionality
&nbsp;
**Back-End** 

- [Python](https://www.python.org/)  - back-end programming language used in this project.             
        &nbsp;          
**Libraries and Frameworks**        
 - [Bootstrap](https://getbootstrap.com)  - main responsive modern front-end framework        
        
 - [Google Fonts](https://fonts.google.com/)  - to import fonts.        
        
 - [FontAwesome](https://fontawesome.com/)  - to provide icons used across the project.        
        
 - [JQuery](https://jquery.com/)  - to simplify DOM manipulation

-   
    Django](https://www.djangoproject.com/)  - Python framework for building the project.

-   [Gunicorn](https://pypi.org/project/gunicorn/)  - a Python WSGI HTTP Server to enable deployment to Heroku.
-   [Psycopg2](https://pypi.org/project/psycopg2/)  - to enable the PostgreSQL database to function with Django.
-   [Stripe](https://stripe.com/ie)  - to handle financial transactions.
-   [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)  - to style Django forms.
&nbsp;
#### Databases

-   [SQlite3](https://www.sqlite.org/index.html)  - a development database.
-   [PostgreSQL](https://www.postgresql.org/)  - a production database.


&nbsp;
#
># Testing
&nbsp;     
### Devices
&nbsp;
*Manual testing was carried out on mobile devices and desktop.*
I also tested the site in Developer Tools. Especially useful for this was Chrome and Safari. 
I used the full gamut of responsivity in Developer Tools, but I also tested on the specific resolutions.
[**BrowserStack**](https://www.browserstack.com/)  - Any platform that I couldn't test in developer tools or on my own devices, I tested here.
&nbsp;
### Validation
&nbsp;
The code has been validated using:      
      &nbsp;  
 - [W3C Mark-up Validation Service](https://validator.w3.org/)      
      
 - [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)      
       
 - app.py was tested through  [PEP8 Online](http://pep8online.com/)     
   validator. There was just complain about few lines being too long.    
    &nbsp;  

### User Scenarios
 &nbsp;
As a visitor I have tested all the links to see if navigation is working and have went through the process of creating an order through successful completion. 
1. Main Page
2. Browse the Products 
3. Add an Item to the cart - both via button or cart icon 
4. On the cart page clicked through either navbar or cart icon, all details of the order has been displayed correctly. 
5. Go through to checkout 
6. Fill in information and clicked Pay. 
7. With successful order redirected to checkout success page with order information. 
 &nbsp;
I have also tried to create account. Email has to be confirmed. 
 &nbsp;
 As registered user I have tried to log in and navigate to My Profile page.
 I have also tried to checkout to see if my stored information would be retrieved.
  &nbsp;
  As A site administrator I have checked if i can amend the products details or even delete an item or create an item and add it to the database. 
   &nbsp;


Overall the page is working fine. There are some outstanding bugs
&nbsp;
#### Failed bootstrap.min.css SourceMap Load 
&nbsp;
Upon load of site this error appears in the browser console: "DevTools failed to load SourceMap: Could not load content for [http://127.0.0.1:8000/static/css/bootstrap.min.css.map](http://127.0.0.1:8000/static/css/bootstrap.min.css.map): HTTP error: status code 404, net::ERR_HTTP_RESPONSE_CODE_FAILURE".
      
&nbsp;
# [](https://github.com/sneachda//#deployment)
># Deployement 

  &nbsp;
The Vintage project was developed using the PyCharm  and using GitHub for version control. It is hosted on the Heroku platform, with static files on  images being hosted in AWS S3 Basket.

### Local Deployment

To be able to run this project, the following tools have to be installed:

-   An IDE of your choice
-   [Git](https://git-scm.com/)
-   [PIP](https://pip.pypa.io/en/stable/installing/)
-   [Python3](https://www.python.org/download/releases/3.0/)

Apart from that, you also need to create accounts with the following services:

-   [Stripe](https://stripe.com/en-ie)
-   [AWS](https://aws.amazon.com/)  to setup the  [S3 basket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
-   [Gmail](https://mail.google.com/)

#### [](https://github.com/#directions)Directions

1.  You can clone this repository directly into the editor of your choice by pasting the following command into the terminal:  
    `git clone https://github.com/sneachda/`  
    Alternatively, you can save a copy of this repository by clicking the green button  **Clone or download**  , then  **Download Zip**  button, and after extract the Zip file to your folder.  
    In the terminal window of your local IDE change the directory (CD) to the correct file location (directory that you have just created).


2.  Set up environment variables.  
    Note, that this process will be different depending on IDE you use.  
    In this it was done using the following way:
    
    -   Create  `.env`  file in the root directory.
    -   Add  `.env`  to the  `.gitignore`  file in your project's root directory
    -   In  `.env`  file set environment variables with the following syntax:
    
    import os  
    os.environ["DEVELOPMENT"] = "True"    
    os.environ["SECRET_KEY"] = "<Your Secret key>"    
    os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public key>"    
    os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret key>"    
    os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH_Secret key>"    

  

3.  Install all requirements from the  **requirements.txt**  file putting this command into your terminal:  
    `pip3 install -r requirements.txt`
4.  In the terminal in your IDE migrate the models to crete a database using the following commands:  
    `python3 manage.py makemigrations`  
    `python3 manage.py migrate`
5.  Load the data fixtures(**categories**,  **products**,  **designers**,  ) in that order into the database using the following command:  
    `python3 manage.py loaddata <fixture_name>`
6.  Create a superuser to have an access to the the admin panel(you need to follow the instructions then and insert username,email and password):  
    `python3 manage.py createsuperuser`
7.  You will now be able to run the application using the following command:  
    `python3 manage.py runserver`
8.  To access the admin panel, you can add the  `/admin`  path at the end of the url link and login using your superuser credentials.

### Heroku Deployment

_To start Heroku Deployment process, you need to clone the project as described in the section above._  
To deploy the project to  [Heroku](https://heroku.com/)  the following steps need to be completed:

1.  Create a  **requirement.txt**  file, which contains a list of the dependencies, using the following command in the terminal:  
    `pip3 freeze > requirements.txt`
2.  Create a  **Procfile**, in order to tell Heroku how to run the project, using the following command in the terminal:  
    `web: gunicorn art_of_tea.wsgi:application`
3.  `git add`,  `git commit`  and  `git push`  these files to GitHub repository.  
    NOTE: these 1-3 steps already done in this project and included in the GitHub repository, but illistrated here as they are required for the successfull deployment to Heroku.  
    As well as that, other things that are required for the Heroku deployment and have to be installed:  **gunicorn**(WSGI HTTP Server),  **dj-database-url**  for database connection and  **Psycopg**  (PostgreSQL driver for Python). All of the mentioned above are  _already installed_  in this project in the requirements.txt file.
4.  On the  [Heroku](https://heroku.com/)  website you need to create a  **new app**, assigne a name (must be unique),set a region to the closest to you(for my project I set Europe) and click  **Create app**.
5.  Go to  **Resources**  tab in Heroku, then in the  **Add-ons**  search bar look for  **Heorku Postgres**(you can type  `postgres`), select  **Hobby Dev — Free**  and click  **Provision**  button to add it to your project.
6.  In Heroku  **Settings**  click on  **Reveal Config Vars**.
7.  Set the following config variables there:

KEY

VALUE

AWS_ACCESS_KEY_ID

`<your aws access key>`

AWS_SECRET_ACCESS_KEY

`<your aws secret access key>`

DATABASE_URL

`<your postgres database url>`

EMAIL_HOST_PASS

`<your email password(generated by Gmail)>`

EMAIL_HOST_USER

`<your email address>`


SECRET_KEY

`<your secret key>`

STRIPE_PUBLIC_KEY

`<your stripe public key>`

STRIPE_SECRET_KEY

`<your stripe secret key>`

STRIPE_WH_SECRET

`<your stripe wh key>`

USE_AWS

`True`

8.  Copy  **DATABASE_URL's value**(Postrgres database URL) from the Convig Vars and temporary paste it into the default database in  **settings.py**.  
    You can temporary comment out the current database settings code and just paste the following in the settings.py:

  DATABASES = {     
        'default': dj_database_url.parse("<your Postrgres database URL here>")     
    }

Important Note: that's just temporary set up, this URL  **should not be committed and published to GitHub**  for security reasons, so make sure not to commit your changes to Git while the URL is in the settings.py.  
9. Migrate the database models to the Postgres database using the following commands in the terminal:  
`python3 manage.py makemigrations`  
`python3 manage.py migrate`  
10. Load the data fixtures(**categories**,  **products**,  **designers**) into the Postgres database using the following command:  
`python3 manage.py loaddata <fixture_name>`  
11. Create a  **superuser**  for the Postgres database by running the following command(_you need to follow the instructions and inserting username,email and password_):  
`python3 manage.py createsuperuser`  
12. You need to remove your Postgres URL database from the settings and uncomment the default DATABASE settings code in the settings.py file.  
Note: for production you get the environment variable 'DATABASE_URL' from the Heroku Config Vars and use Postgress database, while for development you use the SQLite as a default database.  
13. Add your Heroku app URL to  **ALLOWED_HOSTS**  in the settings.py file. 14. You can connect Heroku to GitHub to automatically deploy each time you push to GitHub.  
To do so, from the Heroku dashboard follow the steps:

-   **Deploy**  section ->  **Deployment method**  -> select  **GitHub**
-   link the Heroku app to your GitHub repository for this project
-   click  **Enable Automatic Deploys**  in the Automatic Deployment section
-   Run  `git push`  command in the terminal, that would now push your code to both Github and Heroku, and perform the deployment.

Alternatively, your can deploy using Heroku CLI:


15.  After successful deployment, you can view your app bu clicking  **Open App**  on Heroku platform.

&nbsp;
##### Hosting media files with AWS

The  **static files**  and  **media files**  (that will be uploaded by superuser - product/service images) are hosted in the  [AWS S3 Bucket](https://aws.amazon.com/). 

#
### [](https://github.com/sneachda/#credits)
># Credits


&nbsp;
>**Code Used**

&nbsp;
 **Amado Template**
&nbsp;
The template used to create the site.

-   Source:  [https://colorlib.com/wp/template/amado/](https://colorlib.com/wp/template/amado/)
-   Preview Site:  [https://colorlib.com/preview/#amado](https://colorlib.com/preview/#amado)
&nbsp;
**Boutique Ado**
&nbsp;
I learned so much while creating the above Code Institute mini-project. 
As previous projects gave me enough knowledge on front end design, this one really let me explore what it means to be a Full Stack developer. 

I do feel I had to lean heavily on the Boutique Ado's python code - to get such a complex site designed and up and running in a relatively short period of time. The whole Fullstack Frameworks & Django module was heavily investigated while creating this website. I had also looked around other students project for inspiration and ideas and how they married their own code with course material.
&nbsp;

**Images Used**
&nbsp;
I have used the images and all items description from another fabulous vintage website. Therefore I have no rights to them and if I was to develop this site for professional purposes, I would use my own material. 
( [Jean Vintage](https://www.jeanvintage.co.uk/) ) 

&nbsp;
>## Disclaimer     
    
 _The content of this website is for educational purposes only._