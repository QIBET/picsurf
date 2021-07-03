from pictorial.models import Image
from django.shortcuts import render


# Create your views here.
def pictorial(request):
    pics = Image.all_photos()
    return render(request, 'pictorial.html',{"pics":pics})
