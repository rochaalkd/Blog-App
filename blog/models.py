from tkinter import CASCADE
from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    author=models.ForeignKey('auth.User',
    on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    body=models.TextField()
    image=models.ImageField(upload_to='blog',null=True,blank=True)


    def __str__(self):
       return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
    
    