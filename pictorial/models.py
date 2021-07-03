from django.db import models

class Image(models.Model):
    image_name =models.CharField(max_length =30)
    description =models.CharField(max_length =50)
    image = models.ImageField(upload_to = 'pic/', default='image',null = True)
    location = models.ForeignKey('Location', on_delete = models.CASCADE)
    category = models.ForeignKey('Category', on_delete = models.CASCADE)

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name