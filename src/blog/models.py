from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    # on_delete=models.CASCADE means if the user is deleted, 
    # we want to delete all the posts from that user as well. 
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    title       = models.CharField(max_length=100)
    content     = models.TextField()
    image       = models.ImageField(upload_to = "blog_img/", blank=True)
    
    # Make sql result more script
    def __str__(self):
        return self.title

