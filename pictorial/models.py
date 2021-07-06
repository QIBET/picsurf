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
    
    def delete_image(self):
        self.delete()
    
    @classmethod
    def get_pics(cls):
        pics = cls.objects.all()
        return pics 
    @classmethod
    def search_by_category(cls,category):
        pictures = cls.objects.filter(category__name__icontains=category)
        return pictures

    @classmethod
    def update_image(cls,current_value,new_value):
        fetched_object = Image.objects.filter(image_name=current_value).update(image_name=new_value)
        return fetched_object
    
    @classmethod
    def filter_by_location(cls,location):
        location_result = cls.objects.filter(image_location_id=location)
        return location_result;   


   
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
