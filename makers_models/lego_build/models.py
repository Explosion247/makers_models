from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):

    # add field for piece count and theme e.g. technic

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="build_post"
    )
    image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on", 'author']
    
    def __str__(self):
        return f"{self.title} | made by {self.author}"
    


# Comment code is copied from code institue

class Review(models.Model):
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments_author"
    )
    image = CloudinaryField('image', default='placeholder')
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
    
    def __str__(self):
        return f"Comment {self.body} by {self.author}"