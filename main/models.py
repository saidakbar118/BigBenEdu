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
    
    
class Category(models.Model):
    cover_image = models.ImageField(upload_to='album/')

    def __str__(self):
        return f"Category {self.id}"


class Photo(models.Model):
    category = models.ForeignKey(Category, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='album/')

    def __str__(self):
        return f"Photo {self.id} (Category {self.category.id})"

