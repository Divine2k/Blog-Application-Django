from statistics import mode
from django.db import models
from django.utils import timezone 
from django.urls import reverse
import django
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #To activate it during hitting the publish button
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)
    #Redirect
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comments(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comments = models.BooleanField(default=False)
    

    def approve(self):
        self.approved_comments = True
        self.save()
    #Redirect
    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text