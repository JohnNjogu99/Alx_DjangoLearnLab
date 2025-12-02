from django.db import models               # Import Django ORM tools
from django.contrib.auth.models import User # Import built-in User model

class Post(models.Model):                   # Define a new database table called Post
    title = models.CharField(max_length=200)   # Short text field for the post title
    content = models.TextField()               # Large text field for blog content
    published_date = models.DateTimeField(auto_now_add=True) # Auto-set when created
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Link to User

    def __str__(self):
        return self.title   # Display title in admin instead of "Post object"
