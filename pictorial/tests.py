from django.test import TestCase
from .models import Image,Category,Location

class ImageTestClass(TestCase):
    def setUp(self):
        self.new_image= Image(image = 'burger', description ='Food and snacks')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
     # Testing Save Method

    def test_save_image(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)