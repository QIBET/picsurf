from django.db import models

class Image(models.Model):
    image_name =models.CharField(max_length =30)
    description =models.CharField(max_length =50)
    image = models.ImageField(upload_to = 'pictures/',blank = True)
    location = models.ForeignKey('Location', on_delete = models.CASCADE,null='True', blank=True)
    category = models.ForeignKey('Category', on_delete = models.CASCADE,null='True', blank=True)

    def __str__(self):
        return self.image_name
    

    def save_image(self):
        self.save() 
    
    @classmethod
    def get_pics(cls):
        pics = cls.objects.all()
        return pics 
    @classmethod
    def search_by_category(cls,category):
        pictures = Image.objects.filter(category__name__icontains=category)
        return pictures


   
class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
        
    def save_location(self):
        self.save() 
class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save() 
