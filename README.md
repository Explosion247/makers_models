# Makers Models

Heroku link: https://makers-models-e5ef4f65df4a.herokuapp.com/

## Site Overview
The aim of this website is to allow people to create and share their MOC's (My Own Creations), while also letting other people browse to find new designs to build or get some idea's of their own.

This website will allow someone to log in to upload their designs with a name, description and image. They will also be able to leave comments on post and save builds for later by liking the build.

If you are not logged in then you will be able to create an account or just browse the website and see all the builds that have been uploaded.

## Table of content

- [Design](#design)
- - [Colours](#colours)
- - [Wireframes](#wireframes)
- - [User Stories](#user-stories)
- [Features](#features)
- [Deployment and testing](#deployment-and-testing)
- [Technologies Used](#technologies-used)
- [Credits and References](#credits-and-references)
- - [Images](#images)
- - [Code](#code)

## Design

### Colours

![Colour pallet](./static/images/website-colours.png)

### Wireframes

<details>
   <summary> Wireframe of the main page</summary>
   
   ![main page](./static/images/wireframe-main-page.png)
</details>
<br>
While creating the main page, having the image take up the entire width of the page didnt look right as the image was not fully being displayed therefore i decided to reduce the size of the image and put a card along the side, this allowed more information on the page without it looking too crowded.
<br>
<details>
   <summary> Wireframe of the build page</summary>
   
   ![build page](./static/images/wireframe-model-page.png)
</details>
<br>
while making the build page, most of the page is the same as the wireframe, however i decided to add reviews underneath the image to reduce how croweded the comment box was within the tab box. I have also not included similar builds or other builds by this designer as I did not have enough time and decided this was more important on the designers page.

<details>
   <summary> Wireframe of the Designers page</summary>

   ![Designers page](./static/images/wireframe-designers-page.png)
</details>

 On this page i decided to change the users builds into a carousel to reduce blank space on the page, and place the upload build form next to it allowing a user to easily upload an build. I have also added in the ability to like builds and they will show up beneath the form and carosel.

### Pages

<details>
<summary>Main Page</summary>

![Main Page](/static/images/main-page.png)
</details>
<details>
<summary>Build Page</summary>

![Build Page](/static/images/build-page.png)
</details>
<details>
<summary>Account Page</summary>

![Account Page](/static/images/account-page.png)
</details>

### User Stories
<details>
<summary>As a **Lego Designer**, I can **upload and edit my designs** on a website so that I can **share my designs with other people**.</summary>
<ul>
<li> Given the user is logged in, they can upload a lego moc design and blueprints (if supplied)
<li> Given the user is logged in, they can update their lego moc designs
<li> Given the user is logged in, they can delete their logo moc
</ul>
</details>
<br>
<details>
<summary> As a **Lego Designer**, I can **browse and download other peoples designs** on a website so that I can **get ideas for more lego projects**.</summary>
<ul>
<li> A user can browse uploaded designs on the website without being logged in
<li> Given a user is logged in, they can download designs of other users
</ul>
</details>
<br>
<details>
<summary> As a **Lego Designer**, I can **comment on other designs** so that **others will know how easy a build is**.</summary>
<ul>
<li> Given a user is logged in, they can leave a comment on a design
</ul>
</details>
<br>
<details>
<summary> As a **User**, I can **view a designer's page** so that I can **view the other designs they have created**.</summary>
<ul>
<li> A user can open a page about a designer/account to view all their other designs.
</ul>
</details>
<br>
<details>
<summary>As a **Site Admin** I can **create, read, update and delete designs** so that **I can manage the website content**.</summary>
<ul>
<li> Given a logged-in admin, they can create a design page
<li> Given a logged-in admin, they can read a design page
<li> Given a logged-in admin, they can edit a design page
<li> Given a logged-in admin, they can delete a design page
</ul>
</details>
<br>
<details>
<summary>
As a **Site Admin** I can **Approve comments and design pages** so that **other users can view them**</summary>
<ul>
<li> Given a logged-in admin, they can approve an uploaded Design page
<li> Given a logged-in admin, they can approve a Comment
</ul>
</details>
<br>

Out of these user stories, most of the assessment criteria have been met, however some have not, for example being able to look at other users builds have not been implamented yet, the ability to download designs or view the blueprints has not been implamented, and neither has the ability to edit or delete designs once they have been uploaded. These are all things that will be implamented at a later date.

## Features
### Included Features
<ul>
<li> browse sets - On the main page of this website you have the ability to browse the sets that have been uploaded, there is a next button at the bottom to allow you to view more.
<li> information - once you click on the page of a set, it will give you information about the set and allow you to see the reivews about the set.
<li> Reviews - within the build page you are able to see the reviews of the page, but you are also able to create a review of the set, each review has a rating out of 5 to say how much you like the set.
<li> Likes - on each page for the build you have the ability to like the build, this will add it to a list that is available on the account page
<li> account - when using this website, you are able to create an account and log in, then you have access to the account page. This page will show all the builds you have uploaded (using a carousel) and gives you the ability to upload your own build. Finally you have the ability to look at all the builds you have liked and gives you the ability to remove them from the list using the like button underneath
</ul>

### To be included
<ul>
<li> delete and edit builds - once a build is uploaded the only way to delete it or edit it is through the admin panel, i would like to implament a way for the user to edit and delete the build.
<li> delete accounts - accounts can only be accessed by the admins, so to delete an account its the admin that will have to do it. Therefor if the user can delete the account it will allow for better security
<li> ability to upload and download build files - when a user uploads a build, there is no way for them to upload the blueprints for others to use to view them, and once they are uploaded it would be good for other users to download these files for them build the MOC their self
<li> ability to look at others accounts and see their builds - when browsing builds if people like the work of one designer then it would be good to have a page where they can view all of their builds.
</ul>

## Technologies Used
- Django 4.2, Python 3
- Allauth, Crispy Forms (Bootstrap 5), Summernote
- Whitenoise to store static files
- Cloudinary to store media files

## Deployment and Testing
When you first start the project, create a virtual environment using the settings in the bottom left of vscode and clicking command pallet

Once you have created the basic form of django using - django-admin startproject makers_models - python manage.py startapp lego_build
This will create the file format for the project.

Once the files have been created click the source control on VS code and initiate the repository on GitHub, this will allow you to save the files online.

Install all the files within the requirements.txt file
<details>
<ul>
<li>django
<li>django_summernote
<li>django_crispy_form
<li>django_allauth
<li>crispy_bootstrap5
<li>gunicorn
<li>whitenoise
<li>psycopg2
<li>cloudinary
</ul>
</details>

To create the PostgreSQL database use the link provided by code institute and follow the instuctions, once you have finished copy the api key that is provided.

Create a Cloudinary account and copy the cloudinary api key.

Uploading to heroku

When you select your account on heroku, select new and create new app - give the app the name of makers models and ensure the location is set to Europe - once the app is created, link the app with GitHub by selecting the makers_models repository - within the reveal the convigs vars, and create three, CLOUDINARY_URL, DATABASE_URL and SECRET_KEY using the keys that were created before. - On the deploy page, scroll to manual deployment and deploy click deploy branch, aslong as everything is fine the branch will deploy.

## Testing

Every application that is being build requires tesdting to make sure that everything is working correctly. This is to make sure that the user has a good experiance and would like to use the application again. 

### Manual Testing

The first type of testing that will occur will be manual testing, and this helps alot when it comes to reducing errors. as you are creating the application you will do manual testing to ensure it is working before you work on the next section.

The manual testing table is listed below
![Manual Testing table](./static/images/test-table.png)

### Validation Testing

Validation testing is used to ensure that the code is following best practices

### HTML

When testing the HTML using validation testing, there were 3 errors that appeared for the main page, the first 2 were using a list within a for without the ul elements, and the last one was a trailing slash, these were both fixed so there are no more errors for the main page

![Main page validation](/static/images/html-validation-main-page.png)

Testing the build page it came up with the same errors for the main page but it also had an error due to aria-labelledby attribute, to fix this i had to add a role attribute to the div.

![Build page fail](/static/images/html-validation-build-page-fail.png)
![Build page pass](/static/images/html-validation-build-page-pass.png)

When testing the account page, the only errors that appeared are the ones that appeared with the main page because they where within the base.html after fixing these within the base for the previous page.

![account page validation](/static/images/html-validation-account-page.png)

### JavaScript

Testing the JavaScript the only error that appeared was one undefined variable, however this is due to the installation of bootstrap so there are no error within the JavaScript

![JavaScript Validation](/static/images/js-validation.png)

### CSS

when testing the css there were no errors that had appeared

![CSS Validation](/static/images/css-validation.png)

### Lighthouse Testing

Light house testing is used to test the performance, accessibility and best practices, each of these are tested once the website has loaded as they are the frontend of the site. The results for these shown in a 0-100.

Performance is used to check how well the website has loaded, while accessibility is how easy it would be for people to use the website and finally best practices is how the website runs, for example whether a website uses HTTPS or not.

All of these pages have received a similar score within the lighthouse testing, and each of these are due to the same reason. The performance score was around the low 70's due to image delivery. While the best practices have received a score in the mid 50's, this is due to HTTP response, as the site uses HTTP rather than HTTPS. When you load the website google will automatically upgrade the website from HTTP to HTTPS. Finally the Accessibility is in high 90's, the only problem that appears is that the background and foreground colours do not have high enough contrast.

<details>
<summary>Main page lighthouse testing</summary>

![Main page Lighthouse](/static/images/main-page-lighthouse.png)
</details>
<details>
<summary>Build page Lighthouse testing</summary>

![Build page lighthouse](/static/images/build-page-lighthouse.png)
</details>
<details>
<summary>Account page lighthouse testing</summary>

![Account page lighthouse](/static/images/account-page-lighthouse.png)
</details>




## Credits and References
 
### Images
#### build images and info
- [MOC - 10337 Miami Vice Ferarri Testarossa](https://rebrickable.com/mocs/MOC-245226/firas_legocars/10337-miami-vice-ferarri-testarossa/#details)
- [MOC - Rivendell Display Base](https://rebrickable.com/mocs/MOC-243472/rebelnili/rivendell-display-base/#details)
- [MOC - Castle Grayskull (2x 31168 + 2x 31171)](https://rebrickable.com/mocs/MOC-244703/anderson_brick_art/castle-grayskull-2x-31168-2x-31171/#details)
- [MOC - Oak Corner (Modular)](https://rebrickable.com/mocs/MOC-243252/Thibau_g/oak-corner-modular/#details)
- [MOC - European Harvester Pack](https://rebrickable.com/mocs/MOC-243549/lars_4444/european-harvester-pack/#details)
- [MOC - Medieval Bakery](https://rebrickable.com/mocs/MOC-108189/Huebre/medieval-bakery/#details)
- [MOC - JCB Fastrac 4220 RC](https://rebrickable.com/mocs/MOC-236947/JF551/jcb-fastrac-4220-rc/#details)
- [MOC - Bugatti Atlantic Concept](https://rebrickable.com/mocs/MOC-244292/SKC_LEGO/bugatti-atlantic-concept/#details)
- [MOC - the Traditional](https://rebrickable.com/mocs/MOC-207865/rebelnili/the-traditional/#details)
- [MOC - Battlestar Galactica](https://rebrickable.com/mocs/MOC-144769/KK_MOCS/battlestar-galactica/#details)
- [MOC - LEGO Space Marine Tahu ( Warhammer 40K + BIONICLE )](https://rebrickable.com/mocs/MOC-156725/Demon1408/lego-space-marine-tahu-warhammer-40k-bionicle/#details)

#### Images

- [Lego 3d model](https://www.brothers-brick.com/tag/minimal/)
- [lego pin](https://rebrickable.com/media/parts/elements/4184169.jpg)
- [Lego waving character](https://legothemotionpicture.fandom.com/wiki/Emmet_Brickowski#The_LEGO_Movie)
- [lego city](https://www.youtube.com/watch?v=GLSLUwJn7rk)
- [logo - created through logo generator](https://pixella.ai/en/home)

### Code

- Chat GPT has been used to help with problem
- code institute has been used for the basis of the code
- [W3schools django template](https://www.w3schools.com/django/index.php)





