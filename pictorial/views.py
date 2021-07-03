from django.shortcuts import render
from pictorial.models import Image


# Create your views here.
def pictorial(request):
    pics = Image.all_photos()
    return render(request, 'pictorial.html',{"all_photos":pics})

