from django.test import TestCase
from .models import Image,Category,Location

class ImageTestClass(TestCase):
    def setUp(self):
        self.new_image= Image(image_name = 'burger', description ='Food and snacks', location = "Nairobi",category = "foods")

