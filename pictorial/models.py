from django.db import models

class Image(models.Model):
    image_name =models.CharField(max_length =30)
    description =models.CharField(max_length =50)
    image = models.ImageField(upload_to = 'pictures/', default='image',null = True)
    location = models.ForeignKey('Location', on_delete = models.CASCADE,null='True', blank=True)
    category = models.ForeignKey('Category', on_delete = models.CASCADE,null='True', blank=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['image_name']

    def save_image(self):
        self.save() 

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
