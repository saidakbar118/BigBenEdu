from django.db import models

class About(models.Model):
    name = models.CharField(max_length=120)
    text = models.TextField()
    name1 = models.CharField(max_length=120)
    text1 = models.TextField()
    name2 = models.CharField(max_length=120)
    text2 = models.TextField()
    
    
class Images(models.Model):
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    image4 = models.ImageField(upload_to='images/')
    
class Text(models.Model):
    name = models.CharField(max_length=90)
    text = models.TextField()
    image = models.ImageField()
    name1 = models.CharField(max_length=90)
    text1 = models.TextField()
    image1 = models.ImageField()
    name2 = models.CharField(max_length=90)
    text2 = models.TextField()
    image2 = models.ImageField()
    name3 = models.CharField(max_length=90)
    text3 = models.TextField()
    image3 = models.ImageField()


