from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Build(models.Model):

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
    liked_by = models.ManyToManyField(
        User,
        related_name='liked_builds',
        blank=True
    )

    class Meta:
        ordering = ["-created_on", 'author']
    
    def __str__(self):
        return f"{self.title} | made by {self.author}"
    def total_likes(self):
        return self.liked_by.count()


# Comment code is copied from code institue

class ReviewModel(models.Model):

    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.post`
    """

    build = models.ForeignKey(
        Build, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    rating = models.PositiveIntegerField(choices=((1, '1 star'), (2, '2 star'), (3, '3 star'), (4, '4 star'), (5, '5 star')))
    image = CloudinaryField('image', default='placeholder')
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"{self.body} by {self.author}"
