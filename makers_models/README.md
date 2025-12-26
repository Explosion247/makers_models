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