from django.shortcuts import render


# Create your views here.
def pictorial(request):
    return render(request, 'pictorial.html')
