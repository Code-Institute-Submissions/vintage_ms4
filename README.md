># Full Stack Frameworks With Django &nbsp; &nbsp;    
    
## Milestone Project nr.4 -- *VINTAGE*    
    
 &nbsp;    
- [Repository](https://github.com/sneachda/vintage_ms4)    
&nbsp;    
- [Live website](https://vintage-milestone4.herokuapp.com/)    
&nbsp;    
- [Wireframes](https://github.com/sneachda/vintage_ms4/tree/master/static/wireframes)    
    
# &nbsp;    
This is my 4th and final project for the Full-Stack Web Development Diploma with Code Institute.    
I have decided to create a fully functional e-commerce site - The Vintage.    
The idea behind it this project came from my love for vintage and unique pieces. While doing research online I have came across various websites which have inspired me to create something of my own.     
&nbsp;    
As I am fascinated by the world of fashion and very often browsing the internet, I would be very intrigued if I came across a small brand selling some rare items. Obviously as those products usually come with a hefty price tag, you would always do your due diligence and check their online presence.    
&nbsp;    
The site is created on a full stack Django framework, deployed on Heroku and uses AWS S3 to host media and static files. While working locally it uses the Sqlite3 database, but when deployed to Heroku - it's a Postgres database. Full authentication on site is provided by Django Allauth. Super users have availability to add, edit and delete items. Normal users can register/login to keep track of theirs orders. Plus their delivery details can be stored to provide better user experience and faster checkout.    

# &nbsp;    
# Table of Contents    
    
1. [User Experience](https://github.com/sneachda/vintage_ms4#--user-experience-)    
    - [User stories](https://github.com/sneachda/vintage_ms4#-a-user-stories)    
    - [Designs](https://github.com/sneachda/vintage_ms4#-design)     
 2. [Features](https://github.com/sneachda/vintage_ms4#-features)    
    - [Existing](https://github.com/sneachda/vintage_ms4#-existing)     
    - [Future](https://github.com/sneachda/vintage_ms4#-features-still-to-implement)    
 3. [Technologies Used](https://github.com/sneachda/vintage_ms4#-technology-used)    
 4. [Testing](https://github.com/sneachda/vintage_ms4#-testing)    
    - [Devices](https://github.com/sneachda/vintage_ms4#-devices)    
    - [Validation](https://github.com/sneachda/vintage_ms4#-validation)    
    - [User Scenarios](https://github.com/sneachda/vintage_ms4#-user-scenarioss)    
 5. [Deployment](https://github.com/sneachda/vintage_ms4#-deployment)    
 6. [Credits](https://github.com/sneachda/vintage_ms4#-credits)    
    
    
 #  
># [](https://github.com/sneachda/vintage_ms4#user-experience)  USER EXPERIENCE &nbsp;    
Main goal of this website was to invite visitors to browse around by having a beautiful mixture of vintage items set in a minimalistic and modern website. I wanted this webpage to be easy to navigate, to feel unique and have a high quality images (there is a page that focuses mainly on pictures)  that would make people want to buy the products.  
&nbsp;    
The website is fully responsive, thanks to the bootstrap template I have used to develop the page - Amado. I have actually made a payment to use this template without featuring credits but I feel as this is a student project, I shouldn’t take credit for anything that isn't mine.    
&nbsp;    
### [](https://github.com/sneachda/vintage_ms4#user-stories) A user stories    
 &nbsp;    
The website allows for users to enjoy all the features. You can be just a random, unregistered visitor or a potential buyer. You can also create an account to keep a track of your purchases and to store some of your information.    
&nbsp;  
****As a user, I want/expect:****  
  
- to view all the products without having to register  
      
- to create my own account, but also being able to checkout without creating an account  
  
- to store my order details and some useful account information   
  
- to log out any time and have the session terminated  
      
- to use the website from any device (laptop, tablet, mobile)    
  
****As a superuser, I expect:****   
- to add new items  
      
- to edit items  
      
- to delete items  
  
- have full control of all orders via admin page.
      
Site administrator is created in Django.  
    
*Summing up:*    
 **A Visitor:**    
 You are able to browse through the whole page - you are able to add items to the cart - you can also review your order in the cart and proceed to checkout where you will be able to finalise your order. You have an option to create an account, but you can also complete the order anonymously.    
    
**the Registered User:**    
 You can register or login if you already have an account. Once you are logged in you will have an access to My Profile tab. You will be able to see your order history, access the details of previously made orders but also update your details which will allow for a faster checkout as details are pulled through from database.    
    
**Site Owner:**    
 Super user will be created via Django. He/she can access the profile via typing ‘/admin’ url into browser. They will be able to execute simple commands like editing or deleting an item from the site itself. In admin page, admin can access all orders, emails and all other details needed to maintain a successful business.    
    
###[](https://github.com/sneachda/vintage_ms4#design) Design 
&nbsp;    
I have based my site on a template called [Amado](https://colorlib.com/preview/theme/amado/).  It came with own CSS (which also included fonts and some core images) and Javascript - but I did end up adding some small changes.    
    
As mentioned above I have had this template in my head for quite some time now. It has been amended slightly for the needs of this project and to fit the requirements but it has generally stayed very similar to the original as I feel all fitted well with my idea.  
 &nbsp;
I have created very basic wireframes and they are available to see as images [here](https://github.com/sneachda/vintage_ms4/wireframes).  They are a simple representation of what I was hoping to achieve as my final project.  I didn't feel the need to create mockups like for my previous projects, due to the fact I was already aware of the colour scheme and general layout of the website because of the template.   
&nbsp;   
**Images** &nbsp;    
As this is a e-commerce website I felt images would play an important role. The template's landing page was a great example how images can be used to catch attention. Due to the fact I thought my site wold need some sort of an extra information and explanation, I have amended the landing page to be a simple welcoming page and have included original design to take care of my newest additions. That way best pieces would be represented on a separate page, grabbing the attention by image quality and minimalistic design.     
Temporary logo has been designed by me.     
&nbsp;    
># [](https://github.com/sneachda/vintage_ms4#features) Features 


### [](https://github.com/sneachda/vintage_ms4#existing) Existing 
&nbsp;    
The layout of this multi-page website has been created with Bootstrap 4 grid and has 7 Django Apps.     
    
Template and static files have been created in the root application. Base template contains Head, Navbar, Subscription and Footer sections. All those are applicable to other apps by including base.html in their code.     
		- *Head*
         Contains all necessary meta, favicon, scripts and links to local files.     
         - *Navbar* 
         Navbar is a fully responsive element, which collapses on a smaller devices. On the left top corner I have included my own logo. Below you will find all necessary links to move around the website with ease. There is also a Cart and Search Icon and some Social Media links - I found it very useful that original design included the links in navbar, as with the second hand, expensive items - you would often check their online presence. Also it gives people an option to browse though business's instagram and find a lot of information that way. It's probably one of the easiest way to get in touch. Cart icon will update when item is put to shopping bag, showing a cost of the whole shopping bag  
		 - *Subscription* 
 Visitors can subscribe using EmailJS.    
		 - *Footer* 
 It contains copyright information and again links to some more important parts of the website.    
&nbsp;    
1. Home App    
&nbsp;    
This is the backbone of the whole website. It contains the landing page with interesting background - a grabbing attention image and Logo. You will find short paragraph inviting you to shop with two links - to actually go shopping and to the next app - About us.    
&nbsp;    
2. About App    
&nbsp;    
It's a simple page containing two divs. One of them is an image which disappears on a smaller devices and another contains short information about the intention of the website and business itself. You will find a basic information on how to get in touch. You will also find another link to Products page.    
&nbsp;    
3. All Items App    
&nbsp;    
This view is split in two columns. One the left side you will have a column where you can sort the products by category (there are 2 main categories - sunglasses and handbags) or by designer.     
&nbsp;    
On the right you will find all products displayed in two columns. They are sortable by name and price.  Also on top you will have a number of all the products currently at the shop and depending on the category chosen, the number should change accordingly. By hovering over the items, image will change. The page contains also a name, designer and their price and little cart item, where you can put the item to the shopping bag swiftly without the need of accessing full information.
&nbsp;    
By clicking on a title of the item you will be redirected to a Single Product view - which is way more detailed than everywhere else on the site. On top of previous information you will also find 4-image carousel and description of the item. You will also be able to add the product to the cart from this view.     
A superuser will have an additional options to edit or delete an item. By clicking edit - owner of the page will be redirected to the form with all information of the chosen item already filled in, allowing them to make changes fast. By clicking delete - item will disappear from the database. There is no confirmation of this action.   
&nbsp;    
4. New Arrivals App    
&nbsp;    
This is probably the most attention grabbing page including 9 images with short information about each product. Those images have a hover effect over them. This was a landing page on original Amado template but as explained above - I have amended it for a better user experience.     
On a click you are taken to 'single_product' view where you will find a full description of each item.     
&nbsp;    
This page of the website can be amended by a superuser to feature latest arrivals to the shop in admin panel (as the app comes with its own model and fixture.json)    
&nbsp;    
5. Cart App    
&nbsp;    
The shopping bag application has two main columns. Detailed information what is in your shopping bag with option to delete an item is displayed kind of in the middle. As the number of item for sell is usually 1, there is no option to amend it.     
&nbsp;    
To the right there will be financial information of your order: price, delivery cost and grand total. From there there are couple of options available, either to keep shopping or proceed to checkout.     
&nbsp;    
6. Checkout App    
&nbsp;    
Similar to the shopping bag app, this page has also two main sections. Financial cart details to the right and to the left you will find a checkout information section, where the user needs to input their billing and credit card details. The credit card section is linked to Stripe. The form needs to be fully validated before submission and card (it can be a test card from Stripe page) also needs to be valid.    
I have been using the Visa card: 4242 4242 4242 4242. You can find more information on how to use the Stripe testing cards [here](https://stripe.com/docs/testing).  
&nbsp;    
7. Profile App    
 &nbsp;    
Similar to previous apps, this application also has two main sections. Default Billing information - where logged in user can save and update the info about their delivery address. Each time new order is made, the details will be pulled through. And another section contains order history details (order number, date, items and full price). When clicked it loads an original details of the order.     
&nbsp;    
### [](https://github.com/sneachda/vintage_ms4#future) Features still to implement 
&nbsp; 
With little time left to polish off this project there are certain things I would like to have, but couldn't sort it in time frame given, due to the personal circumstances:    
&nbsp;    
- Full Subscription Service    
I have looked for simple and fast solution for this and by browsing online and seeing it being used in other student's projects, I came across EmailJS free service, which allows me to send automated email thanking for the subscription. In the future I would like to link it to Django framework.  
- Contact Us  
At this stage of business progression I didn't find necessary to include separate contact page. People most likely will be checking our social media accounts before any purchase and it's simple enough to get in touch though them. I have also encourage to do so in 'about us' page.   
With growth I would probably have to introduce another app - contact us where people will be able to drop an email easily.   
This idea would be implemented at the same time when subscription services are improved.   
- Login via Social Links    
I have seen Allauth give you an option to log in via 3rd party social accounts. I didn't have time to explore this further but I do believe going forward it is something to learn as people are more likely to create account via fastest possible route. Another reason for it would be minimising number of passwords to store.     
- Pagination     
As this is a vintage items page, I didn't feel the massive need to include the pagination option for this project, but I believe if the business was to grow, it would be necessary, so users do not need to scroll down for ages, especially on the smaller devices.  
- Sorting Options and Starring System     
I would probably be looking to add a bit more sorting options - especially if I was to include a starring via people opinions.  That would be probably one of the first services to include as people do relay on other people opinions greatly.   
- Proper database control - so when the item is sold out the information will be displayed on the website.   
&nbsp;    
    
># [](https://github.com/sneachda/vintage_ms4#technology-used) Technology Used 
&nbsp;    
Here you can find the list of all the programmes used to create this website:    
    
    
- [Colorlib](https://colorlib.com/) - I sourced my website template from here.    
    
- [PyCharm](https://www.jetbrains.com/pycharm/)  -  IDE for developing this project.            
            
 - [GitHub](https://github.com)  - for remotely storing project's code.    
    
 - [AWS](https://aws.amazon.com/) - Amazon Web Services was used to store the media and static files.  
    
 - [Heroku](https://heroku.com/)  - to host the project.        
&nbsp;    
**Front-End**  
  
 - HTML - to build the foundation of the project.            
            
- CSS  - to style the project.    
    
- Javascript - q number of elements on the site have Javascript functionality.  
&nbsp;    
**Back-End** - [Python](https://www.python.org/)  - back-end programming language.                 
        &nbsp;              
**Libraries and Frameworks**    
 - [Bootstrap](https://getbootstrap.com)  - main responsive modern front-end framework            
            
 - [Google Fonts](https://fonts.google.com/)  - to import fonts.            
            
 - [FontAwesome](https://fontawesome.com/)  - to provide icons.            
            
 - [JQuery](https://jquery.com/)  - to simplify DOM manipulation    
    
- [Django](https://www.djangoproject.com/)  - Python framework for building the project.    
    
- [Gunicorn](https://pypi.org/project/gunicorn/)  - a Python WSGI HTTP Server to enable deployment to Heroku.    
- [Psycopg2](https://pypi.org/project/psycopg2/)  - to enable the PostgreSQL database to function with Django.    
- [Stripe](https://stripe.com/ie)  - to handle financial transactions.    
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)  - to style Django forms.    
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) - for addressing authentication, registration, account management  
&nbsp;    
#### Databases    
 - [SQlite3](https://www.sqlite.org/index.html)  - a development database.    
  
- [PostgreSQL](https://www.postgresql.org/)  - a production database.    
    
    
&nbsp;    
  
># [](https://github.com/sneachda/vintage_ms4#testing) Testing 
&nbsp;         
### [](https://github.com/sneachda/vintage_ms4#devices) Devices 
&nbsp;    
*Manual testing was carried out on mobile devices and desktop.* I also tested the site in Developer Tools. Especially useful for this was Chrome and Safari.     
&nbsp;    
### [](https://github.com/sneachda/vintage_ms4#validation) Validation 
&nbsp;    
The code has been validated using:          
      &nbsp;      
 - [W3C Mark-up Validation Service](https://validator.w3.org/)          
          
 - [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)          
           
 - app.py was tested through  [PEP8 Online](http://pep8online.com/)         
   validator.   
    &nbsp;      
        
        
After putting my html through validators I often received code errors due to python. Example below:    
     
     Bad value{% url 'single_product' arrival.product_id %} for attribute href on element a: Illegal character in path segment: { is not allowed.}   

  &nbsp;   
CSS had zero errors. I did keep it short and relied a lot on  
 templates included in Amado but also on bootstrap.  I have tried to manipulate my code by using bootstrap classes as often as possible.  
   &nbsp;   
After running my python files through PEP8, it turns out I received few   `line too long (85 > 79 characters)` I have decided not to correct this error as visually I believed it worked better. I will take a note of it for future projects though.   
  &nbsp;   
    
### [](https://github.com/sneachda/vintage_ms4#user-scenarios) User Scenarios    
 &nbsp;    
As a visitor I have tested all the links to see if navigation is working and have went through the process of creating an order and went all the way through successful completion.     
1. Go to Main Page    
2. Browse the Products     
3. Add an Item to the cart - both via button or cart icon. As said above there is usually a one item available so each time person want to add the same item to the bag, the grand total won't change.   
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
#### Failed bootstrap.min.css SourceMap Load &nbsp;    
Upon load of site this error appears in the browser console: "DevTools failed to load SourceMap: Could not load content for [http://127.0.0.1:8000/static/css/bootstrap.min.css.map](http://127.0.0.1:8000/static/css/bootstrap.min.css.map): HTTP error: status code 404, net::ERR_HTTP_RESPONSE_CODE_FAILURE".    
          
&nbsp;    

># [](https://github.com/sneachda/vintage_ms4#deployment) Deployement     
 &nbsp;    
The Vintage project was developed using the PyCharm and GitHub for version control. It is hosted on the Heroku platform, with static files on  images being hosted in AWS S3 Basket.    
    
### Local Deployment    
 To be able to run this project, the following tools have to be installed:    
    
- An IDE of your choice    
- [Git](https://git-scm.com/)    
- [PIP](https://pip.pypa.io/en/stable/installing/)    
- [Python3](https://www.python.org/download/releases/3.0/)    
    
Apart from that, you also need to create accounts with the following services:    
    
- [Stripe](https://stripe.com/en-ie)    
- [AWS](https://aws.amazon.com/)  to setup the  [S3 basket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)    
- [Gmail](https://mail.google.com/)    
    
#### [](https://github.com/#directions)Directions    
 1. You can save a copy of this repository by clicking the green button  **Clone or download** , then  **Download Zip** button, and after extract the Zip file to your folder.      
    In the terminal window of your local IDE change the directory (CD) to the correct file location (directory that you have just created).    
2. Set up environment variables.      
    Note, that this process will be different depending on IDE you use.      
    In this it was done using the following way:    
        
   - Create  `.env` file in the root directory.    
   - Add  `.env` to the  `.gitignore` file in your project's root directory    
   - In  `.env` file set environment variables with the following syntax:    
        
    import os      
    os.environ["DEVELOPMENT"] = "True"        
    os.environ["SECRET_KEY"] = "Your Secret key"        
    os.environ["STRIPE_PUBLIC_KEY"] = "Your Stripe Public key"        
    os.environ["STRIPE_SECRET_KEY"] = "Your Stripe Secret key"        
    os.environ["STRIPE_WH_SECRET"] = "Your Stripe WH_Secret key"        
   
3. Install all requirements from the  **requirements.txt** file putting this command into your terminal:      
    `pip3 install -r requirements.txt` 4. In the terminal in your IDE migrate the models to create a database using the following commands:      
    `python3 manage.py makemigrations`      
`python3 manage.py migrate` 5. Load the data fixtures(**categories**,  **products**,  **designers**,  ) in that order into the database using the following command:      
    `python3 manage.py loaddata <fixture_name>` 6. Create a superuser to have an access to the the admin panel(you need to follow the instructions then and insert username, email and password):      
    `python3 manage.py createsuperuser` 7. You will now be able to run the application using the following command:      
    `python3 manage.py runserver` 8. To access the admin panel, you can add the  `/admin` path at the end of the url link and login using your superuser credentials.    
    
### Heroku Deployment    
 To deploy the project to  [Heroku](https://heroku.com/)  the following steps need to be completed:    
    
1. Create a  **requirement.txt** file, which contains a list of the dependencies, using the following command in the terminal:      
    `pip3 freeze > requirements.txt` 2. Create a  **Procfile**, in order to tell Heroku how to run the project  
3. `git add`,  `git commit` and  `git push` these files to GitHub repository.      
4. On the  [Heroku](https://heroku.com/)  website you need to create a  **new app**, assigne a name (must be unique),set a region to the closest to you(for my project I set Europe) and click  **Create app**.    
5. Go to  **Resources** tab in Heroku, then in the  **Add-ons** search bar look for  **Heorku Postgres**(you can type  `postgres`), select  **Hobby Dev — Free** and click  **Provision** button to add it to your project.    
6. In Heroku  **Settings** click on  **Reveal Config Vars**.    
7. Set the following config variables there:    
    
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
 8. Copy  **DATABASE_URL's value**(Postrgres database URL) from the Convig Vars and temporary paste it into the default database in  **settings.py**.      
    You can temporary comment out the current database settings code and just paste the following in the settings.py:    
    
    
  
 DATABASES = {            'default': dj_database_url.parse("<your Postrgres database URL here>")         
}   
  Important Note: that's just temporary set up, this URL  **should not be committed and published to GitHub** for security reasons.  
  
9. Migrate the database models to the Postgres database using the following commands in the terminal:      
`python3 manage.py makemigrations` `python3 manage.py migrate` 10. Load the data fixtures(**categories**,  **products**,  **designers**) into the Postgres.  
11. Create a  **superuser** for the Postgres database  
12. You need to remove your Postgres URL database from the settings and uncomment the default DATABASE settings code in the settings.py file.      
Note: for production you get the environment variable 'DATABASE_URL' from the Heroku Config Vars and use Postgress database, while for development you use the SQLite as a default database.      
13. Add your Heroku app URL to  **ALLOWED_HOSTS** in the settings.py file.   
14. You can connect Heroku to GitHub to automatically deploy each time you push to GitHub.      
To do so, from the Heroku dashboard follow the steps:    
    
-   **Deploy** section ->  **Deployment method** -> select  **GitHub** and follow the instructions.   
    
15. After successful deployment, you can view your app bu clicking  **Open App** on Heroku platform.    
    
&nbsp;    
##### Hosting media files with AWS    
 The  **static files** and  **media files** are hosted in the  [AWS S3 Bucket](https://aws.amazon.com/). But you are free to choose any other service you are familiar with.     
 &nbsp; 
 &nbsp; 
    
># [](https://github.com/sneachda/vintage_ms4#credits) Credits    
    
 &nbsp;    
**Code Used**    
 &nbsp;    
 **Amado Template** 
 &nbsp;    
The template used to create the site.    
    
- Source:  [https://colorlib.com/wp/template/amado/](https://colorlib.com/wp/template/amado/)    
- Preview Site:  [https://colorlib.com/preview/#amado](https://colorlib.com/preview/#amado)    
&nbsp;    
  
**Boutique Ado** 
&nbsp;    
I learned so much while creating the above Code Institute mini-project.     
As previous projects gave me enough knowledge on front end design, this one really let me explore what it means to be a Full Stack developer.     
    
I do feel I had to lean heavily on the Boutique Ado's python code - to get such a complex site up and running in a relatively short period of time. The whole Fullstack Frameworks & Django module was heavily investigated while creating this website. I had also looked around other students project for inspiration and ideas and how they married their own code with course material.  
I need to admit I have found couple of students who have used template, which was very helpful while creating this site.   
This was the first time during my studying period I felt a little bit overwhelmed and not entirely sure how to start. I feel like I have had a better grasping on the earlier modules and I do believe I have still a lot to learn if I am to proceed in this field and look for a career change.   
&nbsp;    
    
**Images Used** 
&nbsp;    
I have used the images and all items description from another fabulous vintage website. Therefore I have no rights to them and if I was to develop this site for professional purposes, I would use my own material.     
( [Jean Vintage](https://www.jeanvintage.co.uk/) )     
    
&nbsp;    
>## Disclaimer         
        
 _The content of this website is for educational purposes only._