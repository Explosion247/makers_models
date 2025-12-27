# Makers Models

A Django 4.2 site for sharing LEGO builds, with authentication via Allauth, reviews/comments, and static assets served by Whitenoise.

## Table of Contents
- Features
- Tech Stack
- Project Structure
- Local Setup
- Running Locally
- Static Files
- Deployment (Heroku)
- Environment Variables
- Tests
- Troubleshooting
- License

## Features
- User registration/login via Django Allauth.
- Lego build pages with reviews/comments.
- Summernote WYSIWYG editing.
- Crispy Bootstrap 5 forms.
- Static/media served via Whitenoise/Cloudinary (prod).

## Tech Stack
- Django 4.2, Python 3.x
- Allauth, Crispy Forms (Bootstrap 5), Summernote
- Whitenoise for static files
- Cloudinary for media (if enabled)

## Project Structure
- `makers_models/` – core settings/urls/wsgi
- `lego_build/` – app code (views/models/templates/static)
- `templates/` – base templates
- `static/` – local static assets (css/js/images)
- `staticfiles/` – collected static (production)

## Local Setup
1) Create venv and install deps:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   pip install -r requirements.txt

SECRET_KEY=your-secret
DATABASE_URL=sqlite:///db.sqlite3   # or your DB URL
CLOUDINARY_URL=...                   # if using Cloudinary

python manage.py migrate
python manage.py runserver

python manage.py test


Want me to apply this to `README.md`? Approve writes and I’ll save it.






This is the start of the read me

error - unable to get variables to function within html, due to using a class model i was unsure about the value to use for the html

fix - after speeking to my teacher, he was able to point out what variable i should be using which was object_list.

error - when on heroku, atempting to log in would cause google to flag a Dangerious page claiming the website was phishing for imformation

fix - this has fixed its self with later deployment, i am unsure about why as this did not appear when hosting locally

errors - when trying to submit a comment it would come up with 'ReviewModel' object is not iterable

fix - On the views page, rename reviews within the if statement to review, the wrong variable was being sent into the render() function

error - When editing the reviews, the edit would bring up both the review and the ratings

fix - to fix this i separated the inputs into two separate div's and then in the comments.js file look for id=review_body to ensure that only the text would appear

error - when loading the reviews, if you had uploaded an image it would not display the image but would show the url

temporary fix - remove the option to upload an image and remove the displaying of the image.

error - when trying to load the accounts page it would come up with 'Page not found'

fix - The urls were in the wrong order so it was matching another page before finding the correct one